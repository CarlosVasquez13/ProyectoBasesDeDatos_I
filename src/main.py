from sudoku import open_sudoku, cargar_tablero_data
from tkinter import *
import configparser
from db.ConfigConnection import ConfigConnection
from db.MySQLEngine import MySQLEngine
from db.querys import Querys


configDB = configparser.ConfigParser()
configDB.read('Config/config.ini')

db = configDB['mysql']

config = ConfigConnection(db['host'], db['port'], db['user'], db['password'], db['database'])


engine = MySQLEngine(config)

splash_root = Tk()
splash_root.title("Splash Screen!!")

#Add icon
# splash_root.iconbitmap('c:/gui...')
app_width = 500
app_height = 500

screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

x = (screen_width // 2) - (app_width // 2)
y = (screen_height // 2) - (app_height // 2)



splash_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
# hide title bar
#splash_root.overrideredirect(True)

splash_label = Label(splash_root, text="Splash Screen", font=("Helvetica", 18))
splash_label.pack(pady=20)

def main_window():
    splash_root.destroy()

    root = Tk()
    root.title('Main window')
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    btn = Button(root, text ="Click to open a new window", command=main_sudoku)
    btn.pack(pady= 10)
    #root.geometry("300x550+-1500+250")

    main_label = Label(root, text="main window", font=("Helvetica", 19))
    main_label.pack(pady=20)

def main_sudoku():
    # query = Querys.cargar_tablero()
    # result = engine.select(query)

    # listItems = []
    # for item in result:
    #     tableroFila =  {"id":item[0], "tableroId": item[1], "fila": item[2], "valor": item[3], "posicionX": item[4], "posicionY": item[5]}
    #     line = item[3].strip()
        
    #     listItems.append([])
    #     for c in line:            
    #         listItems[-1].append(int(c))

    # cargar_tablero_data()
    # open window game
    open_sudoku()
    pass

# splash screen timer
splash_root.after(1000, main_window)


mainloop()