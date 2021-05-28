#funciona solo con sudo en python 2 
import os, sys, time
leido ="(230.0 21.7 230.0 50.0 21.7 5000 4000 48.0 46.0 42.0 56.4 54.0 2 30 060 0 2 0 9 01 0 0 54.0"
#print leido
valores=leido.split() 
#print valores
main_volt =valores[0][1:]
main_herz=valores[1]
out_volt=valores[2]
out_herz=valores[3]
W_power=str(float(valores[4]))
VA_power=str(float(valores[5]))
load_percent=str(float(valores[6]))
bus_voltage=valores[7]
bat_volt=valores[8]
bat_in_current=str(float(valores[9]))
cap_bat = float (valores[10])
inverter_temp=str(float(valores[11]))
pv_in_current=str(float(valores[12]))
pv_in_volt=valores[13]
bat_V_SCC=valores[14]
bat_out_current=str(float(valores[15]))


cap_bat = str(cap_bat)
print "BAT "+cap_bat+"%"
print "BAT "+bat_volt+"V"
print ">>BAT "+bat_in_current+"A"
print "<<"+main_volt+"V"
print "<<"+main_herz+"Hz"
print ">>"+out_volt+"V"
print ">>"+out_herz+"Hz"
print ">>"+W_power+"W"
print ">>"+VA_power+"VA"
print "bus volt "+bus_voltage+"V"
print "inverter temp "+inverter_temp+"C"
print ">> panel "+pv_in_current+"A"
print ">> panel "+pv_in_volt+"V"
print "bat_Volt_SCC "+bat_V_SCC+"V"
print ">> BAT "+bat_out_current+"A"

