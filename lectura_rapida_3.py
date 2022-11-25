#probando en python 3 
import os, sys, datetime, time, json

import sqlite3


print("funcionando en remoto")




def convert (valor):
     a= str(round(float(valor),2))
     return a


# conectar con bases de datos
con = sqlite3.connect("/home/pi/pruebas_django/tiendaonline/db.sqlite3")
cursor = con.cursor()


while True:

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

    fecha=str(datetime.datetime.now())

    #fecha actual para grafica
    now = datetime.datetime.now()
    fecha_base = now.strftime("20%y-%m-%d %H:%M:%S")

    
    #procesado de valores
    
    # datos directos 
    main_volt =convert(valores[0][1:])
    main_herz=convert(valores[1])
    out_volt=convert(valores[2])
    out_herz=convert(valores[3])
    W_power=convert(valores[4])
    VA_power=convert(valores[5])
    load_percent=convert(valores[6])
    bus_voltage=convert(valores[7])
    bat_volt=convert(valores[8])
    bat_in_current=convert(valores[9])
    cap_bat =convert(valores[10])
    inverter_temp=convert(valores[11])
    pv_in_current=convert(valores[12])
    pv_in_volt=convert(valores[13])
    bat_V_SCC=convert(valores[14])
    bat_out_current=convert(valores[15])

    #datos procesados 
    potencia_solar= str (float(pv_in_current)*float(pv_in_volt)) 


    #valores para grafica 
    #x es la fecha_base
    capacidad_actual =float(cap_bat)
    in_power = 0
    sun_power = float(potencia_solar)
    out_power = float(W_power)
    generator = float (main_volt)
    bat_transfer =0
    bat_output =0
    pin =0
    pan=0
    pun=0
    fuera=0

    
    raw_data ={
        "ultima_lectureta":fecha,
        "potencia_solar" :potencia_solar,
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

    #volcado de valores a json para web
    with open('/home/pi/inverter/data.json', 'w') as f:
        json.dump(raw_data, f, ensure_ascii=False, indent=4)

    #volcado de valores a base de datos para grafica
    cursor.execute("insert into gestionpedidos_tiempo(x,y) values('{}',{}) ".format(fecha_base,capacidad_actual))

    #volcado de base de datos para historico 

    destino ="x,y,in_power,sun_power,out_power,generador,bat_transfer,bat_output,pin,pan,pun,fuera" 
    origen ="'{}',{},{},{},{},{},{},{},{},{},{},{}".format(fecha_base,capacidad_actual,in_power,sun_power,out_power,generator,bat_transfer,bat_output,pin,pan,pun,fuera)

    cursor.execute("insert into gestionpedidos_historico({}) values({})".format(destino,origen))



    con.commit()

    print("++++++++++++++++++++")

    for valor in raw_data.items():
        print(valor)

    time.sleep(5)
