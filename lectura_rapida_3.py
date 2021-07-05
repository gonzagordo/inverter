#probando en python 3 
import os, sys, time, json

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

raw_data ={

    "main_volt":main_volt,
    "main_herz":main_herz,
    "out_volt":out_volt,
    "out_herz":out_herz,
    "W_power":W_power,
    "VA_power":VA_power,
    "load_percent":load_percent,
    "bus_voltage":bus_voltage,
    "bat_volt":bat_volt,
    "bat_in_current":bat_in_current,
    "cap_bat":cap_bat,
    "inverter_temp":inverter_temp,
    "pv_in_current":pv_in_current,
    "pv_in_volt":pv_in_volt,
    "bat_V_SCC":bat_V_SCC,
    "bat_out_current":bat_out_current
    
}




print("++++++++++++++++++++")

for valor in raw_data.items():
    print(valor)

