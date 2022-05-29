from train import *
from hand import *


class PlayerTrain(Train):
    """ this class represents the player train.  It is derived from the abstract Train class.
    It MUST implement the abstract method isPlayable. It has 2 new instance variables --
    the hand(player) to which it belongs and a flag that determines if the train is currently open """

    def __init__(self, hand, isOpen=False):
        super().__init__()
        self.__hand = hand
        self.__isOpen = isOpen

    @property
    def isOpen(self):
        return self.__isOpen == True

    def isPlayable(self, hand, domino):
        if hand == self.__hand:
            self._isPlayable(domino)
        if self.__isOpen:
            self._isPlayable(domino)
