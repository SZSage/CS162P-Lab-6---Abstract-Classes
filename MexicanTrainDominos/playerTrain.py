from train import *
from hand import *


class PlayerTrain(Train):
    """ this class represents the player train.  It is derived from the abstract Train class.
    It MUST implement the abstract method isPlayable. It has 2 new instance variables --
    the hand(player) to which it belongs and a flag that determines if the train is currently open """

    def __init__(self, hand, isOpen=False, engineValue=12):
        super().__init__()
        self.__hand = hand
        self.__isOpen = isOpen
        self._engineValue = engineValue

    @property
    def isOpen(self):
        return self.__isOpen

    def isPlayable(self, hand, domino):
        if hand == self.__hand or self.__isOpen:
            return self._isPlayable(domino)

    def open(self):
        return self.__isOpen == True

    def close(self):
        return self.__isOpen == False
