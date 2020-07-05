from ppadb.client import Client
import clipboard as c
import time
client=Client(host="127.0.0.1",port=5037)
print("------------Starting Server------------")
print("Connecting to client",end='')
for i in range(3):
    print('.',end='')
    time.sleep(1)
devices=client.devices()
device=devices[0]
print('Connected\n')
while(True):
        text=c.paste()
        text=text.split()
        text='%s'.join(text)
        device.shell('input keyevent 84')
        time.sleep(2)
        device.shell('input text '+text)
        print(text)
        device.shell('input keyevent 28')
        device.shell('input keyevent 66')
