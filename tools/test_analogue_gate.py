"""Targeted PR7 regressions; run with python -B -m unittest discover -s tools -p test_analogue_gate.py -v."""
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

import analogue_gate as gate

ROOT = Path(__file__).resolve().parents[1]


class InputTests(unittest.TestCase):
    def test_empty_or_negative_grid_is_rejected(self):
        for m, r in [(1, 5), (0, 5), (-2, 5), (11, 0), (11, -1)]:
            with self.subTest(m=m, r=r):
                with self.assertRaises(ValueError):
                    gate.run_gate(m, r)

    def test_custom_quantity_accepts_only_exact_int_or_fraction(self):
        from fractions import Fraction
        for value in [0, Fraction(1, 3), Fraction(-2, 5)]:
            with self.subTest(valid=value):
                gate.run_gate(2, 1, quantity=lambda m, r, p, b, value=value: value)
        for value in [True, 0.5, '1/2', float('nan')]:
            with self.subTest(invalid=repr(value)):
                with self.assertRaisesRegex(TypeError, 'exact int or Fraction'):
                    gate.run_gate(2, 1, quantity=lambda m, r, p, b, value=value: value)

    def test_custom_quantity_uses_exact_numeric_equality(self):
        from fractions import Fraction
        def quantity(m, r, p, b):
            if (p, b) == (3, 1):
                return 1
            if (p, b) == (3, -1):
                return Fraction(1, 1)
            return Fraction(2, 1)
        result = gate.run_gate(2, 1, quantity=quantity)
        self.assertTrue(result['comparisons']['3n-1']['identical'])
        self.assertEqual(result['comparisons']['3n-1']['rows_differing'], 0)

    def test_h_step_invalid_parity_is_value_error_even_under_optimization(self):
        with self.assertRaisesRegex(ValueError, 'must be even'):
            gate.H_step(1, 2, 1)

    def test_module_docstring_scopes_exit_two_to_json_output_io(self):
        self.assertIn('JSON output I/O failure', gate.__doc__)
        self.assertNotIn('or output I/O failure.', gate.__doc__)


class CycleTests(unittest.TestCase):
    def test_witnesses_are_positive_closed_and_orbit_ordered(self):
        for p, b in [(3, -1), (5, 1), (1, -3)]:
            with self.subTest(p=p, b=b):
                cycles = gate.find_cycles(p, b, limit=50)
                for cycle in cycles:
                    self.assertTrue(all(x > 0 for x in cycle), cycle)
                    self.assertEqual(cycle[0], min(cycle))
                    self.assertEqual([gate.H_step(x, p, b) for x in cycle],
                                     cycle[1:] + cycle[:1])
                if (p, b) == (5, 1):
                    self.assertIn([1, 3, 8, 4, 2], cycles)
                if (p, b) == (3, -1):
                    self.assertIn([5, 7, 10], cycles)
                if (p, b) == (1, -3):
                    self.assertEqual(cycles, [])


class HistogramTests(unittest.TestCase):
    def test_runtime_rejects_corrupt_stratum_mass(self):
        # Fault injection: denominator drift must not silently produce an energy.
        with patch.object(gate, 'n_k', return_value=0):
            with self.assertRaisesRegex(AssertionError, 'mass'):
                gate.Ecal(3, 2, 3, 1)

    def test_runtime_rejects_missing_strata(self):
        # Fault injection models broken orbit/parity enumeration.
        with patch.object(gate, 'H_step', return_value=0):
            with self.assertRaisesRegex(AssertionError, 'strat'):
                gate.source_histograms(3, 2, 3, 1)

    def test_mass_and_modulo_coarsening_on_default_grid(self):
        for p, b in gate.MAPS.values():
            for m in range(2, 12):
                fine_r = min(5, m)
                fine = gate.source_histograms(m, fine_r, p, b)
                self.assertEqual(set(fine), set(range(1, m + 1)))
                for r in range(1, fine_r + 1):
                    coarse = gate.source_histograms(m, r, p, b)
                    for k, vec in coarse.items():
                        self.assertEqual(sum(vec), gate.n_k(m, k))
                        self.assertEqual(vec, [sum(fine[k][z::1 << r])
                                               for z in range(1 << r)])


