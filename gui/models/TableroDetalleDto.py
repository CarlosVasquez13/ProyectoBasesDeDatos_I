
class TableroDetalleDto:
    id = 0
    tableroId = 0
    fila = 0
    valor = ""
    posicionX = 0
    posicionY = 0
    
    def __init__(self, id, tableroId, fila, valor, posicionX, posicionY):
        self.id = id
        self.tableroId = tableroId
        self.fila = fila
        self.valor = valor
        self.posicionX = posicionX
        self.posicionY = posicionY
    