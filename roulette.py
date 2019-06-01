from random import Random
from os import urandom

class Outcome:

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    
    def winAmount(self, amount):
        return self.odds * amount

    def __eq__(self, other):
        return self.name == other.name


    def __ne__(self, other):
        return self.name != other.name


    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f"{self.name} ({self.odds}:1)"

    def __repr__(self):
        return "{class_:s}({name!r}, {odds!r})".format(class_=type(self).__name__, **vars(self) )



class Bin(frozenset):
    """
    Bin contains a collection of Outcomes which reflect the winning bets 
    that are paid for a particular bin on a Roulette wheel. 
    In Roulette, each spin of the wheel has a number of Outcomes. 
    Example: A spin of 1, selects the “1” bin with the following winning 
    Outcomes: “1” , “Red” , “Odd” , “Low” , “Column 1” , “Dozen 1-12” , 
    “Split 1-2” , “Split 1-4” , “Street 1-2-3” , “Corner 1-2-4-5” , “Five Bet” , 
    “Line 1-2-3-4-5-6” , “00-0-1-2-3” , “Dozen 1” , “Low” and “Column 1” . 
    These are collected into a single Bin .
    """
        

class Wheel:
    """
    Wheel contains the 38 individual bins on a Roulette wheel, plus a random number generator. 
    It can select a Bin at random, simulating a spin of the Roulette wheel.
    """
    def __init__(self):
        self.bins = [Bin() for _ in range(38)]
        self.rng = Random()


    def addOutcome(self, number, outcome):
        """
        Adds the given Outcome to the Bin with the given number.
        """
        self.bins[number] |= Bin([outcome])


    def next(self):
        """
        Generate a random number between 0-37 and return the coressponding bin
        """
        self.rng.seed(urandom(20))
        return self.rng.choice(self.bins)


    def get(self, bin):
        """
        Returns the given Bin from the internal collection.

        Parameters:	bin (int) – bin number, in the range zero to 37 inclusive.
        Returns:	The requested Bin.
        Return type:	Bin
        """
        return self.bins[bin]




class BinBuilder:
    """
    BinBuilder creates the Outcomes for all of the 38 individual Bin on a Roulette wheel.
    """

    def __init__(self):
        print("building bins....")


    def buildBins(self, wheel):
        self.straightBets(wheel)
        self.splitBets(wheel)
        self.streetBets(wheel)
        self.cornerBets(wheel)
        self.lineBets(wheel)
        


    def straightBets(self, wheel):
        odds = 35
        for n in range(0, 37):
            o = Outcome(str(n), odds)
            wheel.addOutcome(n, o)

        o = Outcome("00", odds)
        wheel.addOutcome(37, o)


    def splitBets(self, wheel):
        prefix = "split"
        odds = 17
        # create left-right split bets for column 1 and 2
        for r in range(0, 12): 
            first_column_number = (3 * r) + 1
            outcome_name = prefix + " " + str(first_column_number) + "-" + str(first_column_number+1) # split 1-2
            outcome = Outcome(outcome_name, odds)
            wheel.addOutcome(first_column_number, outcome)
            wheel.addOutcome(first_column_number + 1, outcome)


        # create left-right split bets for column 2 and 3
        for r in range(0, 12):
            first_column_number = (3 * r) + 2
            outcome_name = prefix + " " + str(first_column_number) + "-" + str(first_column_number+1) # split 2-3
            outcome = Outcome(outcome_name, odds)
            wheel.addOutcome(first_column_number, outcome)
            wheel.addOutcome(first_column_number + 1, outcome)

        # create up-down split bets for column 1
        for r in range(0, 11):
            bin_number = (3 * r) + 1
            outcome_name = prefix + " " + str(bin_number) + "-" + str(bin_number + 3)
            outcome = Outcome(outcome_name, odds)
            wheel.addOutcome(bin_number, outcome)
            wheel.addOutcome(bin_number + 3, outcome)


        # create up-down split bets for column 2
        for r in range(0, 11):
            bin_number = (3 * r) + 2
            outcome_name = prefix + " " + str(bin_number) + "-" + str(bin_number + 3)
            outcome = Outcome(outcome_name, odds)
            wheel.addOutcome(bin_number, outcome)
            wheel.addOutcome(bin_number + 3, outcome)


        # create up-down split bets for column 3
        for r in range(0, 11):
            bin_number = (3 * r) + 3
            outcome_name = prefix + " " + str(bin_number) + "-" + str(bin_number + 3)
            outcome = Outcome(outcome_name, odds)
            wheel.addOutcome(bin_number, outcome)
            wheel.addOutcome(bin_number + 3, outcome)

            

    def streetBets(self, wheel):
        odds = 11
        prefix = "street"

        for r in range(0, 12):
            bin_number = (3 * r) + 1
            outcome_name = prefix + " " + str(bin_number) + "-" + str(bin_number + 1) + "-" + str(bin_number + 2)
            outcome = Outcome(outcome_name, odds)
            wheel.addOutcome(bin_number, outcome)
            wheel.addOutcome(bin_number + 1, outcome)
            wheel.addOutcome(bin_number + 2, outcome)


    def cornerBets(self, wheel):
        odds = 8
        prefix = "corner"

        for r in range(0, 11):
            # column 1-2 corner
            first_bin = (3 * r) + 1
            c1_outcome_name = prefix + " " + str(first_bin) + "-" + str(first_bin + 1) + "-" + str(first_bin + 3) + "-" + str(first_bin + 4)
            corner_one = Outcome(c1_outcome_name, odds)
            wheel.addOutcome(first_bin, corner_one)
            wheel.addOutcome(first_bin + 1, corner_one)
            wheel.addOutcome(first_bin + 3, corner_one)
            wheel.addOutcome(first_bin + 4, corner_one)

            #column 2-3 corner
            second_bin = (3 * r) + 2
            c2_outcome_name = prefix + " " + str(second_bin) + "-" + str(second_bin + 1) + "-" + str(second_bin + 3) + "-" + str(second_bin + 4)
            corner_two = Outcome(c2_outcome_name, odds)
            wheel.addOutcome(second_bin, corner_one)
            wheel.addOutcome(second_bin + 1, corner_one)
            wheel.addOutcome(second_bin + 3, corner_one)
            wheel.addOutcome(second_bin + 4, corner_one)


    def lineBets(self, wheel):
        odds = 5
        prefix = "line"
        
        for r in range(0, 11):
            outcome_name = prefix + " " + str(3 * r+1) + "-" + str(3 * r + 6)
            outcome = Outcome(outcome_name, odds)
            wheel.addOutcome(3 * r + 1, outcome)
            wheel.addOutcome(3 * r + 2, outcome)
            wheel.addOutcome(3 * r + 3, outcome)
            wheel.addOutcome(3 * r + 4, outcome)
            wheel.addOutcome(3 * r + 5, outcome)
            wheel.addOutcome(3 * r + 6, outcome)


    def dozenBets(self, wheel):
        pass

    def columnBets(self, wheel):
        pass


    def redBlackBets(self, wheel):
        pass

    def oddEvenBets(self, wheel):
        pass

    def highLowBets(self, wheel):
        pass

    
