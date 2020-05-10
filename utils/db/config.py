#!/usr/bin/python
from configparser import ConfigParser
 
def config(file='database.ini', section='postgresql'):
    # Crear el parser y leer el archivo
    parser = ConfigParser()
    parser.read(file)
 
    # Obtener la sección de conexión a la base de datos
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Seccion {0} no encontrada en el archivo {1}'.format(section, file))