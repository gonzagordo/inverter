#funciona solo con sudo en python 2 
import os, sys, time
path ='/dev/hidraw0'
path2='/home/pi/posix.txt'

fd = os.open(path2, os.O_RDWR | os.O_NONBLOCK)
os.write(fd, "QPIGS\xB7\xA9\r") 
time.sleep(0.5)
os.lseek(fd,0,0) 
leido = os.read (fd,8)

while leido.find('\r') == -1 :   
    leido = leido + os.read(fd, 8)
fd.close()
#print leido
valores=leido.split() 

print (valores)

"""
main_volt =valores[0][1:]
main_herz=valores[1]
out_volt=valores[2]
out_herz=valores[3]
W_power=str(int(valores[4]))
VA_power=str(int(valores[5]))
load_percent=str(int(valores[6]))
bus_voltage=valores[7]
bat_volt=valores[8]
bat_in_current=str(int(valores[9]))
cap_bat = int (valores[10])
inverter_temp=str(int(valores[11]))
pv_in_current=str(float(valores[12]))
pv_in_volt=valores[13]
bat_V_SCC=valores[14]
bat_out_current=str(int(valores[15]))


cap_bat = str(cap_bat)
print ("BAT "+cap_bat+"%")
print ("BAT "+bat_volt+"V")
print (">>BAT "+bat_in_current+"A")
print ("<<"+main_volt+"V")
print ("<<"+main_herz+"Hz")
print (">>"+out_volt+"V")
print (">>"+out_herz+"Hz")
print (">>"+W_power+"W")
print (">>"+VA_power+"VA")
print ("bus volt "+bus_voltage+"V")
print ("inverter temp "+inverter_temp+"C")
print (">> panel "+pv_in_current+"A")
print (">> panel "+pv_in_volt+"V")
print ("bat_Volt_SCC "+bat_V_SCC+"V")
print (">> BAT "+bat_out_current+"A")
"""
