archivo="Alumnos.txt"
with open(archivo,"r") as fichero:
    for línea in fichero.readlines():
        print(línea, end="")