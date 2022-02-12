import serial
import pyqrcode

ERROR = 'M'
QUIET_ZONE = 4
PORT = '/dev/serial0'
BAUD = 115200
CLEAR_LINES = 50

def clear_lines():
  print('\n' * CLEAR_LINES)

clear_lines()
done = False

with serial.Serial(PORT, BAUD, timeout=0.9) as ser:
  while not done:
    line = ser.readline()
    if line != b'':
      line = line[:-1]
      if line == b'quit':
        done = True
      elif line == b'clear':
        clear_lines()
      else:
        qr = pyqrcode.create(line, error=ERROR)
        print(qr.terminal(quiet_zone=QUIET_ZONE))
