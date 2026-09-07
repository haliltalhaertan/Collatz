#!/usr/bin/env python3
"""
audit_integrity.py -- protocol item A for research_manager/exploratory/prefix_bridge_20260906/.
Reads package bytes for hashing/diffing only; executes nothing from the package.
  * recompute SHA-256 of every on-disk file; compare with SHA256SUMS.txt and PACKAGE_SHA256SUMS.txt
  * detect CRLF per file; compute LF-normalised hash to show which byte form the lists were made on
  * list ZIP members, compare member bytes with on-disk bytes
  * check the V2 output-hash claim 3b6fe2ac... and the V1->V2 "exactly two substitutions" claim (difflib)
"""
import hashlib, os, zipfile, json, difflib, sys

PKG = r"C:/Users/MDP/Documents/ChatGPT/Collatz/research_manager/exploratory/prefix_bridge_20260906"
ZIP = PKG + ".zip"
CLAIMED_V2_OUTPUT_HASH = "3b6fe2ac8166cee1f7891d4f3abfc4b70a847c3085e4d7c44fde8e12ce084c3d"
out = {"package": PKG, "files": {}, "lists": {}, "zip": {}, "v2_hash_claim": {}, "v1_v2_diff": {}}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def parse_list(path):
    d = {}
    for line in open(path, "rb").read().decode("utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        h, name = line.split(None, 1)
        d[name.lstrip("*").replace("\\", "/")] = h
    return d


disk = {}
for dp, dn, fn in os.walk(PKG):
    for f in fn:
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, PKG).replace("\\", "/")
        b = open(p, "rb").read()
        disk[rel] = b
        out["files"][rel] = {"size": len(b), "sha256": sha(b), "crlf_count": b.count(b"\r\n"),
                             "lone_lf_count": b.count(b"\n") - b.count(b"\r\n"),
                             "sha256_lf_normalised": sha(b.replace(b"\r\n", b"\n"))}

for lst in ("SHA256SUMS.txt", "PACKAGE_SHA256SUMS.txt"):
    claimed = parse_list(os.path.join(PKG, lst))
    res = {"entries": len(claimed), "match": [], "mismatch": [], "missing_on_disk": [], "on_disk_not_listed": []}
    for name, h in claimed.items():
        if name not in disk:
            res["missing_on_disk"].append(name)
        elif out["files"][name]["sha256"] == h:
            res["match"].append(name)
        else:
            res["mismatch"].append({"file": name, "claimed": h, "actual": out["files"][name]["sha256"],
                                    "matches_lf_normalised": out["files"][name]["sha256_lf_normalised"] == h})
    res["on_disk_not_listed"] = sorted(set(disk) - set(claimed))
    out["lists"][lst] = res
    print(f"{lst}: entries={res['entries']} match={len(res['match'])} mismatch={len(res['mismatch'])} "
          f"missing={res['missing_on_disk']} unlisted_on_disk={res['on_disk_not_listed']}")

# CRLF summary
crlf_files = [k for k, v in out["files"].items() if v["crlf_count"] > 0]
print("files containing CRLF:", crlf_files)
for k in crlf_files:
    v = out["files"][k]
    print(f"  {k}: crlf={v['crlf_count']} lone_lf={v['lone_lf_count']} sha_on_disk={v['sha256'][:16]}.. sha_lf_norm={v['sha256_lf_normalised'][:16]}..")

# ZIP
z = zipfile.ZipFile(ZIP)
zres = {"zip_sha256": sha(open(ZIP, "rb").read()), "members": [], "identical": 0, "different": 0,
        "missing_on_disk": [], "on_disk_not_in_zip": []}
names = []
for info in z.infolist():
    names.append(info.filename)
    b = z.read(info)
    rec = {"name": info.filename, "size": len(b), "sha256": sha(b), "datetime": list(info.date_time)}
    if info.filename in disk:
        rec["identical_to_disk"] = (sha(b) == out["files"][info.filename]["sha256"])
        zres["identical" if rec["identical_to_disk"] else "different"] += 1
    else:
        zres["missing_on_disk"].append(info.filename)
    zres["members"].append(rec)
zres["on_disk_not_in_zip"] = sorted(set(disk) - set(names))
out["zip"] = zres
print(f"ZIP sha256={zres['zip_sha256']} members={len(names)} identical={zres['identical']} different={zres['different']} "
      f"missing_on_disk={zres['missing_on_disk']} on_disk_not_in_zip={zres['on_disk_not_in_zip']}")

