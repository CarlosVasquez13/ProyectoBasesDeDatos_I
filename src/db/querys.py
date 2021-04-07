class Querys:

    def __init__(self) -> None:
        pass
    
    def cargar_tablero():
        query = """SELECT td.id, td.tablero_id, td.fila, td.valor, td.posicion_x, td.posicion_y FROM sudoku.tablero t
            INNER JOIN tablerodetalle td ON td.tablero_id = t.id;"""
        return query