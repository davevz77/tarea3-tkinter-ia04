"""
Pantalla moderna de inicio de sesión
"""
import tkinter as tk
from tkinter import messagebox
from config import COLORS, FONTS
from user_manager import UserManager
import os

class LoginScreen:
    def __init__(self, root, on_login_success, on_register_click):
        self.root = root
        self.on_login_success = on_login_success
        self.on_register_click = on_register_click
        self.user_manager = UserManager()
        
        self.frame = tk.Frame(root, bg=COLORS['white'])
        self.frame.pack(fill='both', expand=True)
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Crea la interfaz de login"""
        # Contenedor principal con dos paneles
        main_container = tk.Frame(self.frame, bg=COLORS['white'])
        main_container.pack(fill='both', expand=True)
        
        # Panel izquierdo (azul con info)
        left_panel = tk.Frame(main_container, bg=COLORS['primary'], width=450)
        left_panel.pack(side='left', fill='both', expand=True)
        left_panel.pack_propagate(False)
        
        # Contenido del panel izquierdo
        left_content = tk.Frame(left_panel, bg=COLORS['primary'])
        left_content.place(relx=0.5, rely=0.5, anchor='center')
        
        # Logo/Título
        title = tk.Label(
            left_content,
            text="UCreativa",
            font=('Segoe UI', 36, 'bold'),
            fg=COLORS['white'],
            bg=COLORS['primary']
        )
        title.pack(pady=(0, 5))
        
        subtitle = tk.Label(
            left_content,
            text="LA U DEL FUTURO",
            font=('Segoe UI', 12, 'bold'),
            fg=COLORS['white'],
            bg=COLORS['primary']
        )
        subtitle.pack(pady=(0, 40))
        
        # Línea decorativa
        line = tk.Frame(left_content, bg=COLORS['white'], height=3, width=120)
        line.pack(pady=(0, 30))
        
        # Descripción
        desc_text = "Sistema de Gestión\nde Estudiantes\n\nIA04 - Razonamiento Artificial"
        description = tk.Label(
            left_content,
            text=desc_text,
            font=FONTS['body'],
            fg=COLORS['white'],
            bg=COLORS['primary'],
            justify='center'
        )
        description.pack(pady=10)
        
        # Panel derecho (formulario)
        right_panel = tk.Frame(main_container, bg=COLORS['white'])
        right_panel.pack(side='right', fill='both', expand=True)
        
        # Contenedor del formulario centrado
        form_container = tk.Frame(right_panel, bg=COLORS['white'])
        form_container.place(relx=0.5, rely=0.5, anchor='center')
        
        # Título del formulario
        form_title = tk.Label(
            form_container,
            text="Iniciar Sesión",
            font=FONTS['title'],
            fg=COLORS['text_dark'],
            bg=COLORS['white']
        )
        form_title.pack(pady=(0, 40))
        
        # Campo Email
        email_label = tk.Label(
            form_container,
            text="Correo Electrónico",
            font=FONTS['heading'],
            fg=COLORS['text_dark'],
            bg=COLORS['white'],
            anchor='w'
        )
        email_label.pack(fill='x', pady=(0, 8))
        
        self.email_entry = tk.Entry(
            form_container,
            font=FONTS['body'],
            bg=COLORS['secondary'],
            fg=COLORS['text_dark'],
            relief='flat',
            bd=0,
            width=35
        )
        self.email_entry.pack(ipady=12, pady=(0, 20))
        
        # Campo Contraseña
        password_label = tk.Label(
            form_container,
            text="Contraseña",
            font=FONTS['heading'],
            fg=COLORS['text_dark'],
            bg=COLORS['white'],
            anchor='w'
        )
        password_label.pack(fill='x', pady=(0, 8))
        
        self.password_entry = tk.Entry(
            form_container,
            font=FONTS['body'],
            bg=COLORS['secondary'],
            fg=COLORS['text_dark'],
            relief='flat',
            bd=0,
            show='●',
            width=35
        )
        self.password_entry.pack(ipady=12, pady=(0, 30))
        
        # Bind Enter key
        self.password_entry.bind('<Return>', lambda e: self._handle_login())
        
        # Botón de login
        login_btn = tk.Button(
            form_container,
            text="Iniciar Sesión",
            font=FONTS['button'],
            bg=COLORS['primary'],
            fg=COLORS['white'],
            activebackground=COLORS['primary_dark'],
            activeforeground=COLORS['white'],
            relief='flat',
            bd=0,
            cursor='hand2',
            command=self._handle_login,
            width=30,
            height=2
        )
        login_btn.pack(pady=(0, 20))
        
        # Texto de registro
        register_frame = tk.Frame(form_container, bg=COLORS['white'])
        register_frame.pack()
        
        register_text = tk.Label(
            register_frame,
            text="¿No tienes cuenta? ",
            font=FONTS['body'],
            fg=COLORS['text_light'],
            bg=COLORS['white']
        )
        register_text.pack(side='left')
        
        register_link = tk.Label(
            register_frame,
            text="Regístrate aquí",
            font=FONTS['body'],
            fg=COLORS['primary'],
            bg=COLORS['white'],
            cursor='hand2'
        )
        register_link.pack(side='left')
        register_link.bind('<Button-1>', lambda e: self.on_register_click())
    
    def _handle_login(self):
        """Procesa el inicio de sesión"""
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        
        if not email or not password:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        success, user_data, message = self.user_manager.login_user(email, password)
        
        if success:
            self.on_login_success(user_data)
        else:
            messagebox.showerror("Error de Login", message)
            self.password_entry.delete(0, 'end')
    
    def show(self):
        """Muestra la pantalla"""
        self.frame.pack(fill='both', expand=True)
    
    def hide(self):
        """Oculta la pantalla"""
        self.frame.pack_forget()