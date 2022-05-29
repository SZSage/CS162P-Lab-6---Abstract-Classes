from mexicanTrain import *
from playerTrain import *

# these global variables can be used for testing
mTrain1 = MexicanTrain()
mTrain2 = MexicanTrain()
h = Hand()
hOther = Hand()
pTrain = PlayerTrain(h, 12)
d12_1 = Domino(12, 1)
d1_12 = Domino(1, 12)
d3_4 = Domino(3, 4)
d1_6 = Domino(1, 6)


# this function resets each of the globals to a known state
def resetGlobals():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    mTrain1 = MexicanTrain()
    mTrain2 = MexicanTrain()
    h = Hand()
    hOther = Hand()
    pTrain = PlayerTrain(h, 12)
    d12_1 = Domino(12, 1)
    d1_12 = Domino(1, 12)
    d1_6 = Domino(1, 6)
    d3_4 = Domino(3, 4)


# just so you know how to use the globals and resetGlobal
def testMTConstructor():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()
    # the rest of your test will go here

    print(f"Testing count. Expect domino count for mTrain1 0: {mTrain1.count}")
    print(f"Testing isEmpty. Expect domino count for mTrain1 true: {mTrain1.isEmpty}")
    print(f"Testing playableValue. Expect engine value 12: {mTrain1.playableValue}")
    print(f"Testing lastDomino. Expect last domino none: {mTrain1.lastDomino}")


def testAdd():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()
    mTrain1.add(d12_1)
    print("\033[1mMexican train\033[0m")
    print(f"Count: {mTrain1.count}")
    print(f"isEmpty: {mTrain1.isEmpty}")
    print(f"PlayableValue: {mTrain1.playableValue} ")
    print(f"lastDomino: {mTrain1.lastDomino}\n")
    pTrain.add(d12_1)
    print(f"\033[1mPlayer train\033[0m")
    print(f"Count: {pTrain.count}")
    print(f"isEmpty: {pTrain.isEmpty}")
    print(f"PlayableValue: {pTrain.playableValue} ")
    print(f"lastDomino: {pTrain.lastDomino}")


def testPlayOnMexicanTrain():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()
    okToPlay, mustFlip = mTrain1.isPlayable(h, d1_12)
    print(f"okToPlay: {okToPlay}")
    print(f"mustFlip: {mustFlip}")
    okToPlay, mustFlip = mTrain1.isPlayable(h, d12_1)
    print(f"okToPlay: {okToPlay}")
    print(f"mustFlip: {mustFlip}")
    okToPlay, mustFlip = mTrain1.isPlayable(h, d3_4)
    print(f"okToPlay: {okToPlay}")
    print(f"mustFlip: {mustFlip}\n")

    print("\033[1mBefore play\033[0m")
    print(f"Last domino: {mTrain1.lastDomino}")
    print(f"Playable value: {mTrain1.playableValue}")
    print(f"Count: {mTrain1.count}\n")
    mTrain1.play(h, d1_12)
    print("\033[1mAfter play\033[0m")
    print(f"Last domino: {mTrain1.lastDomino}")
    print(f"Playable value: {mTrain1.playableValue}")
    print(f"Count: {mTrain1.count}\n")

    try:
        mTrain1.play(h, d3_4)
    except ValueError as rErr:
        print(f"Expect an exception since domino is not playable: {rErr}")
        print(f"Last domino: {mTrain1.lastDomino}")
        print(f"Playable value: {mTrain1.playableValue}")
        print(f"Count: {mTrain1.count}")


def testPlayOnPlayerTrain():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()
    okToPlay, mustFlip = pTrain.isPlayable(h, d1_12)
    print(f"okToPlay: {okToPlay}")
    print(f"mustFlip: {mustFlip}")
    okToPlay, mustFlip = pTrain.isPlayable(h, d12_1)
    print(f"okToPlay: {okToPlay}")
    print(f"mustFlip: {mustFlip}")
    okToPlay, mustFlip = pTrain.isPlayable(h, d3_4)
    print(f"okToPlay: {okToPlay}")
    print(f"mustFlip: {mustFlip}")
    okToPlay, mustFlip = pTrain.isPlayable(hOther, d1_12)
    print(f"okToPlay: {okToPlay}")
    print(f"mustFlip: {mustFlip}")
    pTrain.isOpen()
    okToPlay, mustFlip = pTrain.isPlayable(hOther, d1_12)
    print(f"okToPlay: {okToPlay}")
    print(f"mustFlip: {mustFlip}")
    print()
