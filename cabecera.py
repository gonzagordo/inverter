#funciona solo con sudo en python 2 y probando en 3 
import os, sys, time
version=sys.version
version = version [0]
comando = "QPIGS\xB7\xA9\r"
if version == '3':
    comando  = str.encode("QPIGS\xB7\xA9\r""QPIGS\xB7\xA9\r")
fd = os.open('/dev/hidraw0', os.O_RDWR | os.O_NONBLOCK)
os.write(fd, comando) 
time.sleep(0.5) 
#leido = os.read (fd,8)
#print (leido)
