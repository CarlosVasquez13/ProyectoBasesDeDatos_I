from tkinter import *
import os
from funciones import *
from sudoku import open_sudoku
from sudoku import open_sudoku, cargar_tablero_data

 # Splash screen 
splash_root = Tk()
splash_root.title("Splash Screen!!")
app_width = 500
app_height = 500

screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

x = (screen_width // 2) - (app_width // 2)
y = (screen_height // 2) - (app_height // 2)
splash_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
splash_label = Label(splash_root, text="Splash Screen", font=("Helvetica", 18))
splash_label.pack(pady=20)


# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x500")
 
    global username
    global password
    global userLastName
    global usernameNick
    global identityNumber

    global username_entry
    global password_entry
    global userLastName_entry
    global usernameNick_entry
    global identityNumber_entry

    username = StringVar()
    password = StringVar()
    userLastName = StringVar()
    usernameNick = StringVar()
    identityNumber = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    
    userLastName_label = Label(register_screen, text="Apellido * ")
    userLastName_label.pack()
    userLastName_entry = Entry(register_screen, textvariable=userLastName)
    userLastName_entry.pack()
    
    identityNumber_label = Label(register_screen, text="No.Identidad * ")
    identityNumber_label.pack()
    identityNumber_entry = Entry(register_screen, textvariable=identityNumber)
    identityNumber_entry.pack()

    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    usernameNick_label = Label(register_screen, text="Nombre de usuario * ")
    usernameNick_label.pack()
    usernameNick_entry = Entry(register_screen, textvariable=usernameNick)
    usernameNick_entry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Iniciar Sesión")
    login_screen.geometry("300x250")
    Label(login_screen, text="Introduzca sus credenciales").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Nombre de usuario * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Contraseña * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Iniciar sesión", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()

    #desarrollo
    #Registrar usuario en base de datos
    args = [username.get(), userLastName.get(), identityNumber.get(), password.get(), usernameNick.get(), False, '']

    result = register_user_db(args)
    print(result.message)
    # file = open(username_info, "w")
    # file.write(username_info + "\n")
    # file.write(password_info)
    # file.close()
    
    if result.ok:
        Label(register_screen, text="Registro completado", fg="green", font=("calibri", 11)).pack()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        userLastName_entry.delete(0, END)
        identityNumber_entry.delete(0, END)
        usernameNick_entry.delete(0, END)
    else: 
        Label(register_screen, text="Error: " + result.message, fg="green", font=("calibri", 11)).pack()

 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    #VERIFICAR CON DATOS DE LA BASE DE DATOS
    response = user_login([username1, password1, '', False, ''])

    if response.ok:
        login_sucess()
    else:
        password_not_recognised()
    # list_of_files = os.listdir()
    # if username1 in list_of_files:
    #     file1 = open(username1, "r")
    #     verify = file1.read().splitlines()
    #     if password1 in verify:
    #         login_sucess()
 
    #     else:
    #         password_not_recognised()
 
    # else:
    #     user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    main_screen.destroy()
    #open_sudoku()
    second_main_screen()
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Inicio de sesión completado.").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("300x300")
    Label(password_not_recog_screen, text="Usuario o Contraseña incorrectos").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("200x200")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    splash_root.destroy()
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()

def second_main_screen():
    
    global second_main_screen
    second_main_screen = Tk()
    second_main_screen.geometry("300x250")
    second_main_screen.title("Segunda pantalla")
    # Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    # Label(text="").pack()
    #Button(text="Login", height="2", width="30", command = login).pack()
    #Label(text="").pack()
    # Button(text="Register", height="2", width="30", command=register).pack()
 
    second_main_screen.mainloop()

def splash_screen():
    global splash_screen
    splash_screen = Tk()
    #splash_screen.geometry


splash_root.after(1000, main_account_screen)


mainloop()
#main_account_screen()