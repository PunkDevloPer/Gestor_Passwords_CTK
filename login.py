import os
import customtkinter as ctk
import tkinter as tk
from PIL import Image
import database as dtb
from password_management import MasterPanel


class LoginApp:
    def verify_user(self):
        user = self.entry_user.get()
        passwd = self.entry_password.get()
        if dtb.validate_user_exists(user, passwd):
            self.show_welcome_message(user)
            return user
        elif not dtb.validate_user_exists(user, passwd):
            dtb.create_default_user()
        else:
            print("Error")

    def init_master_panel(self, user):
        # Si self.master_panel aún no está inicializado, inicialízalo
        if not hasattr(self, 'master_panel'):
            self.master_panel = None
        self.master_panel = MasterPanel(user)

    def show_welcome_message(self, user):
        welcome_label = ctk.CTkLabel(master=self.frame_login, text=f"Bienvenido {user}",
                                     font=("ButterCookie-Regular", 20), bg_color="#090e0c")
        welcome_label.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        def destroy_label():
            welcome_label.destroy()
            self.init_master_panel(user)
        self.ventana.after(3000, destroy_label)

    def __init__(self):
        self.ventana = ctk.CTk()
        self.master_panel = None
        self.ventana.title("inicio de sesion")
        self.ventana.geometry("500x300")
        self.ventana.resizable(0, 0)
        color = "#222221"
        self.frame_login = ctk.CTkFrame(
            master=self.ventana, fg_color=color)
        self.frame_login.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)

        # frame del logo
        frame_logo = ctk.CTkFrame(
            master=self.frame_login, fg_color="#212023")
        frame_logo.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)

        # imagen
        my_logo = ctk.CTkImage(light_image=Image.open(
            "images/logn.png"), size=(190, 190))

        # label_logo
        label_logo = ctk.CTkLabel(
            master=frame_logo, image=my_logo, text="", width=200, height=200)
        label_logo.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        # label del titulo
        label_title = ctk.CTkLabel(
            master=self.frame_login, text="Inicio de Sesion", fg_color=color, font=("ButterCookie-Regular", 20))
        label_title.pack(expand=tk.YES, fill=tk.BOTH)

        # frame principal de entrys
        frame_entry = ctk.CTkFrame(
            master=self.frame_login, fg_color=color)
        frame_entry.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)

        user_label = ctk.CTkLabel(
            master=frame_entry, text="Usuario:", font=("ButterCookie-Regular", 15), anchor="w", padx=30)
        user_label.pack(fill=tk.BOTH)

        self.entry_user = ctk.CTkEntry(
            master=frame_entry, placeholder_text="Usuario", )
        self.entry_user.pack(fill=tk.X, padx=30, pady=10)

        passwd_label = ctk.CTkLabel(
            master=frame_entry, text="Contraseña:", font=("ButterCookie-Regular", 15), anchor="w", padx=30)
        passwd_label.pack(fill=tk.BOTH)

        self.entry_password = ctk.CTkEntry(
            master=frame_entry, placeholder_text="Contraseña", show=" ")
        self.entry_password.pack(fill=tk.X, padx=30, pady=10)
        framebutton = ctk.CTkFrame(
            master=self.frame_login, fg_color=color)
        framebutton.pack(side=tk.BOTTOM, expand=tk.YES)
        login_button = ctk.CTkButton(master=framebutton, text="Iniciar sesion",
                                     command=self.verify_user)
        login_button.pack(fill=tk.BOTH)
        self.ventana.mainloop()
