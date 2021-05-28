# -*- coding: utf-8 -*-
path = '/dev/hidraw0'
path2 = '/home/pi/basurilla.txt'
inverter = open (path,"r+")
ack = inverter.write("QPIGS\xB7\xA9\r")
print(ack)
