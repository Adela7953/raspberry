import serial

port = '/dev/ttyACM0'
brate = 9600
cmd = 'temp'

seri = serial.Serial(port, baudrate=9600,timeout = None)
print(seri.name)

seri.write(cmd.encode())


while 1:
	if seri.in_waiting !=0:
	    content = seri.readline()
	    print(content.decode())

