#Archivo de prueba y ejemplo
import configparser
from ConfigConnection import ConfigConnection
from MySQLEngine import MySQLEngine

configDB = configparser.ConfigParser()
configDB.read('Config/config.ini')

db = configDB['mysql']

config = ConfigConnection(db['host'], db['port'], db['user'], db['password'], db['database'])

engine = MySQLEngine(config)

result = engine.select("SELECT * FROM Usuarios;")



for item in result:
    print(item)