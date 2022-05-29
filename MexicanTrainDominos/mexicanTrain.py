from train import *


# test mexicanTrain
class MexicanTrain(Train):
    """ this class represents the mexican train.  It is derived from the abstract Train class.
    It MUST implement the abstract method isPlayable. """

    # isPlayable is not the same as isPlayable in playerTrain, dependent on what kind of train it is
    def __init__(self):
        super().__init__()

    def isPlayable(self, hand, domino):
        return self._isPlayable(domino)
