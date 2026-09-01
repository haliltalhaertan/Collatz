#!/usr/bin/env python3
"""Independent, read-only checks for the CP20 Task 8B3 E4 audit package."""

from __future__ import annotations

import argparse
import cmath
import csv
import hashlib
import json
import math
import platform
import sys
import time
from pathlib import Path


EXPECTED_AUDIT_ZIP = "a99185ffc4e9daa527a3ee54b59df8ced02bed65490421ce3f9a028119f8c408"
EXPECTED_COMPLETE_ZIP = "95190d5cbdb633ad049720897b28c73898be229832549153c1fe9ee03b9c4cb1"
DEPTHS = (1000, 2000, 4000, 6000, 8000)
CS = (4, 7)
D_MIN, D_MAX = -64, 32


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_manifest(root: Path, manifest: Path, expected_count: int) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for raw in manifest.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        expected, relative = raw.split("  ", 1)
        target = root / Path(relative)
        actual = sha256(target) if target.is_file() else None
        rows.append(
            {
                "path": relative,
                "expected_sha256": expected,
                "actual_sha256": actual,
                "match": actual == expected,
            }
        )
    if len(rows) != expected_count or not all(bool(row["match"]) for row in rows):
        raise AssertionError(f"manifest failure: {manifest}")
    return {
        "entry_count": len(rows),
        "all_match": True,
        "manifest_sha256": sha256(manifest),
        "rows": rows,
    }


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def direct_reduced_checkpoint(rmax: int = 1000) -> dict[tuple[int, int], complex]:
    """Recompute the reduced recurrence without importing supplied E4 code."""
    beta = math.log2(3.0) - 1.0
    selected_d = (D_MIN, -8, D_MAX)
    nmax = math.floor(beta * rmax) + max(selected_d)
    previous: dict[int, list[complex]] = {}
    for c in CS:
        base_residue = pow(2, -c, 3)
        base = cmath.exp(2j * math.pi * base_residue / 3.0)
        previous[c] = [base] * (nmax + 1)

    modulus = 3
    for r in range(2, rmax + 1):
        modulus *= 3
        current: dict[int, list[complex]] = {}
        for c in CS:
            values = [0j] * (nmax + 1)
            residue = pow(2, r - 1 - c, modulus)
            for n in range(nmax + 1):
                phase = cmath.exp(2j * math.pi * (residue / modulus))
                inherited = phase * previous[c][n]
                if n == 0:
                    values[n] = inherited
                else:
                    denominator = r + n - 1.0
                    values[n] = (n / denominator) * values[n - 1] + ((r - 1.0) / denominator) * inherited
                residue = (2 * residue) % modulus
            current[c] = values
        previous = current

    floor_value = math.floor(beta * rmax)
    return {(c, d): previous[c][floor_value + d] for c in CS for d in selected_d}


def check_rotation_and_coordinates() -> dict[str, object]:
    beta = math.log2(3.0) - 1.0
    phases = [0.0, beta, math.nextafter(beta, 0.0), math.nextafter(beta, 1.0), 0.125, 0.875]
    max_rotation_error = 0.0
    max_coordinate_error = 0.0
    for theta0 in phases:
        theta = theta0
        epsilon_sum = 0
        for n in range(1, 257):
            epsilon = 1 if theta < beta else 0
            theta = theta - beta + epsilon
            epsilon_sum += epsilon
            max_rotation_error = max(max_rotation_error, abs(epsilon_sum - (n * beta + theta - theta0)))
        for d in (-2, 0, 3):
            epsilon = 1 if theta0 < beta else 0
            transformed = theta0 - beta + epsilon
            x = d - theta0
            max_coordinate_error = max(
                max_coordinate_error,
                abs(((d - 1) - theta0) - (x - 1)),
                abs(((d + epsilon) - transformed) - (x + beta)),
            )
            d_back = math.ceil(x)
            theta_back = d_back - x
            if d_back != d or abs(theta_back - theta0) > 2e-15:
                raise AssertionError("coordinate inverse failed")
    if max_rotation_error > 3e-13 or max_coordinate_error > 3e-15:
        raise AssertionError("rotation/coordinate identity failed")
    return {
        "phases_include_exact_0_and_beta": True,
        "max_rotation_identity_abs_error": max_rotation_error,
        "max_coordinate_shift_abs_error": max_coordinate_error,
    }


