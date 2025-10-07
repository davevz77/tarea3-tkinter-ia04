# 🎓 Sistema de Gestión UCreativa

**Tarea 3: Introducción a Tkinter**  
**IA04 - Razonamiento Artificial**  
**Universidad Creativa de Costa Rica**

---

## 📝 Descripción

Sistema de gestión de estudiantes con interfaz gráfica moderna desarrollado en Python con Tkinter. Implementa un flujo completo de registro, inicio de sesión y acceso a pantalla principal con persistencia de datos en formato JSON.

---

## 👥 Autores

- **[Tu Nombre Aquí]**
- **[Nombre del Compañero 2]** *(si aplica)*
- **[Nombre del Compañero 3]** *(si aplica)*

**Profesor:** Angelo Ortiz Vega  
**Fecha de Entrega:** 13 de Octubre, 2025

---

## ✨ Características

### Funcionalidades Implementadas

- ✅ **Pantalla de Inicio de Sesión**
  - Validación de credenciales
  - Mensajes de error descriptivos
  - Navegación a registro

- ✅ **Pantalla de Registro**
  - Formulario completo (nombre, apellido, email, contraseña)
  - Validaciones robustas:
    - Email con formato válido
    - Contraseña con mínimo 6 caracteres
    - Al menos 1 mayúscula, 1 minúscula y 1 carácter especial
  - Verificación de correos duplicados

- ✅ **Pantalla Principal (Home)**
  - Mensaje de bienvenida personalizado
  - Tarjetas informativas con información del estudiante
  - Botón de cerrar sesión
  - Diseño moderno y responsive

- ✅ **Persistencia de Datos**
  - Almacenamiento en formato JSON
  - Gestión automática de archivos
  - Validación de integridad de datos

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **Tkinter** - Interfaz gráfica
- **JSON** - Persistencia de datos
- **Pillow** - Manejo de imágenes

---

## 📦 Instalación

### Requisitos Previos

- Python 3.8 o superior instalado
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**

```bash
cd tarea3-tkinter
```

2. **Crear entorno virtual**

```bash
python -m venv tarea3
```

3. **Activar el entorno virtual**

**Windows:**
```bash
tarea3\Scripts\activate
```

**macOS/Linux:**
```bash
source tarea3/bin/activate
```

4. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

---

## 🚀 Uso

### Ejecutar la Aplicación

Desde la carpeta raíz del proyecto con el entorno virtual activado:

```bash
python src/main.py
```

### Flujo de Uso

#### 1️⃣ **Registro de Usuario**

1. En la pantalla de inicio, haz clic en **"Regístrate aquí"**
2. Completa el formulario:
   - Nombre
   - Apellido
   - Correo electrónico
   - Contraseña (debe cumplir requisitos)
3. Haz clic en **"Registrarse"**
4. Recibirás confirmación y serás redirigido al login

#### 2️⃣ **Inicio de Sesión**

1. Ingresa tu correo electrónico
2. Ingresa tu contraseña
3. Haz clic en **"Iniciar Sesión"**
4. Serás redirigido a la pantalla principal

#### 3️⃣ **Pantalla Principal**

- Visualiza tu información de bienvenida
- Explora las tarjetas con información
- Usa el botón **"Cerrar Sesión"** para salir

---

## 📁 Estructura del Proyecto

```
tarea3-tkinter/
├── src/
│   ├── assets/
│   │   └── images/
│   │       └── ucreativa_logo.png    # Logo de la universidad
│   ├── main.py                       # Punto de entrada
│   ├── config.py                     # Configuración de colores y estilos
│   ├── user_manager.py               # Gestión de usuarios
│   ├── login_screen.py               # Pantalla de login
│   ├── register_screen.py            # Pantalla de registro
│   └── home_screen.py                # Pantalla principal
├── data/
│   └── users.json                    # Base de datos de usuarios
├── docs/
│   └── screenshots/                  # Capturas de pantalla
├── tarea3/                           # Entorno virtual
├── requirements.txt                  # Dependencias
├── README.md                         # Este archivo
└── .gitignore                        # Archivos ignorados por Git
```

