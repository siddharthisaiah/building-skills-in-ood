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
