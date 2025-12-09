"""
Desarrolla un sistema de login sencillo utilizando únicamente operaciones básicas de cadenas
 (por ejemplo: .lower(), .replace(), .split(), concatenación, slicing, reversed(), etc.).

El programa deberá pedir por teclado un nombre de usuario y una contraseña, y convertir ambos valores a minúsculas.

La contraseña deberá “cifrarse” usando un método basado únicamente en manipulación de cadenas.

Por ejemplo: invertir la cadena, sustituir caracteres o intercalar texto.
El método elegido deberá aplicarse también al comprobar las credenciales.

La contraseña ya transformada deberá guardarse dentro de una lista de contraseñas.

A continuación, se creará una cadena que contenga el nombre de usuario en minúsculas
seguido de “:”, seguido de la contraseña cifrada.
Esta cadena representará las credenciales guardadas del sistema.

Implementa un método llamado unirCredenciales(usuario, contraseña) que convierta
ambas a minúsculas, aplique el mismo cifrado de cadenas a la contraseña y una ambas usando
el formato usuario:contraseñaCIFRADA.
Después, comparará el resultado con las credenciales almacenadas.

El método deberá devolver:

"Sesión iniciada" si coinciden.

"Credenciales inválidas" si no coinciden.
"""

def cifrar(texto):
    texto = texto.lower()
    texto = texto[::-1]
    texto = texto.replace("a", "@")
    texto = texto.replace("e", "3")
    texto = texto.replace("i", "1")
    texto = texto.replace("o", "0")
    texto = texto.replace("u", "µ")
    return texto


nombre = input("Escriba su nombre de usuario: ").lower()
passwd = input("Escriba su contraseña: ").lower()

passwd_cifrada = cifrar(passwd)

lista_contraseñas = []
lista_contraseñas.append(passwd_cifrada)

credenciales_guardadas = f"{nombre}:{passwd_cifrada}"

def unirCredenciales(usuario, pwd):
    usuario = usuario.lower()
    pwd_cifrada = cifrar(pwd.lower())

    credenciales_introducidas = usuario + ":" + pwd_cifrada

    if credenciales_introducidas == credenciales_guardadas:
        return "Sesión iniciada"
    else:
        return "Credenciales inválidas"

usuario_login = input("Introduzca usuario para iniciar sesión: ")
clave_login = input("Introduzca contraseña: ")

resultado = unirCredenciales(usuario_login, clave_login)
print(resultado)
