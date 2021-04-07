import mysql.connector

class MySQLEngine: 
    def __init__(self, config):
        self.config = config
              
        self.mydb = mysql.connector.connect(
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
