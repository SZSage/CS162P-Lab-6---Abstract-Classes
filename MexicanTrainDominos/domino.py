class Domino:
    """ This class representa a domino.  
        A card has 2 attributes, side1 and side2.  Both sides can have an integer value between 0 and 12.
        It uses private attributes and property getters and setters.
        Setters have appropriate validation that raise an exception when invalid data is used."""

    # region constructor
    def __init__(self, side1, side2):
        self.__side1 = side1
        self.__side2 = side2
    # endregion

    # region property getters and setters
    @property
    def side1(self):
        return self.__side1

    @property
    def side2(self):
        return self.__side2

    @side1.setter
    def side1(self, side1):
        if isinstance(side1, int) and 0 <= side1 <= 12:
            self.__side1 = side1
        else:
            raise ValueError(f"Side1 must an integer between 0 and 12 {type(side1)}  {side1}")

    @side2.setter
    def side2(self, side2):
        if isinstance(side2, int) and 0 <= side2 <= 12:
            self.__side2 = side2
        else:
            raise ValueError(f"Side2 must an integer between 0 and 12 {type(side2)}  {side2}")

    # because this property has no setter it is a "read only" property
    @property
    def score(self):
        return self.__side1 + self.__side2

    # endregion

    #region other methods
    def isDouble(self):
        return self.__side1 == self.__side2

    def flip(self):
        self.__side1, self.__side2 = self.__side2, self.__side1
    # endregion

    # region "magic" methods
    def __str__(self):
        return f'Domino({self.__side1} | {self.__side2})'

    def __eq__(self, other):
        """ This "magic method" is called when you check the equality of 2 dominos.  if domino1 == domino2 for example.
        2 dominos are equal if they're both dominos and if their attributes have the same values"""
        if isinstance(other, Domino):
            return (self.__side1 == other.side1 and self.__side2 == other.side2) or (self.__side1 == other.side2 and self.__side2 == other.side1)
        else:
            return False
    # endregion