# V2 output hash claim
hits = [k for k, v in out["files"].items() if v["sha256"] == CLAIMED_V2_OUTPUT_HASH]
out["v2_hash_claim"] = {"claimed": CLAIMED_V2_OUTPUT_HASH, "files_with_this_hash": hits,
                        "RESULTS_V2_lf_normalised_hash": out["files"]["checks/RESULTS_V2.json"]["sha256_lf_normalised"]}
print("claimed V2 output hash matches on-disk file(s):", hits,
      "| LF-normalised RESULTS_V2.json hash:", out["v2_hash_claim"]["RESULTS_V2_lf_normalised_hash"][:16] + "..")
# also: does RESULTS_V2.json record its own source hash equal to the on-disk V2 source hash?
rv2 = json.loads(disk["checks/RESULTS_V2.json"].decode("utf-8"))
rv1 = json.loads(disk["checks/RESULTS.json"].decode("utf-8"))
out["results_internal_hashes"] = {
    "V2_source_sha256_recorded": rv2["source_sha256"], "V2_source_sha256_disk": out["files"]["checks/exact_prefix_checks_v2.py"]["sha256"],
    "V1_source_sha256_recorded": rv1["source_sha256"], "V1_source_sha256_disk": out["files"]["checks/exact_prefix_checks.py"]["sha256"],
    "plan_sha256_recorded_V1": rv1["plan_sha256"], "plan_sha256_recorded_V2": rv2["plan_sha256"],
    "plan_sha256_disk": out["files"]["checks/PLAN.md"]["sha256"],
    "V1_failures": len(rv1["failures"]), "V1_failure_tests": sorted(set(f["test"] for f in rv1["failures"])),
    "V1_checks_by_name": rv1["checks_by_name"], "V2_failures": len(rv2["failures"]), "V2_checks_by_name": rv2["checks_by_name"],
    "V1_paths_total": rv1["paths_total"], "V2_paths_total": rv2["paths_total"],
    "V1_start_utc": rv1["start_utc"], "V2_start_utc": rv2["start_utc"], "V1_elapsed": rv1["elapsed_seconds"], "V2_elapsed": rv2["elapsed_seconds"],
    "V1_residue_keys": rv1["residue_keys"], "V2_residue_keys": rv2["residue_keys"], "V2_observed_B_mod16": rv2["observed_B_mod16"],
    "V2_target_sample": rv2["target_sample"], "V1_input_hashes_unchanged": rv1["input_hashes_unchanged"], "V2_input_hashes_unchanged": rv2["input_hashes_unchanged"]}
print("internal hash consistency:", json.dumps({k: v for k, v in out["results_internal_hashes"].items() if "sha256" in k}, indent=0))
print("V1: paths", rv1["paths_total"], "failures", len(rv1["failures"]), "tests failing", out["results_internal_hashes"]["V1_failure_tests"],
      "checks", sum(rv1["checks_by_name"].values()), "| V2: paths", rv2["paths_total"], "failures", len(rv2["failures"]), "checks", sum(rv2["checks_by_name"].values()))
print("V1 start", rv1["start_utc"], "V2 start", rv2["start_utc"])

# V1 -> V2 diff
v1 = disk["checks/exact_prefix_checks.py"].decode("utf-8").splitlines()
v2 = disk["checks/exact_prefix_checks_v2.py"].decode("utf-8").splitlines()
ud = list(difflib.unified_diff(v1, v2, "checks/exact_prefix_checks.py", "checks/exact_prefix_checks_v2.py", lineterm="", n=0))
changed = [l for l in ud if (l.startswith("+") or l.startswith("-")) and not l.startswith("+++") and not l.startswith("---")]
out["v1_v2_diff"] = {"unified_diff": ud, "removed_lines": [l for l in changed if l.startswith("-")],
                     "added_lines": [l for l in changed if l.startswith("+")], "v1_lines": len(v1), "v2_lines": len(v2)}
print("V1->V2 unified diff (n=0):")
for l in ud:
    print("   ", l)
print("removed", len(out["v1_v2_diff"]["removed_lines"]), "added", len(out["v1_v2_diff"]["added_lines"]))

with open(sys.argv[1] if len(sys.argv) > 1 else "audit_integrity_results.json", "w", encoding="utf-8", newline="\n") as f:
    json.dump(out, f, indent=1)
