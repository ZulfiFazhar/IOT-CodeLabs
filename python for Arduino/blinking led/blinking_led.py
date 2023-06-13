import pyfirmata
import time


board = pyfirmata.Arduino('COM3')
led_builtin = board.digital[13] # inisialisasi led_builtin Arduino yang berada di pin 13 digital

while True:
    try:
        led_builtin.write(1)       # 1 = HIGH
        time.sleep(1)              # delay 1 second
        led_builtin.write(0)       # 0 = LOW
        time.sleep(1)              # delay 1 second
    except KeyboardInterrupt:
        break

board.exit() # tekan Ctrl + C untuk exit