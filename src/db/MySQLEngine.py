import mysql.connector as sql
#from mysql.connector import MySQLConnection, Error
class MySQLEngine: 
    def __init__(self, config):
        self.config = config
              
        self.mydb = sql.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            password=config.password,
            database=config.database
        )
       

    def select(self, query):
        link = self.mydb.cursor()

        link.execute(query)
        result = link.fetchall()
        return result

    #Metodo para ejecutar los procedimientos almacenados
    def call_sp(self, sp, args):
        try:
            ##con = MySQLConnection(self.config)
            link = self.mydb.cursor()

            result = link.callproc(sp, args)
            return result
        except Exception as e:
            print(e)
        finally:
            
            link.close()
            #con.close();

        