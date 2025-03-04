1
n = int(input("escribe el porcentaje de tu calificación"  ))
if n > 90: 
    print("Sacaste A")
elif n >80 and n <=90:
    print("Sacaste B")
elif n >=60 and n <=80:
    print("Sacaste C")
else:
    print("Sacaste D")

2
x = int(input("ingresa el precio de la bicicleta"  ))
if x >100000:
    print("Se le añade el 15%. El precio con IVA sería  ", x * 0.15)
elif x >5000 and x <=100000:
    print("Se le añade el 10%. El precio con IVA sería   ", x * 0.10)
else:
    print("Se le añade el 5%. El precio con IVA sería   ", x * 0.05)

3
año = int(input("Qué año quieres saber si es bisiesto?"))
año_bisiesto = 2024
if (año_bisiesto - año) % 4 == 0:
    print("ese año es  bisiesto")
else:
    print("no es año bisiesto")

4
numero = int(input("ingresa un número del 1-7 para saber el día"))
if numero == 1:
    print("es Lunes")
elif numero == 2:
    print("es Martes")
elif numero == 3:
    print("es Miércoles")
elif numero == 4:
    print("es Jueves")
elif numero == 5:
    print("es Viernes")
elif numero == 6:
    print("es Sábado")
else:
    print("es Domingo")


5
mes = int(input("ingresa un número del 1-12 para saber el mes"))
if mes == 1:
    print("es Enero")
elif mes == 2:
    print("es Febrero")
elif mes == 3:
    print("es Marzo")
elif mes == 4:
    print("es Abril")
elif mes == 5:
    print("es Mayo")
elif mes == 6:
    print("es Junio")
elif mes == 7:
    print("es Julio")
elif mes == 8:
    print("es Agosto")
elif mes == 9:
    print("es Septiembre")
elif mes == 10:
    print("es Octubre")
elif mes == 11:
    print("es Noviembre")
else:
    print("es Diciembre")