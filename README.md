# **README: Solución al Ejercicio de Seguridad en Contraseñas**

## **Descripción del problema**
El objetivo de este proyecto es implementar una función en Python llamada `validate_password` que evalúe la fortaleza de una contraseña basada en los siguientes criterios de seguridad:

1. **Tamaño mínimo**: La contraseña debe tener al menos 8 caracteres.
2. **Mayúsculas**: Debe incluir al menos una letra mayúscula.
3. **Minúsculas**: Debe incluir al menos una letra minúscula.
4. **Números**: Debe contener al menos un número.
5. **Caracteres especiales**: Debe incluir al menos un carácter especial de la lista `!@#$%^&*`.

La aplicación también proporciona una interfaz de consola para que los usuarios ingresen y evalúen la fortaleza de sus contraseñas de forma segura.

---

## **Solución**
### **1. Validación de contraseñas**
La función `validate_password` utiliza expresiones regulares para evaluar si una contraseña cumple con cada una de las reglas descritas. 

#### Código:
```python
import re

def validate_password(password: str) -> bool:
    def min_length(password: str) -> bool:
        return len(password) >= 8
    
    def upper_case(password: str) -> bool:
        return bool(re.search(r'[A-Z]', password))

    def lower_case(password: str) -> bool:
        return bool(re.search(r'[a-z]', password))

    def digit(password: str) -> bool:
        return bool(re.search(r'\d', password))

    def special_character(password: str) -> bool:
        return bool(re.search(r'[!@#$%^&*]', password))

    rules = [
        min_length,
        upper_case,
        lower_case,
        digit,
        special_character,
    ]

    return all(rule(password) for rule in rules)
```

---

### **2. Interfaz segura para ingresar contraseñas**
La aplicación utiliza el módulo `getpass` para solicitar al usuario que ingrese su contraseña de forma oculta, garantizando mayor privacidad y seguridad.

#### Código principal:
```python
import getpass

def main():
    while True:
        print("\n1. Ingresar contraseña")
        print("2. Salir")
        option = input("Selecciona una opción (1 o 2): ").strip()

        if option == "1":
            password = getpass.getpass("Por favor, ingresa tu contraseña: ")

            if validate_password(password):
                print("¡La contraseña es fuerte!")
            else:
                print("La contraseña no cumple con los requisitos de seguridad.")
        elif option == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona 1 o 2.")

main()
```

---

## **Cómo usar**
### **1. Requisitos previos**
- Python 3.6 o superior.
- El módulo `getpass` está incluido por defecto en Python.

### **2. Ejecución del programa**
1. Guarda el código en un archivo llamado `password_validator.py`.
2. Abre una terminal o consola.
3. Ejecuta el archivo con el siguiente comando:
   ```bash
   python password_validator.py
   ```
4. Sigue las instrucciones en la interfaz para ingresar y validar tus contraseñas.

---

## **Ejemplo de uso**
### Entrada:
- Contraseña ingresada: `P@ssw0rd`

### Salida:
```
¡La contraseña es fuerte!
```

### Entrada:
- Contraseña ingresada: `password123`

### Salida:
```
La contraseña no cumple con los requisitos de seguridad.
```

---

## **Características clave**
1. **Validación completa**: Comprueba múltiples reglas de fortaleza.
2. **Interfaz segura**: Utiliza `getpass` para ocultar la contraseña durante la entrada.
3. **Uso sencillo**: Menú interactivo para una experiencia de usuario intuitiva.

---

## **Tecnologías utilizadas**
- **Lenguaje:** Python 3
- **Módulos:** 
  - `re` para expresiones regulares.
  - `getpass` para entrada segura de contraseñas.

---
