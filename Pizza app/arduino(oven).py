import time
from fhict_cb_01.CustomPymata4 import CustomPymata4
import time

board = CustomPymata4("COM5")

LEFT_BUTTON = 9
RIGHT_BUTTON = 8
RED_LED = 4
GREEN_LED = 5

BUTTON_PRESSED = 0

cooking = False

def LeftButtonChanged(data):
    global cooking
    if data[2] == 1 and cooking == False:
        cooking = True


def RightButtonChanged(data):
    global cooking
    if data[2] == 1 and cooking == True:
        cooking = False


board.set_pin_mode_digital_input_pullup(RIGHT_BUTTON, callback = RightButtonChanged)
board.set_pin_mode_digital_input_pullup(LEFT_BUTTON, callback = LeftButtonChanged)


while True:
    if cooking:
        board.digital_write(RED_LED, 1)
        board.digital_write(GREEN_LED, 0)
    else:
        board.digital_write(RED_LED, 0)
        board.digital_write(GREEN_LED, 1)
    time.sleep(0.2)