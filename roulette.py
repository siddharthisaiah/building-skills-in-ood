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




        
