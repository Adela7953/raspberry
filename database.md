# database
```
import time
import requests, json
from influxdb import InfluxDBClient as influxdb
import serial

port = '/dev/ttyACM0'
brate = 9600
cmd = 'temp'

seri = serial.Serial(port, baudrate=9600,timeout = None)
print(seri.name)

seri.write(cmd.encode())

try:
    while True:

        if seri.in_waiting !=0:
            content = seri.readline()
            temp = int(content.decode())

            data = [{
                'measurement' : 'pir',
                'tags':{
                    'office': 'hgcom',
                 },
                'fields':{
                    'value': temp
                 }
            }]
        else:
             print("Read error")
        client = None
        try:
            client = influxdb('localhost',8086,'root','root','pir')
        except Exception as e:
            print("Exception" + str(e))
        if client is not None:
            try:
                client.write_points(data)
            except Exception as e:
                print("Exception wrtie" + str(e))
            finally:
                client.close()
        time.sleep(1)
except KeyboardInterrupt:
    print("Terminated by Keyboard")

finally:
    print("End of Program")

```

