import unittest
from roulette import Outcome, Bin, Wheel, BinBuilder


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
    

class WheelBuildTest(unittest.TestCase):
    
    def setUp(self):
        self.five = Outcome("00-0-1-2-3", 6)
        self.one = Outcome("1", 35)
        self.street_one_two_three = Outcome("1-2-3", 11)
        self.corner_one_two_four_five = Outcome("1-2-4-5", 8)
        self.line_one_to_six = Outcome("1-2-3-4-5-6", 5)
        self.bin_one = Bin([self.five, self.one, self.street_one_two_three, self.corner_one_two_four_five, self.line_one_to_six])
        self.bin_four = Bin([self.corner_one_two_four_five, self.line_one_to_six])
        self.wheel = Wheel()

    def test_wheel_returns_empty_bin(self):
        self.assertEqual(self.wheel.get(15), Bin() )

    def test_wheel_has_38_bins(self):
        self.assertEqual(len(self.wheel.bins), 38)

        
    def test_outcomes_can_be_added_to_empty_bins_in_wheel(self):
        self.wheel.addOutcome(1, self.one)
        self.assertEqual(self.wheel.get(1), Bin({Outcome("1", 35)}))

        
    def test_outcomes_can_be_added_to_non_empty_bins_in_wheel(self):
        self.wheel.addOutcome(1, self.street_one_two_three)
        self.wheel.addOutcome(1, self.one)
        self.assertEqual(self.wheel.get(1), Bin({Outcome("1", 35), Outcome("1-2-3", 11)}))

    


class WheelRandomTest(unittest.TestCase):

    def setUp(self):
        self.wheel = Wheel()

    # @unittest.skip("Cannot ensure randomness")
    def test_wheel_selects_random_bins(self):
        # seed is set to os.urandom(20)
        self.assertEqual(self.wheel.next(), self.wheel.get(3))
        self.assertEqual(self.wheel.next(), self.wheel.get(13))
        

class BinBuilderTest(unittest.TestCase):
    # TODO: setup
    # create wheel and call binbuilder on it

    def setUp(self):
        self.wheel = Wheel()
        self.bin_builder = BinBuilder()
        self.bin_builder.straightBets(self.wheel)

        
    def test_create_straight_bet_for_special_case_00(self):
        expected = {Outcome("00", 35) } # frozenset of outcomes
        self.assertEqual(self.wheel.get(37), expected)
        
if __name__ == '__main__':
    unittest.main()
