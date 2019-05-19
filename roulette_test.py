import unittest
from roulette import Outcome


class OutcomeTest(unittest.TestCase):

    def setUp(self):
        self.o1 = Outcome("red", 1)
        self.o2 = Outcome("red", 3)
        self.o3 = Outcome("6", 35)

    def test_outcomes_with_same_name_are_equal(self):
        self.assertEqual(self.o1 == self.o2, True)


    def test_outcomes_with_same_name_have_same_hash_code(self):
        self.assertEqual(hash(self.o1) == hash(self.o2), True)

    def test_outcomes_with_different_names_dont_have_same_hash_code(self):
        self.assertEqual(hash(self.o1) != hash(self.o2), False)


    def test_outcome_pays_correct_win_amount(self):
        self.assertEqual(self.o3.winAmount(10), 350)


if __name__ == '__main__':
    unittest.main()
