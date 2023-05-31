from pyfirmata import util, Arduino
import time

board = Arduino('COM3')

it = util.Iterator(board)
it.start()

nilai_analog = board.get_pin('a:0:i')

while True:
    try:
        nilai = nilai_analog.read()

        if nilai is not None:
            nilai *= 1000
            print("Nilai LDR: ", nilai)
        else:
            print("Gagal membaca nilai LDR")

    except KeyboardInterrupt:
        break

    time.sleep(2)

board.exit()
