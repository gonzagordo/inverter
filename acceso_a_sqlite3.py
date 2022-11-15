import sqlite3
con = sqlite3.connect("/home/pi/pruebas_django/tiendaonline/db.sqlite3")
cursor = con.cursor()
cursor.execute("SELECT * FROM gestionpedidos_grafica" )
resultado =cursor.fetchall()

cursor.execute("insert into gestionpedidos_grafica(valor,fecha) values(1,'2022-11-20') ")

cursor.close()

con.close()


