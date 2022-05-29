from abc import ABC, abstractmethod
from domino import *
from hand import *


class Train(ABC):
    """ This class represents a train of dominos. It is and abstract base class for other train classes
        It contains one abstract method, isPlayable """

    def __init__(self, engineValue=12):
        """ Should create the empty list _dominos and initialize the _engineValue attribute """
        self._dominos = []
        self._engineValue = engineValue

    @property
    def count(self):
        """ gets count of dominos in train """
        return len(self._dominos)

    @property
    def engineValue(self):
        """gets engine value for train"""
        return self._engineValue

    @property
    def lastDomino(self):
        """ returns the last domino in the train or None when the train is empty """
        if self.isEmpty:
            return None
        else:
            return self._dominos[-1]
        pass

    @property
    def playableValue(self):
        """ returns side 2 of the last domino or the engine value """
        if self.isEmpty:
            return self.engineValue
        else:
            return self.lastDomino.side2
        pass

    @property
    def isEmpty(self):
        """checks if train is empty"""
        return self.count == 0

    def add(self, item):
        if isinstance(item, Domino):
            self._dominos.append(item)
        else:
            raise TypeError(f"Item must be a valid domino object {type(item)} {item}")

    # engineValue getter and/or setter
    # is empty getter
    # lastDomino is getter
    # add method adds domino to train

    @abstractmethod
    def isPlayable(self, hand, domino):
        """ This abstract method takes a hand and a domino as its parameters and
        returns a tuple (isTheDominoPlayableByTheHand, mustTheDominoBeFlipped)
        DO NOT CHANGE THIS IMPLEMENTATION """
        pass

    def _isPlayable(self, domino):  # can't call in main
        """ this protected method contains the logic for determining if a domino is playable on the train """
        if isinstance(domino, Domino):
            mustFlip = False
            okToPlay = False
            if self.playableValue == domino.side1:
                mustFlip = False
                okToPlay = True
            elif self.playableValue == domino.side2:
                mustFlip = True
                okToPlay = True
            else:
                pass
            return okToPlay, mustFlip
        else:
            raise TypeError(f"domino must be a valid domino object {type(domino)}  {domino}")

    def play(self, hand, domino):
        """ this method plays a domino from a hand on the train.
        Notice that it calls the abstract method isPlayable even though it is not yet implemented. """
        if isinstance(hand, Hand) and isinstance(domino, Domino):
            okToPlay, mustFlip = self.isPlayable(hand, domino)
            if okToPlay:
                if mustFlip:
                    domino.flip()
                self.add(domino)
            else:
                raise ValueError(f"Domino {domino} does not match last domino in the train and can not be played")
        else:
            raise TypeError(
                f"hand and domino must be a valid hand and domino objects respectively {type(hand)}  {type(domino)}")

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._dominos[item]
        else:
            raise TypeError(f"Index must be an int {type(item)} {item}")

    def __str__(self):
        """Creates a string representation of train"""
        output = f"Train["
        for c in self._dominos:
            output += f"{c} "
        output += "]\n"
        return output
