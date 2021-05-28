#funciona solo con sudo en python 2 y probando en 3 
import os, sys, time

path = '/dev/hidraw0'
comando  = b"QPIGS\xB7\xA9\r"

inverter = open (path,"rb+")

ack = inverter.write(comando)

#print(ack)
time.sleep(0.5) 
#primera lectura
leido = inverter.read(8)
#bucle de lectura hasta encontrar retorno de carro 
while leido.find(b'\r') == -1 :   
    leido = leido + inverter.read(8)
       
#print (leido)
valores=leido.split() 
#print (valores)

#procesado de valores
main_volt =str(float(valores[0][1:]))
main_herz=str(float(valores[1]))
out_volt=str(float(valores[2]))
out_herz=str(float(valores[3]))
W_power=str(float(valores[4]))
VA_power=str(float(valores[5]))
load_percent=str(float(valores[6]))
bus_voltage=str(float(valores[7]))
bat_volt=str(float(valores[8]))
bat_in_current=str(float(valores[9]))
cap_bat =str(float (valores[10]))
inverter_temp=str(float(valores[11]))
pv_in_current=str(float(valores[12]))
pv_in_volt=str(float(valores[13]))
bat_V_SCC=str(float(valores[14]))
bat_out_current=str(float(valores[15]))


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
