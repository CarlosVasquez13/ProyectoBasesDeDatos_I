import argparse
import configparser

from db.ConfigConnection import ConfigConnection
from db.MySQLEngine import MySQLEngine
from db.querys import Querys
from Config.responseDto import Reponse

configDB = configparser.ConfigParser()
configDB.read('Config/config.ini')

db = configDB['mysql']

config = ConfigConnection(db['host'], db['port'], db['user'], db['password'], db['database'])


engine = MySQLEngine(config)
	
def user_login(args):
	#query = Querys.login("carlos")
	#query = """SELECT * FROM usuario WHERE nombre_usuario = '""" + user +"""'"""
	result = engine.call_sp("SP_LOGIN", args)
	result_state = result[3] == 1
	resultDto = Reponse(not result_state, result_state, result[4], result[2])
	
	return resultDto

def register_user_db(args):
	result = engine.call_sp("SP_REGISTRAR_USUARIO", args)
	ok = result[5] == 1
	resultDto = Reponse(not ok, ok, result[6], null)
	return resultDto

def cargar_tableros_disponibles():
	result = engine.select("SELECT id, nombre, jugadas_disponibles as ID from tablero")

	tableros = []
	for item in result:
		tablero = {"id": item[0], "nombre": item[1], "jugadas diponibles" : item[2]}
		tableros.append(tablero)
	print(tableros)

# args = ['carlos', 'vasquez','123123123','123','carlos', False, '']
# resulta = register_user_db(args)
# print(resulta.ok)
# print(resulta.message)
#user_login("carlos", "holamundo123")

cargar_tableros_disponibles()