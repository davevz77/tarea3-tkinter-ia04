"""
Gestor de usuarios con persistencia en JSON
"""
import json
import os
import re
from typing import Dict, Optional

class UserManager:
    def __init__(self, data_file: str = "data/users.json"):
        self.data_file = data_file
        self._ensure_data_file()
    
    def _ensure_data_file(self):
        """Crea el archivo de datos si no existe"""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump([], f)
    
    def _load_users(self) -> list:
        """Carga todos los usuarios del archivo"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    def _save_users(self, users: list):
        """Guarda usuarios en el archivo"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(users, f, indent=2, ensure_ascii=False)
    
    def validate_password(self, password: str) -> tuple[bool, str]:
        """
        Valida que la contraseña cumpla con los requisitos
        Retorna: (es_válida, mensaje_error)
        """
        if len(password) < 6:
            return False, "La contraseña debe tener mínimo 6 caracteres"
        
        if not re.search(r'[A-Z]', password):
            return False, "Debe contener al menos una letra mayúscula"
        
        if not re.search(r'[a-z]', password):
            return False, "Debe contener al menos una letra minúscula"
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False, "Debe contener al menos un carácter especial"
        
        return True, ""
    
    def validate_email(self, email: str) -> tuple[bool, str]:
        """Valida formato de email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            return False, "Formato de correo inválido"
        return True, ""
    
    def email_exists(self, email: str) -> bool:
        """Verifica si el correo ya está registrado"""
        users = self._load_users()
        return any(user['email'] == email for user in users)
    
    def register_user(self, nombre: str, apellido: str, email: str, password: str) -> tuple[bool, str]:
        """
        Registra un nuevo usuario
        Retorna: (éxito, mensaje)
        """
        # Validar email
        valid, msg = self.validate_email(email)
        if not valid:
            return False, msg
        
        # Verificar si existe
        if self.email_exists(email):
            return False, "Este correo ya está registrado"
        
        # Validar contraseña
        valid, msg = self.validate_password(password)
        if not valid:
            return False, msg
        
        # Guardar usuario
        users = self._load_users()
        users.append({
            'nombre': nombre.strip(),
            'apellido': apellido.strip(),
            'email': email.strip().lower(),
            'password': password  # En producción, esto debería estar hasheado
        })
        self._save_users(users)
        
        return True, "Usuario registrado exitosamente"
    
    def login_user(self, email: str, password: str) -> tuple[bool, Optional[Dict], str]:
        """
        Valida credenciales de login
        Retorna: (éxito, datos_usuario, mensaje)
        """
        users = self._load_users()
        
        for user in users:
            if user['email'] == email.strip().lower():
                if user['password'] == password:
                    return True, user, "Login exitoso"
                else:
                    return False, None, "Contraseña incorrecta"
        
        return False, None, "Usuario no registrado"