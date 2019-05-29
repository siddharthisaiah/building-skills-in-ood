import unittest
from roulette import Outcome, Bin


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


class BinTest(unittest.TestCase):

    def setUp(self):
        self.five = Outcome("00-0-1-2-3", 6)
        self.three_five = Outcome("3-5", 17)
        self.one_twelve = Outcome("1-12", 2)
        self.low = Outcome("low-1-18", 1)
        self.high = Outcome("high-19-36", 1)
        self.street_thirty_one_two_three = Outcome("31-32-33", 11)
        

    def test_bins_can_be_created_from_outcomes(self):
        self.assertEqual(Bin([self.five, self.three_five, self.one_twelve]), Bin({Outcome("00-0-1-2-3", 6), Outcome("3-5", 17), Outcome("1-12", 2)}) )
        self.assertEqual(Bin([Outcome("0",35), self.five]), Bin({Outcome("0",35), Outcome("00-0-1-2-3", 6)}))
        self.assertEqual(Bin([Outcome("00",35), self.five]), Bin({Outcome("00",35), Outcome("00-0-1-2-3", 6)}))
    

if __name__ == '__main__':
    unittest.main()
