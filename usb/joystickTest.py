import struct
import time


jstick = open('/dev/input/js0', 'rb')

try:
    while True:
	data = jstick.read(8)
	a,b,c,d = struct.unpack('Ih2B', data)
	print time.ctime(), a,b,c,d
	time.sleep(1)
finally:
	jstick.close()
