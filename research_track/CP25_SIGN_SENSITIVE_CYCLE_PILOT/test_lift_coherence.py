import sys
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from lift_coherence import (
    B_value,
    h_residue,
    is_primitive,
    lift_profile,
    product_barrier_profile,
    scan_all_words,
    scan_lift,
    scan_product_barrier,
)


class LiftCoherenceTests(unittest.TestCase):
    def test_trivial_3n_plus_cycle_dominates_on_every_rotation(self):
        profile = lift_profile(3, (1, 0))
        self.assertEqual(profile["b"], 1)
        self.assertEqual(profile["A"], 1)
        self.assertEqual(tuple(row["q"] for row in profile["rotations"]), (Fraction(1), Fraction(2)))
        self.assertTrue(profile["all_dominate"])
        self.assertTrue(profile["integral"])

    def test_known_3n_minus_cycles_dominate(self):
        self.assertTrue(lift_profile(3, (1,))["all_dominate"])
        self.assertTrue(lift_profile(3, (1, 1, 0))["all_dominate"])

    def test_simple_nonintegral_word_fails_dominance(self):
        profile = lift_profile(3, (1, 0, 0))
        self.assertFalse(profile["integral"])
        self.assertFalse(profile["all_dominate"])
        self.assertEqual(profile["rotations"][0]["t"], -3)

    def test_exact_carry_recurrence_holds_on_every_rotation(self):
        profile = lift_profile(3, (1, 1, 0))
        rows = profile["rotations"]
        for i, row in enumerate(rows):
            next_row = rows[(i + 1) % len(rows)]
            epsilon = row["word"][0]
            self.assertEqual(
                2 * next_row["t"],
                (3**epsilon) * row["t"] + profile["A"] * row["carry"],
            )
            self.assertEqual(row["dominates"], row["t"] >= 0)

    def test_residue_and_primitivity_helpers(self):
        self.assertEqual(B_value(3, (1, 1, 0)), 5)
        self.assertEqual(h_residue(3, 1, (1, 0)), 1)
        self.assertTrue(is_primitive((1, 1, 0)))
        self.assertFalse(is_primitive((1, 0, 1, 0)))

    def test_inexact_inputs_are_rejected(self):
        for bad_p in (True, 3.0, "3"):
            with self.assertRaises(ValueError):
                B_value(bad_p, (1,))
        for bad_word in ((True,), (1.0,), ("1",)):
            with self.assertRaises(ValueError):
                B_value(3, bad_word)
        for bad_b in (True, 1.0, "1"):
            with self.assertRaises(ValueError):
                h_residue(3, bad_b, (1,))
        for bad_max_m in (True, 2.0, "2"):
            with self.assertRaises(ValueError):
                scan_lift(3, bad_max_m)

    def test_small_scan_counts_raw_words_and_necklaces_separately(self):
        result = scan_lift(3, max_m=3)
        self.assertEqual(result["primitive_raw_starting_one"], 5)
        self.assertEqual(result["primitive_necklaces"], 4)
        self.assertEqual(result["dominance_survivors"], 3)
        self.assertEqual(result["nonintegral_survivors"], 0)
        self.assertEqual(result["by_sign"]["+1"]["necklaces"], 2)
        self.assertEqual(result["by_sign"]["+1"]["all_q_at_least_one"], 1)
        self.assertEqual(result["by_sign"]["-1"]["necklaces"], 2)
        self.assertEqual(result["by_sign"]["-1"]["all_q_at_least_one"], 2)

    def test_all_word_scan_keeps_repeated_words_visible(self):
        result = scan_all_words(3, max_m=3)
        self.assertEqual(result["words"], 7)
        self.assertEqual(result["premise_rows"], 6)
        self.assertEqual(result["integral_premise_rows"], 6)
        self.assertEqual(result["nonintegral_premise_rows"], 0)
        self.assertEqual([row["premise_rows"] for row in result["by_m"]], [1, 2, 3])

    def test_product_barrier_examples_and_small_scan(self):
        plus = product_barrier_profile(3, (1, 0, 0, 1))
        minus = product_barrier_profile(3, (1, 0, 1, 1))
        self.assertEqual(plus["b"], 1)
        self.assertTrue(plus["barrier_holds"])
        self.assertEqual(minus["b"], -1)
        self.assertTrue(minus["barrier_holds"])
        profile = lift_profile(3, (1, 0, 1, 1))
        cycle_product = Fraction(1)
        for row in profile["rotations"]:
            if row["word"][0]:
                cycle_product *= Fraction(3) + Fraction(profile["b"], row["q"])
        self.assertEqual(cycle_product, 1 << profile["m"])
        result = scan_product_barrier(3, max_m=4)
        self.assertEqual(result["counterexamples"], [])
        self.assertGreater(result["nonintegral_necklaces"], 0)


if __name__ == "__main__":
    unittest.main()
