"""password manager"""
import customtkinter as ctk
import database as dtb


class MasterPanel:
    """Clase del panel principal del gestor de contraseñas"""

    def __init__(self, user):
        self.user = user
        self.ventana = ctk.CTk()
        self.ventana.geometry("500x500")
        self.ventana.resizable(0, 0)
        self.ventana.title("Gestor de Contraseñas")
        self.setup_window()

    def setup_window(self):
        frame = ctk.CTkFrame(master=self.ventana)
        frame.configure(width=500, height=500)
        frame.pack(side="left", fill="both")
        frame_img = ctk.CTkFrame(
            master=frame, width=100, height=100, corner_radius=100)
        frame_img.pack(anchor="center", padx=10, pady=10)
        label_nick = ctk.CTkLabel(master=frame, text=f"Usuario: {self.user}")
        label_nick.pack(anchor="nw", padx=10, pady=10)

        boton_accounts = ctk.CTkButton(master=frame, text="Cuentas",
                                       command="")
        boton_accounts.pack(anchor="w", padx=10, pady=10)

        botton_add = ctk.CTkButton(
            master=frame, text="Anadir Cuenta", command=dtb.open_register)
        botton_add.pack(anchor="w", padx=10, pady=10)

        exportdb = ctk.CTkButton(master=frame, text="Exportar Base de datos")
        exportdb.pack(anchor="w", padx=10, pady=10)

        config = ctk.CTkButton(master=frame, text="Configuracion")
        config.pack(anchor="w", padx=10, pady=10)
        self.ventana.mainloop()
