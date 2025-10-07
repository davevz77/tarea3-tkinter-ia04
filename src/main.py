"""
Aplicación principal - Sistema de Gestión UCreativa
Tarea 3: Introducción a Tkinter
IA04 - Razonamiento Artificial
"""
import tkinter as tk
from tkinter import messagebox
from config import COLORS, WINDOW_SIZE, MIN_WINDOW_SIZE
from login_screen import LoginScreen
from register_screen import RegisterScreen
from home_screen import HomeScreen

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("UCreativa - Sistema de Gestión")
        self.root.geometry(WINDOW_SIZE)
        self.root.minsize(*MIN_WINDOW_SIZE)
        self.root.configure(bg=COLORS['white'])
        
        # Centrar ventana
        self._center_window()
        
        # Variables de estado
        self.current_user = None
        self.current_screen = None
        
        # Inicializar con pantalla de login
        self.show_login()
        
    def _center_window(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def _clear_screen(self):
        """Limpia la pantalla actual"""
        if self.current_screen:
            self.current_screen.hide()
    
    def show_login(self):
        """Muestra la pantalla de login"""
        self._clear_screen()
        self.current_screen = LoginScreen(
            self.root,
            on_login_success=self.handle_login_success,
            on_register_click=self.show_register
        )
        self.current_screen.show()
    
    def show_register(self):
        """Muestra la pantalla de registro"""
        self._clear_screen()
        self.current_screen = RegisterScreen(
            self.root,
            on_register_success=self.handle_register_success,
            on_login_click=self.show_login
        )
        self.current_screen.show()
    
    def show_home(self):
        """Muestra la pantalla principal"""
        if not self.current_user:
            self.show_login()
            return
        
        self._clear_screen()
        self.current_screen = HomeScreen(
            self.root,
            user_data=self.current_user,
            on_logout=self.handle_logout
        )
        self.current_screen.show()
    
    def handle_login_success(self, user_data):
        """Maneja el login exitoso"""
        self.current_user = user_data
        self.show_home()
    
    def handle_register_success(self):
        """Maneja el registro exitoso"""
        self.show_login()
    
    def handle_logout(self):
        """Maneja el cierre de sesión"""
        result = messagebox.askyesno(
            "Cerrar Sesión",
            "¿Estás seguro que deseas cerrar sesión?"
        )
        if result:
            self.current_user = None
            self.show_login()
    
    def run(self):
        """Inicia la aplicación"""
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()