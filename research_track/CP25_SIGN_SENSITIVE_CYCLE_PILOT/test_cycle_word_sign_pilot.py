import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from cycle_word_sign_pilot import (
    candidate_from_word,
    enumerate_map,
    follows_word_and_returns,
    run_suite,
)


class CycleCandidateTests(unittest.TestCase):
    def test_known_cycles_are_recovered_exactly(self):
        self.assertEqual(candidate_from_word(3, 1, (1, 0)).x, 1)
        self.assertEqual(candidate_from_word(3, -1, (1,)).x, 1)
        self.assertEqual(candidate_from_word(3, -1, (1, 1, 0)).x, 5)
        self.assertEqual(candidate_from_word(5, 1, (1, 1, 0, 0, 0)).x, 1)

    def test_every_integral_candidate_through_length_ten_realizes_its_word(self):
        for p, b in ((3, 1), (3, -1), (5, 1)):
            for m in range(1, 11):
                for tail in range(1 << (m - 1)):
                    word = (1,) + tuple((tail >> j) & 1 for j in range(m - 1))
                    candidate = candidate_from_word(p, b, word)
                    if candidate.x is not None:
                        self.assertTrue(follows_word_and_returns(candidate))

    def test_length_eighteen_scan_matches_the_frozen_counts(self):
        expected = {
            (3, 1): (46, 9, ((1, 2),)),
            (3, -1): (
                46,
                37,
                ((1,), (5, 7, 10), (17, 25, 37, 55, 82, 41, 61, 91, 136, 68, 34)),
            ),
            (5, 1): (
                27,
                18,
                ((1, 3, 8, 4, 2), (13, 33, 83, 208, 104, 52, 26), (17, 43, 108, 54, 27, 68, 34)),
            ),
        }
        for key, frozen in expected.items():
            result = enumerate_map(*key, max_m=18)
            self.assertEqual((result["divisible"], result["positive_integer"], result["cycles"]), frozen)

    def test_suite_labels_all_three_analogue_maps(self):
        result = run_suite(max_m=3)
        self.assertEqual(tuple(result), ("3n+1", "3n-1", "5n+1"))
        self.assertTrue(all(row["words"] == 7 for row in result.values()))

    def test_inexact_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            candidate_from_word(True, 1, (1,))
        with self.assertRaises(ValueError):
            candidate_from_word(3, True, (1,))
        with self.assertRaises(ValueError):
            candidate_from_word(3, 1, (1.0,))
        with self.assertRaises(ValueError):
            enumerate_map(3, 1, True)
        with self.assertRaises(ValueError):
            enumerate_map(3, 1, 3.0)


if __name__ == "__main__":
    unittest.main()
