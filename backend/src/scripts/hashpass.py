from werkzeug.security import generate_password_hash, check_password_hash
import sys

# Verifica si se proporciona un nombre como argumento de línea de comandos
if len(sys.argv) > 1:
    password = sys.argv[1]
    print(generate_password_hash(password))
else:
    print("Por favor, proporciona un password como argumento.")


