import re
import getpass

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
