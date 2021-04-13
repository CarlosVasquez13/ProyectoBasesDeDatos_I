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
	
def user_login(user, password):
	#query = Querys.login("carlos")
	query = """SELECT * FROM usuario WHERE nombre_usuario = '""" + user +"""'"""
	result = engine.select(query)
	user = result[0]
	valid = user[3] == password
	resultDto = Reponse(False, valid, "holamundo123")
	
	return resultDto

#user_login("carlos", "holamundo123")