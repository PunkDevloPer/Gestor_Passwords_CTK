"""importar librerias"""
from tkinter import messagebox
import os
import sqlite3
import customtkinter as ctk


def conectdb():
    """_summary_
    Conect the database to the program
    Returns:
        _type_: _description_
    """
    sqlite3.connect("data/passwords.db")
    return "data/passwords.db"


def create_default_user():
    """ Create default user """
    if validate_user_exists("admin", ""):
        bdd = sqlite3.connect(conectdb())
        cursor = bdd.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND password=?",
                       ("admin", ""))
        resultado = cursor.fetchone()
        bdd.close()
        print("El usuario por defecto ya existe.")

        return resultado is not None
    else:
        create("admin", "")
        print("Usuario por defecto creado con éxito.")


def open_register():
    """_summary_"""
    new_window = ctk.CTk()
    new_window.geometry("220x200")
    new_window.resizable(False, False)
    new_window.title = "Registrar Usuario"
    user_label = ctk.CTkLabel(new_window, text="Usuario")
    user_label.pack()
    user_entry = ctk.CTkEntry(new_window, corner_radius=10)
    user_entry.pack()
    user_pass = ctk.CTkLabel(new_window, text="Contraseña")
    user_pass.pack()
    pass_entry = ctk.CTkEntry(new_window, show="*", corner_radius=10)
    pass_entry.pack()
    register_label = ctk.CTkLabel(new_window, text="", font=("Arial", 16))
    register_label.pack()

    # Añadimos el botón de registro y le pasamos las entradas como argumentos
    register_button = ctk.CTkButton(
        new_window, text="Registrarse",
        command=lambda: [on_register(new_window, user_entry, pass_entry)], corner_radius=10)
    register_button.pack()

    new_window.mainloop()


def validate_user_exists(nombre, password):
    """Validate is user exists in database"""
    bdd = sqlite3.connect(conectdb())
    cursor = bdd.cursor()
    create_table_users = '''
            CREATE TABLE if not exists usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                password varchar(255)
            )'''
    cursor.execute(create_table_users)
    cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND password=?",
                   (nombre, password))
    resultado = cursor.fetchone()

    bdd.close()

    return resultado is not None


def on_register(app, user_entry, pass_entry):
    """Register user function"""
    nombre = user_entry.get()
    password = pass_entry.get()

    # Verifica si el usuario ya existe
    if validate_user_exists(nombre, password):
        messagebox.showerror("Error", "El usuario y la clave ya existen")

    else:
        create(nombre, password)
        messagebox.showinfo("Éxito", "Registrado con éxito")
        app.destroy()


def create(nombre, password):
    """create database if not exist"""
    route = conectdb()
    if os.path.exists(route):
        bdd = sqlite3.connect(route)
        cursor = bdd.cursor()

        create_table_query1 = '''
            CREATE TABLE if not exists usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                password varchar(255)
            )'''
        cursor.execute(create_table_query1)
        insert_user_query1 = "INSERT INTO usuarios (nombre, password) VALUES (?, ?)"
        cursor.execute(insert_user_query1, (nombre, password))
        bdd.commit()
        bdd.close()


def read():
    """read the database"""
    pass


def update():
    """update the database"""
    pass


def delete():
    """delete user in the database"""
    pass
