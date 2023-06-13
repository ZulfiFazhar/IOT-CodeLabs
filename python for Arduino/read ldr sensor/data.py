from pyfirmata import util, Arduino
import csv
import time

board = Arduino('COM3')

it = util.Iterator(board)
it.start()

nilai_analog = board.get_pin('a:0:i')

# Open the CSV file for writing
file_name = 'data.csv'
csv_file = open(file_name, 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Timestamp', 'LDR Value'])

while True:
    try:
        nilai = nilai_analog.read()

        if nilai is not None:
            nilai *= 1000
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            print("Nilai LDR: ", nilai)

            csv_writer.writerow([timestamp, nilai])
        else:
            print("Gagal membaca nilai LDR")

    except KeyboardInterrupt:
        break

    time.sleep(2)

# Close the CSV file
csv_file.close()

board.exit()
