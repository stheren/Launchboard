import random

import launchpad_py as launchpad
from enum import Enum


class Color(Enum):
    BLACK = 0
    RED = 1
    GREEN = 2
    ORANGE = 3


def LedCtrlXY_Mini(lpt, x, y, c: Color):
    if c == Color.BLACK:
        lpt.LedCtrlXY(x, y, 0, 0)
    elif c == Color.RED:
        lpt.LedCtrlXY(x, y, 1, 0)
    elif c == Color.GREEN:
        lpt.LedCtrlXY(x, y, 0, 1)
    elif c == Color.ORANGE:
        lpt.LedCtrlXY(x, y, 1, 1)


lp = launchpad.Launchpad()
if lp.Open():
    print("Launchpad Mk1/S/Mini is now open ...")
    mode = "Mk1"
else:
    print("Did not find any Launchpads, meh...")
    exit(-1)

lp.ButtonFlush()
lp.LedAllOn(Color.GREEN)
LedCtrlXY_Mini(lp, 0, 0, Color.ORANGE)

while 1:
    # lp.LedCtrlRaw(random.randint(0, 127), random.randint(0, 3), random.randint(0, 3))
    but = lp.ButtonStateXY()
    if len(but) > 0:
        if but == [0, 0, True]:
            break
        else:
            if but[2]:
                LedCtrlXY_Mini(lp, but[0], but[1], Color.RED)
            else:
                LedCtrlXY_Mini(lp, but[0], but[1], Color.GREEN)
            # lp.LedCtrlXY(but[0], but[1], random.randint(0, 255), random.randint(0, 255))




lp.Reset()  # turn all LEDs off
lp.Close()  # close the Launchpad (will quit with an error due to a PyGame bug)
print("Launchpad Mk1/S/Mini is now close !")
