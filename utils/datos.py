import csv
import pathlib

def leer_csv_users(ruta_archivo):
    ruta = pathlib.Path(ruta_archivo)
    usuarios = []
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            funciona = fila['debe_funcionar'].strip().lower() == 'true'
            usuarios.append((fila['usuario'],fila['password'],funciona))
    return usuarios