class VerdictTests(unittest.TestCase):
    def test_default_grid_separates_observation_from_analytic_scope(self):
        result = gate.run_gate()
        self.assertEqual(result['grid_rows'], 44)
        self.assertEqual(result['comparisons']['3n-1']['rows_differing'], 0)
        self.assertEqual(result['comparisons']['5n+1']['rows_differing'], 38)
        self.assertEqual(result.get('verdict'), 'BLIND_ON_TEST_GRID')
        self.assertEqual(result.get('max_r'), 5)
        proof = result.get('analytical_result') or {}
        self.assertEqual(proof.get('status'), 'PROVED_BLIND')
        self.assertIn('CP24_REPORT.md', proof.get('citation', ''))
        self.assertIn('same hypotheses', proof.get('scope', ''))
        self.assertEqual(result.get('ship_gate', {}).get('approved'), False)
        self.assertEqual(result['comparisons']['3n-1'].get('cycle_search_status'),
                         'WITNESS_FOUND')
        self.assertNotIn('has_nontrivial_cycles', result['comparisons']['3n-1'])

    def test_custom_quantity_never_inherits_ecal_proof_or_claim_approval(self):
        import inspect
        self.assertIn('quantity', inspect.signature(gate.run_gate).parameters)
        for quantity, verdict in [(lambda m, r, p, b: 1, 'BLIND_ON_TEST_GRID'),
                                  (lambda m, r, p, b: p + b, 'VALUE_SEPARATES_ON_TEST_GRID')]:
            result = gate.run_gate(2, 1, quantity=quantity)
            self.assertEqual(result['verdict'], verdict)
            self.assertIsNone(result['analytical_result'])
            self.assertEqual(result['ship_gate'], {'approved': False, 'status': 'NOT_ASSESSED'})

    def test_no_bounded_witness_means_unknown_not_absent(self):
        import inspect
        self.assertIn('quantity', inspect.signature(gate.run_gate).parameters)
        # Exercise actual bounded search with no starts, not a fictional no-cycle oracle.
        original = gate.find_cycles
        with patch.object(gate, 'find_cycles', side_effect=lambda p, b: original(p, b, limit=1)):
            result = gate.run_gate(2, 1, quantity=lambda m, r, p, b: p + b)
        for comparison in result['comparisons'].values():
            self.assertEqual(comparison['cycle_search_status'], 'NOT_FOUND_WITHIN_BOUNDS')
        self.assertFalse(result['ship_gate']['approved'])


class CLITests(unittest.TestCase):
    def cli(self, *args):
        return subprocess.run([sys.executable, '-B', str(ROOT / 'tools/analogue_gate.py'), *args],
                              capture_output=True, text=True, encoding='utf-8')

    def test_default_ship_gate_is_nonzero_not_a_successful_diagnostic(self):
        result = self.cli('--max-m', '2', '--max-r', '1')
        self.assertEqual(result.stderr, '')
        self.assertEqual(result.returncode, 1)
        self.assertIn('SHIP GATE: BLOCKED_FOR_STATED_SCOPE', result.stdout)

    def test_explicit_diagnostic_mode_is_zero_but_not_approval(self):
        result = self.cli('--diagnostic', '--max-m', '2', '--max-r', '1')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('not claim approval', result.stdout)

    def test_invalid_cli_bounds_are_errors_even_in_diagnostic_mode(self):
        for diagnostic in [[], ['--diagnostic']]:
            for args in [('--max-m', '1'), ('--max-m', '0'), ('--max-m', '-2'),
                         ('--max-r', '0'), ('--max-r', '-1'), ('--max-m', '')]:
                with self.subTest(diagnostic=diagnostic, args=args):
                    result = self.cli(*diagnostic, *args)
                    self.assertEqual(result.returncode, 2, result.stderr)
                    self.assertNotIn('Traceback', result.stderr)
                    self.assertNotIn('VERDICT:', result.stdout)

    def test_internal_consistency_failure_is_exit_two(self):
        with patch.object(sys, 'argv', ['analogue_gate.py']), \
             patch.object(gate, 'run_gate', side_effect=AssertionError('injected mass failure')), \
             contextlib.redirect_stderr(io.StringIO()) as err:
            try:
                code = gate.main()
            except AssertionError:
                self.fail('main must convert consistency failure to exit 2')
        self.assertEqual(code, 2)
        self.assertIn('injected mass failure', err.getvalue())

    def test_empty_result_is_never_approved(self):
        with patch.object(sys, 'argv', ['analogue_gate.py', '--diagnostic']), \
             patch.object(gate, 'run_gate', return_value={'grid_rows': 0}), \
             contextlib.redirect_stderr(io.StringIO()):
            try:
                code = gate.main()
            except SystemExit:
                self.fail('diagnostic must parse and explicitly reject empty result')
        self.assertEqual(code, 2)


