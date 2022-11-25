import sqlite3
import datetime, time

con = sqlite3.connect("/home/pi/pruebas_django/tiendaonline/db.sqlite3")
cursor = con.cursor()
#cursor.execute("SELECT * FROM gestionpedidos_grafica" )
#cursor.execute("SELECT * FROM gestionpedidos_tiempo" )

#resultado =cursor.fetchall()

#cursor.execute("insert into gestionpedidos_grafica(valor,fecha) values(1,'2022-11-21') ")
#modo simple 
#cursor.execute("insert into gestionpedidos_tiempo(x,y) values('2022-11-22 19:15:56',6) ")
#con variables 
# fecha = '2022-11-22 22:18:56'
now = datetime.datetime.now()
fecha_base = now.strftime("20%y-%m-%d %H:%M:%S")
capacidad_actual = 59
cursor.execute("insert into gestionpedidos_tiempo(x,y) values('{}',{}) ".format(fecha_base,capacidad_actual))

con.commit()

cursor.close()
con.close()


