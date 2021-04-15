class Querys:

    def __init__(self) -> None:
        pass
    
    def cargar_tablero(tableroID):
        query = """SELECT td.id, td.tablero_id, td.fila, td.valor, td.posicion_x, td.posicion_y FROM sudoku.tablero t
            INNER JOIN tablerodetalle td ON td.tablero_id = t.id
            WHERE t.id = """ + str(tableroID)
        print(query)
        return query
	
	# def cargar_tableros_disponibles():
	# 	query = "SELECT id, nombre, jugadas_disponibles as ID from tablero"
	# 	return query
 	# def login():
 	# 	query = """SELECT * FROM usuario WHERE nombre_usuario = carlos"""
 	# 	return query
