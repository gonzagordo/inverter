#probando en python 3 
import os, sys, datetime, time, json

print("funcionando en remoto")

def convert (valor):
     a= str(round(float(valor),2))
     return a

    
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

    with open('/home/pi/inverter/data.json', 'w') as f:
        json.dump(raw_data, f, ensure_ascii=False, indent=4)


    print("++++++++++++++++++++")

    for valor in raw_data.items():
        print(valor)

    time.sleep(5)
