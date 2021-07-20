from time import sleep
import mouse
import win32api
import keyboard

class Clickers:
    def auto(self):
        print('r')
        mouse.click('right')
        sleep(0.01)



#86 (0.01)
#10 (0.1)
#19 (0.05)
#32 (0.03)
#47 (0.02)
#59 (0.015)

c = Clickers()

while True:
    while win32api.GetAsyncKeyState(0x05):
        c.auto()

