import serial
import pyqrcode

ERROR = 'M'
QUIET_ZONE = 1
PORT = '/dev/serial0'
BAUD = 115200
CLEAR_LINES = 50
NEW_LINE = '\n'

def clear_lines():
  print('\n' * CLEAR_LINES)

clear_lines()
done = False

with serial.Serial(PORT, BAUD, timeout=0.9) as ser:
  line = ''
  while not done:
    line = line + ser.readline().decode(errors='ignore')
    if line != '' and line.endswith(NEW_LINE):
      line = line[:-1]
      if line == 'quit':
        done = True
      elif line == 'clear':
        clear_lines()
      else:
        qr = pyqrcode.create(line, error=ERROR)
        print(qr.terminal(quiet_zone=QUIET_ZONE))
      line = ''