---

## 🎨 Diseño

El diseño de la interfaz está inspirado en aplicaciones modernas con:

- **Paleta de colores moderna** - Azul primario (#4A90E2)
- **Tipografía clara** - Segoe UI
- **Layout de dos paneles** - Información visual + formulario
- **Tarjetas informativas** - En la pantalla principal
- **Efectos hover** - Interactividad mejorada

---

## ⚙️ Validaciones Implementadas

### Validación de Email
- Formato estándar de correo electrónico
- Verificación de dominio válido

### Validación de Contraseña
- ✅ Mínimo 6 caracteres
- ✅ Al menos 1 letra mayúscula (A-Z)
- ✅ Al menos 1 letra minúscula (a-z)
- ✅ Al menos 1 carácter especial (!@#$%^&*...)

### Validación de Registro
- ✅ Todos los campos obligatorios
- ✅ Email único (no duplicado)
- ✅ Trimming de espacios en blanco

---

## 📊 Formato de Datos

Los usuarios se almacenan en `data/users.json` con el siguiente formato:

```json
[
  {
    "nombre": "Juan",
    "apellido": "Pérez",
    "email": "juan.perez@example.com",
    "password": "Password123!"
  }
]
```

**Nota:** En una aplicación de producción, las contraseñas deberían estar hasheadas (bcrypt, scrypt, etc.)

---

## 🐛 Solución de Problemas

### El programa no inicia

```bash
# Verificar que estás en el entorno virtual
# Deberías ver (tarea3) al inicio de la línea

# Reinstalar dependencias
pip install -r requirements.txt
```

### Error de importación de módulos

```bash
# Asegúrate de estar en la carpeta raíz
cd tarea3-tkinter

# Ejecutar desde src/
python src/main.py
```

### No se guardan los usuarios

- Verifica que existe la carpeta `data/`
- Verifica permisos de escritura
- El archivo `users.json` se crea automáticamente

---

## 🎯 Cumplimiento de Requisitos

### Requisitos Obligatorios ✅

- [x] Pantalla de Inicio de Sesión
- [x] Pantalla de Registro de Usuario
- [x] Pantalla Principal (Home)
- [x] Validación de datos de entrada
- [x] Persistencia en archivos (JSON)
- [x] Flujo de navegación correcto
- [x] Validación de contraseñas (6 chars, mayúscula, minúscula, especial)

### Puntos Extra Implementados ✅

- [x] **GitHub:** Repositorio con commits significativos
- [x] **Diseño Previo:** Mockup de las pantallas
- [x] **README Completo:** Con documentación detallada

---

## 📸 Capturas de Pantalla

### Pantalla de Inicio de Sesión
![Login](docs/screenshots/login.png)

### Pantalla de Registro
![Register](docs/screenshots/register.png)

### Pantalla Principal
![Home](docs/screenshots/home.png)

---

## 🔒 Notas de Seguridad

⚠️ **Este es un proyecto educativo.** En producción se debería:

- Hashear contraseñas con bcrypt o argon2
- Usar HTTPS para transmisión de datos
- Implementar rate limiting
- Usar base de datos real (PostgreSQL, MySQL)
- Validar datos del lado del servidor
- Implementar tokens de sesión

---

## 📚 Referencias

- [Documentación oficial de Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Universidad Creativa](https://ucreativa.ac.cr/)
- Material del curso IA04 - Razonamiento Artificial

---

## 📄 Licencia

Este proyecto es parte de un trabajo académico para la Universidad Creativa.

---

## 🙏 Agradecimientos

- **Prof. Angelo Ortiz Vega** - Por la guía y enseñanza
- **Universidad Creativa** - Por la formación en IA
- **Compañeros de clase** - Por el apoyo y colaboración

---

**© 2025 Universidad Creativa - Todos los derechos reservados**