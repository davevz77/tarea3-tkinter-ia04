"""
Pantalla principal (Home) después del login
"""
import tkinter as tk
from config import COLORS, FONTS

class HomeScreen:
    def __init__(self, root, user_data, on_logout):
        self.root = root
        self.user_data = user_data
        self.on_logout = on_logout
        
        self.frame = tk.Frame(root, bg=COLORS['white'])
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Crea la interfaz de home"""
        # Header con gradiente visual
        header = tk.Frame(self.frame, bg=COLORS['primary'], height=200)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        # Contenedor del header
        header_content = tk.Frame(header, bg=COLORS['primary'])
        header_content.pack(expand=True)
        
        # Logo/Título
        logo_label = tk.Label(
            header_content,
            text="UCreativa",
            font=('Segoe UI', 28, 'bold'),
            fg=COLORS['white'],
            bg=COLORS['primary']
        )
        logo_label.pack(pady=(10, 5))
        
        subtitle_label = tk.Label(
            header_content,
            text="LA U DEL FUTURO",
            font=('Segoe UI', 10, 'bold'),
            fg=COLORS['white'],
            bg=COLORS['primary']
        )
        subtitle_label.pack()
        
        # Mensaje de bienvenida
        welcome_msg = f"Bienvenido, {self.user_data['nombre']} {self.user_data['apellido']}"
        welcome_label = tk.Label(
            header_content,
            text=welcome_msg,
            font=('Segoe UI', 20),
            fg=COLORS['white'],
            bg=COLORS['primary']
        )
        welcome_label.pack(pady=(20, 10))
        
        # Botón de cerrar sesión en el header
        logout_btn_header = tk.Button(
            header_content,
            text="Cerrar Sesión",
            font=('Segoe UI', 10),
            bg=COLORS['error'],
            fg=COLORS['white'],
            activebackground='#C0392B',
            activeforeground=COLORS['white'],
            relief='flat',
            bd=0,
            cursor='hand2',
            command=self.on_logout,
            width=15
        )
        logout_btn_header.pack(pady=(10, 0))
        
        # Contenedor principal
        main_container = tk.Frame(self.frame, bg=COLORS['white'])
        main_container.pack(fill='both', expand=True, padx=50, pady=40)
        
        # Título de sección
        section_title = tk.Label(
            main_container,
            text="Panel de Estudiante",
            font=FONTS['title'],
            fg=COLORS['text_dark'],
            bg=COLORS['white']
        )
        section_title.pack(pady=(0, 30))
        
        # Grid de tarjetas/módulos
        cards_container = tk.Frame(main_container, bg=COLORS['white'])
        cards_container.pack(pady=20)
        
        # Tarjeta 1 - Mis Cursos
        self._create_card(
            cards_container,
            "📚 Mis Cursos",
            "IA04 - Razonamiento Artificial\nProfesor: Angelo Ortiz Vega",
            0, 0
        )
        
        # Tarjeta 2 - Tareas
        self._create_card(
            cards_container,
            "📝 Tareas Pendientes",
            "Tarea 3: Introducción a Tkinter\nVencimiento: 13 Octubre, 2025",
            0, 1
        )
        
        # Tarjeta 3 - Perfil
        self._create_card(
            cards_container,
            "👤 Mi Perfil",
            f"Email: {self.user_data['email']}\nEstudiante activo",
            1, 0
        )
        
        # Tarjeta 4 - Recursos
        self._create_card(
            cards_container,
            "📖 Recursos",
            "Biblioteca digital\nMaterial de apoyo",
            1, 1
        )
        
        # Botón de cerrar sesión
        logout_btn = tk.Button(
            main_container,
            text="Cerrar Sesión",
            font=FONTS['button'],
            bg=COLORS['error'],
            fg=COLORS['white'],
            activebackground='#C0392B',
            activeforeground=COLORS['white'],
            relief='flat',
            bd=0,
            cursor='hand2',
            command=self.on_logout,
            width=20,
            height=2
        )
        logout_btn.pack(pady=30)
        
        # Footer
        footer = tk.Label(
            main_container,
            text="© 2025 Universidad Creativa - Todos los derechos reservados",
            font=FONTS['small'],
            fg=COLORS['text_light'],
            bg=COLORS['white']
        )
        footer.pack(side='bottom', pady=20)
    
    def _create_card(self, parent, title, content, row, col):
        """Crea una tarjeta informativa"""
        card = tk.Frame(
            parent,
            bg=COLORS['secondary'],
            relief='flat',
            bd=0
        )
        card.grid(row=row, column=col, padx=15, pady=15, sticky='nsew')
        
        # Configurar peso de las columnas
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)
        
        # Contenido interno con padding
        inner_frame = tk.Frame(card, bg=COLORS['secondary'])
        inner_frame.pack(padx=25, pady=25)
        
        # Título de la tarjeta
        card_title = tk.Label(
            inner_frame,
            text=title,
            font=('Segoe UI', 14, 'bold'),
            fg=COLORS['text_dark'],
            bg=COLORS['secondary']
        )
        card_title.pack(anchor='w', pady=(0, 10))
        
        # Contenido de la tarjeta
        card_content = tk.Label(
            inner_frame,
            text=content,
            font=FONTS['body'],
            fg=COLORS['text_light'],
            bg=COLORS['secondary'],
            justify='left'
        )
        card_content.pack(anchor='w')
        
        # Efecto hover
        def on_enter(e):
            card.configure(bg=COLORS['border'])
            inner_frame.configure(bg=COLORS['border'])
            card_title.configure(bg=COLORS['border'])
            card_content.configure(bg=COLORS['border'])
        
        def on_leave(e):
            card.configure(bg=COLORS['secondary'])
            inner_frame.configure(bg=COLORS['secondary'])
            card_title.configure(bg=COLORS['secondary'])
            card_content.configure(bg=COLORS['secondary'])
        
        card.bind('<Enter>', on_enter)
        card.bind('<Leave>', on_leave)
        inner_frame.bind('<Enter>', on_enter)
        inner_frame.bind('<Leave>', on_leave)
    
    def show(self):
        """Muestra la pantalla"""
        self.frame.pack(fill='both', expand=True)
    
    def hide(self):
        """Oculta la pantalla"""
        self.frame.pack_forget()
        