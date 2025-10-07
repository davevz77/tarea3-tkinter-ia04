"""
Pantalla moderna de registro de usuarios
"""
import tkinter as tk
from tkinter import messagebox
from config import COLORS, FONTS
from user_manager import UserManager

class RegisterScreen:
    def __init__(self, root, on_register_success, on_login_click):
        self.root = root
        self.on_register_success = on_register_success
        self.on_login_click = on_login_click
        self.user_manager = UserManager()
        
        self.frame = tk.Frame(root, bg=COLORS['white'])
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Crea la interfaz de registro"""
        main_container = tk.Frame(self.frame, bg=COLORS['white'])
        main_container.pack(fill='both', expand=True)
        
        # Panel izquierdo (azul con info)
        left_panel = tk.Frame(main_container, bg=COLORS['primary'], width=450)
        left_panel.pack(side='left', fill='both', expand=True)
        left_panel.pack_propagate(False)
        
        # Contenido del panel izquierdo
        left_content = tk.Frame(left_panel, bg=COLORS['primary'])
        left_content.place(relx=0.5, rely=0.5, anchor='center')
        
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
        
        line = tk.Frame(left_content, bg=COLORS['white'], height=3, width=120)
        line.pack(pady=(0, 30))
        
        desc_text = "Únete a la comunidad\nde innovación y creatividad\n\nCrea tu cuenta ahora"
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
        
        # Contenedor del formulario con scroll
        form_canvas = tk.Canvas(right_panel, bg=COLORS['white'], highlightthickness=0)
        form_canvas.pack(side='left', fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(right_panel, orient='vertical', command=form_canvas.yview)
        scrollbar.pack(side='right', fill='y')
        
        form_canvas.configure(yscrollcommand=scrollbar.set)
        
        form_container = tk.Frame(form_canvas, bg=COLORS['white'])
        form_canvas_window = form_canvas.create_window((0, 0), window=form_container, anchor='nw')
        
        # Centrar el formulario
        def center_form(event=None):
            form_canvas.update_idletasks()
            canvas_width = form_canvas.winfo_width()
            form_width = form_container.winfo_reqwidth()
            x_position = max(0, (canvas_width - form_width) // 2)
            form_canvas.coords(form_canvas_window, x_position, 20)
            form_canvas.configure(scrollregion=form_canvas.bbox('all'))
        
        form_canvas.bind('<Configure>', center_form)
        form_container.bind('<Configure>', lambda e: form_canvas.configure(scrollregion=form_canvas.bbox('all')))
        
        # Título
        form_title = tk.Label(
            form_container,
            text="Crear Cuenta",
            font=FONTS['title'],
            fg=COLORS['text_dark'],
            bg=COLORS['white']
        )
        form_title.pack(pady=(20, 30))
        
        # Campo Nombre
        self._create_field(form_container, "Nombre", False, 'nombre_entry')
        
        # Campo Apellido
        self._create_field(form_container, "Apellido", False, 'apellido_entry')
        
        # Campo Email
        self._create_field(form_container, "Correo Electrónico", False, 'email_entry')
        
        # Campo Contraseña
        self._create_field(form_container, "Contraseña", True, 'password_entry')
        
        # Requisitos de contraseña
        req_frame = tk.Frame(form_container, bg=COLORS['white'])
        req_frame.pack(pady=(0, 20))
        
        req_title = tk.Label(
            req_frame,
            text="La contraseña debe contener:",
            font=('Segoe UI', 9),
            fg=COLORS['text_light'],
            bg=COLORS['white']
        )
        req_title.pack(anchor='w')
        
        requirements = [
            "• Mínimo 6 caracteres",
            "• Una letra mayúscula",
            "• Una letra minúscula",
            "• Un carácter especial (!@#$%...)"
        ]
        
        for req in requirements:
            req_label = tk.Label(
                req_frame,
                text=req,
                font=('Segoe UI', 8),
                fg=COLORS['text_light'],
                bg=COLORS['white']
            )
            req_label.pack(anchor='w', padx=(10, 0))
        
        # Botón de registro
        register_btn = tk.Button(
            form_container,
            text="Registrarse",
            font=FONTS['button'],
            bg=COLORS['primary'],
            fg=COLORS['white'],
            activebackground=COLORS['primary_dark'],
            activeforeground=COLORS['white'],
            relief='flat',
            bd=0,
            cursor='hand2',
            command=self._handle_register,
            width=30,
            height=2
        )
        register_btn.pack(pady=(10, 20))
        
        # Link a login
        login_frame = tk.Frame(form_container, bg=COLORS['white'])
        login_frame.pack(pady=(0, 30))
        
        login_text = tk.Label(
            login_frame,
            text="¿Ya tienes cuenta? ",
            font=FONTS['body'],
            fg=COLORS['text_light'],
            bg=COLORS['white']
        )
        login_text.pack(side='left')
        
        login_link = tk.Label(
            login_frame,
            text="Inicia sesión",
            font=FONTS['body'],
            fg=COLORS['primary'],
            bg=COLORS['white'],
            cursor='hand2'
        )
        login_link.pack(side='left')
        login_link.bind('<Button-1>', lambda e: self.on_login_click())
    
    def _create_field(self, parent, label_text, is_password, entry_name):
        """Crea un campo de entrada con su etiqueta"""
        label = tk.Label(
            parent,
            text=label_text,
            font=FONTS['heading'],
            fg=COLORS['text_dark'],
            bg=COLORS['white'],
            anchor='w'
        )
        label.pack(fill='x', padx=40, pady=(0, 8))
        
        entry = tk.Entry(
            parent,
            font=FONTS['body'],
            bg=COLORS['secondary'],
            fg=COLORS['text_dark'],
            relief='flat',
            bd=0,
            show='●' if is_password else '',
            width=35
        )
        entry.pack(ipady=12, padx=40, pady=(0, 20))
        
        setattr(self, entry_name, entry)
    
    def _handle_register(self):
        """Procesa el registro"""
        nombre = self.nombre_entry.get().strip()
        apellido = self.apellido_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        
        if not all([nombre, apellido, email, password]):
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        success, message = self.user_manager.register_user(nombre, apellido, email, password)
        
        if success:
            messagebox.showinfo("Éxito", "¡Cuenta creada exitosamente!\nAhora puedes iniciar sesión.")
            self.on_register_success()
        else:
            messagebox.showerror("Error de Registro", message)
    
    def show(self):
        """Muestra la pantalla"""
        self.frame.pack(fill='both', expand=True)
    
    def hide(self):
        """Oculta la pantalla"""
        self.frame.pack_forget()