import pyfirmata
import time


board = pyfirmata.Arduino('COM3')

while True:
    board.digital[13].write(1) # 1 = HIGH
    time.sleep(1)              # delay 1 second
    board.digital[13].write(0) # 0 = LOW
    time.sleep(1)              # delay 1 second
    