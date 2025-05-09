from datetime import datetime
dia = int(input("Ingresa el día de tu nacimiento:  "))
mes = int(input("Ingresa el mes de tu nacimiento (en números):   "))
año = int(input("Ingresa el año de tu nacimiento:   "))

fecha_de_nacimiento = datetime(año,mes,dia)
fecha_de_hoy = datetime.now()
print(fecha_de_hoy - fecha_de_nacimiento)