class DocumentationAndRegressionTests(unittest.TestCase):
    def test_handoff_withdraws_l2_and_scopes_mixed_gram(self):
        text = (ROOT / 'START_HERE_CURRENT_HANDOFF.md').read_text(encoding='utf-8')
        self.assertNotIn('L2 `[FAIL]`', text)
        self.assertIn('L2 `[WITHDRAWN', text)
        self.assertIn('strategic withdrawal', text)
        self.assertIn('auxiliary lemma', text)

    def test_documentation_distinguishes_values_proofs_and_exit_contract(self):
        text = (ROOT / 'tools/ANALOGUE_GATE.md').read_text(encoding='utf-8')
        for required in ['BLIND_ON_TEST_GRID', 'VALUE_SEPARATES_ON_TEST_GRID',
                         'PROVED_BLIND', '--diagnostic', 'NOT_FOUND_WITHIN_BOUNDS',
                         'same hypotheses', 'auxiliary lemma', 'exponential']:
            self.assertIn(required, text)
        self.assertNotIn('replace the `Ecal` call', text)

    def test_raw_values_differ_but_target_truth_agrees_on_33_pairs(self):
        pairs = [(m, s) for m in range(2, 11) for s in range(1, min(4, m) + 1)]
        self.assertEqual(len(pairs), 33)
        for p, b in gate.MAPS.values():
            truths = [gate.Ecal(m, s + 1, p, b) >= gate.Ecal(m + 1, s, p, b)
                      for m, s in pairs]
            self.assertEqual(sum(truths), 33)

    def test_reflection_words_endpoints_and_energy(self):
        for m in range(1, 13):
            for h in range(1, 1 << m, 2):
                reflected = (1 << m) - h
                w = gate.parity_word(h, m, 3, 1)
                self.assertEqual(w, gate.parity_word(reflected, m, 3, -1))
                self.assertEqual(gate.endpoint(h, m, 3, 1) +
                                 gate.endpoint(reflected, m, 3, -1), 3 ** sum(w))
            for r in range(1, min(5, m) + 1):
                self.assertEqual(gate.Ecal(m, r, 3, 1), gate.Ecal(m, r, 3, -1))

    def test_saved_json_matches_current_gate_and_uses_lf(self):
        path = ROOT / 'tools/analogue_gate_verdict.json'
        self.assertNotIn(b'\r\n', path.read_bytes())
        self.assertEqual(json.loads(path.read_text(encoding='utf-8')), gate.run_gate())

    def test_independent_energy_enumeration_matches_default_grid(self):
        from fractions import Fraction
        from math import comb
        for p, b in gate.MAPS.values():
            for m in range(2, 12):
                endpoints = {k: [] for k in range(1, m + 1)}
                for h in range(1, 2 ** m, 2):
                    x, k = h, 0
                    for _ in range(m):
                        odd = x & 1
                        k += odd
                        x = (p * x + b) // 2 if odd else x // 2
                    endpoints[k].append(x)
                for r in range(1, min(5, m) + 1):
                    q, half = 2 ** r, 2 ** (r - 1)
                    value = Fraction(0)
                    for k, ends in endpoints.items():
                        signed = [0] * half
                        for e in ends:
                            z = e % q
                            signed[z % half] += 1 if z < half else -1
                        value += Fraction(half * sum(x * x for x in signed), comb(m - 1, k - 1))
                    self.assertEqual(value, gate.Ecal(m, r, p, b))

    def test_histogram_walks_each_start_only_once(self):
        with patch.object(gate, 'H_step', wraps=gate.H_step) as step:
            gate.source_histograms(3, 2, 3, 1)
        self.assertEqual(step.call_count, 3 * (1 << (3 - 1)))


if __name__ == '__main__':
    unittest.main()
