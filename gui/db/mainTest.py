#Archivo de prueba y ejemplo

import sys
import configparser
from ConfigConnection import ConfigConnection
from MySQLEngine import MySQLEngine

configDB = configparser.ConfigParser()
configDB.read('Config/config.ini')

db = configDB['mysql']

config = ConfigConnection(db['host'], db['port'], db['user'], db['password'], db['database'])

engine = MySQLEngine(config)

query = """SELECT td.id, td.tablero_id, td.fila, td.valor, td.posicion_x, td.posicion_y FROM sudoku.tablero t
        INNER JOIN tablerodetalle td ON td.tablero_id = t.id;"""
result = engine.select(query)


listItems = []
for item in result:
    tableroFila =  {"id":item[0], "tableroId": item[1], "fila": item[2], "valor": item[3], "posicionX": item[4], "posicionY": item[5]}
    print(tableroFila)
    listItems.append(tableroFila)
    print(item)

print(listItems)

for fila in listItems:
    print(fila['valor'])