def check_walk() -> dict[str, object]:
    alpha = math.log2(3.0)
    beta = alpha - 1.0
    a = beta / alpha
    b = 1.0 / alpha
    mass = b / (1.0 - a)
    mean_j = a / b
    variance_j = a / (b * b)
    grid = (-0.75, -0.25, 0.0, 0.25, 0.75)
    moments = []
    for s in grid:
        multiplier = b * math.exp(beta * s) / (1.0 - a * math.exp(-s))
        moments.append({"s": s, "unrolled_multiplier": multiplier})
        if s != 0.0 and not multiplier > 1.0:
            raise AssertionError("strict exponential obstruction failed")
    if max(abs(mass - 1.0), abs(mean_j - beta), abs(variance_j - alpha * beta)) > 2e-15:
        raise AssertionError("critical-walk moment failure")
    return {
        "alpha": alpha,
        "beta": beta,
        "a": a,
        "b": b,
        "mass": mass,
        "mean_J": mean_j,
        "variance_J": variance_j,
        "mgf_domain": f"s > log(a) = {math.log(a):.17g}",
        "multiplier_grid": moments,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-zip", type=Path, required=True)
    parser.add_argument("--complete-zip", type=Path, required=True)
    parser.add_argument("--audit-root", type=Path, required=True)
    parser.add_argument("--e3-root", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, required=True)
    args = parser.parse_args()
    started = time.perf_counter()

    audit_hash = sha256(args.audit_zip)
    complete_hash = sha256(args.complete_zip)
    if audit_hash != EXPECTED_AUDIT_ZIP or complete_hash != EXPECTED_COMPLETE_ZIP:
        raise AssertionError("ZIP provenance failure")

    audit_manifest = verify_manifest(
        args.audit_root,
        args.audit_root / "CP20_TASK8B3_E4_AUDIT_SHA256SUMS.txt",
        28,
    )
    e3_manifest = verify_manifest(args.e3_root, args.e3_root / "SHA256SUMS.txt", 23)

    e4 = args.audit_root / "E4"
    profiles = read_csv(e4 / "CP20_TASK8B3_E4_OFFSET_PROFILES.csv")
    boundaries = read_csv(e4 / "CP20_TASK8B3_E4_BOUNDARY_SENSITIVITY.csv")
    if len(profiles) != 970 or len(boundaries) != 40:
        raise AssertionError("CSV row-count failure")
    if {int(row["r"]) for row in profiles} != set(DEPTHS):
        raise AssertionError("profile depth scope failure")
    if {int(row["C"]) for row in profiles} != set(CS):
        raise AssertionError("profile C scope failure")
    if {int(row["d"]) for row in profiles} != set(range(D_MIN, D_MAX + 1)):
        raise AssertionError("profile offset scope failure")

    profile_index = {(int(row["r"]), int(row["C"]), int(row["d"])): row for row in profiles}
    direct = direct_reduced_checkpoint()
    checkpoint_rows = []
    max_complex_error = 0.0
    max_scaled_complex_error = 0.0
    for (c, d), recomputed in sorted(direct.items()):
        source = profile_index[(1000, c, d)]
        supplied = complex(float(source["re"]), float(source["im"]))
        supplied_h = complex(float(source["h_re"]), float(source["h_im"]))
        complex_error = recomputed - supplied
        scaled_error = 1000.0 * recomputed - supplied_h
        max_complex_error = max(max_complex_error, abs(complex_error))
        max_scaled_complex_error = max(max_scaled_complex_error, abs(scaled_error))
        checkpoint_rows.append(
            {
                "r": 1000,
                "C": c,
                "d": d,
                "recomputed_re": recomputed.real,
                "recomputed_im": recomputed.imag,
                "supplied_re": supplied.real,
                "supplied_im": supplied.imag,
                "complex_error_re": complex_error.real,
                "complex_error_im": complex_error.imag,
                "complex_error_abs": abs(complex_error),
                "scaled_complex_error_abs": abs(scaled_error),
            }
        )
    if max_complex_error >= 5e-11 or max_scaled_complex_error >= 5e-8:
        raise AssertionError("independent recurrence checkpoint failure")

    boundary_max_formula_error = 0.0
    selected_boundary_rows = []
    for row in boundaries:
        exact = complex(float(row["exact_h_re"]), float(row["exact_h_im"]))
        approximate = complex(float(row["approx_h_re"]), float(row["approx_h_im"]))
        declared = float(row["abs_error"])
        formula_error = abs(abs(approximate - exact) - declared)
        boundary_max_formula_error = max(boundary_max_formula_error, formula_error)
        if int(row["r"]) == 8000:
            selected_boundary_rows.append(
                {
                    "r": 8000,
                    "C": int(row["C"]),
                    "scheme": row["scheme"],
                    "declared_abs_error": declared,
                    "recomputed_abs_error": abs(approximate - exact),
                }
            )
    if boundary_max_formula_error > 2e-14:
        raise AssertionError("boundary error column failure")

    engine_text = (e4 / "CP20_TASK8B3_E4_ENGINE.cs").read_text(encoding="utf-8")
    analyzer_text = (e4 / "CP20_TASK8B3_E4_ANALYZE.py").read_text(encoding="utf-8")
    if 'if (rmax != 8000)' not in engine_text or "DEPTHS = (1000, 2000, 4000, 6000, 8000)" not in analyzer_text:
        raise AssertionError("declared depth guard not found")

    result = {
        "schema": "CP20_TASK8B3_E4_INDEPENDENT_AUDIT_CHECKS_V1",
        "status": "PASS_WITH_REPAIRS",
        "claim_statuses": {
            "audit_zip_and_28_payload_hashes": "PROVED",
            "full_sibling_e3_23_payload_hashes": "PROVED",
            "predeclaration_predates_output_inspection": "UNSUPPORTED",
            "finite_same_phase_unrolling": "PROVED",
            "qualified_infinite_unrolling": "PROVED",
            "cylinder_to_line_conjugacy": "PROVED",
            "centered_critical_walk_and_deterministic_zero_drift": "PROVED",
            "pure_exponential_complex_operator_spectral_obstruction": "PROVED",
            "patched_or_asymptotically_exponential_scope": "REPAIRABLE",
            "polynomial_jump_tail_not_spatial_truncation": "PROVED",
            "local_bv_claim_for_unrolled_operator": "REPAIRABLE",
            "moving_boundary_nonzero_asymptotic": "PROVED",
            "compactness": "OPEN",
            "fixed_target_nonzero_profile": "OPEN",
            "profile_fits_phase_widths_decay_and_boundary_sensitivity": "NUM",
        },
        "runtime": {
            "elapsed_seconds": time.perf_counter() - started,
            "python": sys.version,
            "platform": platform.platform(),
            "script_sha256": None,
        },
        "provenance": {
            "audit_zip_sha256": audit_hash,
            "complete_zip_sha256": complete_hash,
            "audit_manifest": audit_manifest,
            "e3_manifest": e3_manifest,
        },
        "scope": {
            "profile_rows": len(profiles),
            "boundary_rows": len(boundaries),
            "depths": list(DEPTHS),
            "C_values": list(CS),
            "d_range": [D_MIN, D_MAX],
            "source_depth_guard_8000": True,
            "predeclaration_temporal_order": "UNSUPPORTED_BY_PACKAGE_TIMESTAMPS_OR_EXTERNAL_SEAL",
        },
        "identities": check_rotation_and_coordinates(),
        "critical_walk": check_walk(),
        "reduced_recurrence": {
            "checkpoint_rows": checkpoint_rows,
            "max_complex_error_abs": max_complex_error,
            "max_scaled_complex_error_abs": max_scaled_complex_error,
        },
        "boundary_sensitivity": {
            "max_abs_error_column_recalculation_difference": boundary_max_formula_error,
            "selected_r8000_rows": selected_boundary_rows,
            "oracle_is_implementation_control_only": True,
        },
    }
    result["runtime"]["script_sha256"] = sha256(Path(__file__))
    args.output_json.write_text(
        json.dumps(result, ensure_ascii=False, allow_nan=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"audit ZIP SHA-256: {audit_hash} PASS")
    print(f"complete ZIP SHA-256: {complete_hash} PASS")
    print("audit payload manifest: 28/28 PASS")
    print("full sibling E3 manifest: 23/23 PASS")
    print(f"CSV scope: profiles={len(profiles)}, boundary={len(boundaries)}, max_r={max(int(r['r']) for r in profiles)} PASS")
    print(f"independent reduced recurrence: 6 complex checkpoints, max |error|={max_complex_error:.3e} PASS")
    print(f"boundary error-column recomputation: max difference={boundary_max_formula_error:.3e} PASS")
    print("predeclaration temporal ordering: UNSUPPORTED (ZIP times normalized; no external pre-output seal)")
    print("ALL INDEPENDENT IMPLEMENTATION CHECKS: PASS WITH DOCUMENTARY REPAIRS")


if __name__ == "__main__":
    main()
