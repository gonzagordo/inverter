# -*- coding: utf-8 -*-
path = '/dev/hidraw0'
path2 = '/home/pi/basurilla.txt'
inverter = open (path,"rb+")
ack = inverter.write(b"QPIGS\xB7\xA9\r")
print(ack)
