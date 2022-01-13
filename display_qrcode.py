import serial
import pyqrcode

ERROR = 'M'
QUIET_ZONE = 1
PORT = '/dev/serial0'
BAUD = 115200
CLEAR_LINES = 40


done = False

with serial.Serial(PORT, BAUD, timeout=1) as ser:
  while not done:
    line = ser.readline()
    if line != b'':
      line = line[:-1]
      if line == b'quit':
        done = True
      elif line == b'clear':
        print('\n' * CLEAR_LINES)
      else:
        qr = pyqrcode.create(line, error=ERROR)
        print(qr.terminal(quiet_zone=QUIET_ZONE))
