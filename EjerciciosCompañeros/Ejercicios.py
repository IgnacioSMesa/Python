import itertools
import unicodedata


ejercicio = 4

match ejercicio:
    case 1:
        """
        Ejercicio(Jojo): Hacer una función a la que se le introduce strings y devuelve una cadena con los datos introducidos usando .format()
        """

        def concatenarCadenas(saludo, nombre, edad):
            texto = "{fsaludo} como estas {fnombre} tienes {fedad} años"
            return texto.format(fsaludo = saludo, fnombre = nombre, edad = edad)

        print(concatenarCadenas("Hola" ,"Natalia", "20"))
    case 2:
        """
        Ejercicio 8 (Diego Scott): Dado un array de correos introduce en una lista los nombres de los correos siguientes:
         correos = [ barack.obama@nagger.com", angela.merkel@pretzel.com", emmanuel.macron@gabacho.com", 
         justin.trudeau@pokemon.com", gorgefluidos@air.lkc" ]
        """
        correos = ["barack.obama@nagger.com",
                   "angela.merkel@pretzel.com",
                   "emmanuel.macron@gabacho.com",
                   "justin.trudeau@pokemon.com",
                   "gorgefluidos@air.lkc"]

        def correos_nombres(correos):
            nombres = []
            for correo in correos:
                nombres.append(correo.split("@")[0])

            return nombres

        print(correos_nombres(correos))
    case 3:
        """
        # Haz un metodo que reemplace cada palabra con la primera letra en mayuscula y cuenta cuantas ‘e’ hay.
        # frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"
        """

        def reempleazarMayuscula(frase):

            contador = 0

            for letra in frase.split(" "):
                print(letra.capitalize())

            for e in frase:
                if e == "e":
                    contador += 1
            print(contador, "letras(e)")

        print(reempleazarMayuscula("Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"))
    case 4:

        def anagrama(palabra1, palabra2):

            palabra1 = palabra1.lower().replace(" ", "")
            palabra2 = palabra2.lower().replace(" ", "")

            #tener en cuenta tildes
            palabra1 = unicodedata.normalize("NFD", palabra1) #Quita tildes, dieresis, ñ etc
            palabra1 = palabra1.encode("ascii", "ignore") #todo lo que se salga del ascii lo ignora

            palabra2 = unicodedata.normalize("NFD", palabra2)
            palabra2 = palabra2.encode("ascii", "ignore")

            return sorted(palabra1) == sorted(palabra2)


        frase = "I am lord voldemort"
        frase2 = "Tom marvolo riddle"

        if anagrama(frase, frase2):
            print("Es anagrama")
        else:
            print("No anagrama")
    case 5:
        """
        Pedir al usuario una frase y que se muestre la frase en minúsculas, mayúsculas, 
        el numero de palabras que tiene, las palabras en orden inverso y la cantidad de veces que aparece la letra “a”.
        """
        contadorA = 0
        frase = input("Escriba una frase: ")

        print("Frase en minúsculas: ", frase.lower())
        print("Frase en mayúsculas: ",frase.upper())

        palabras = frase.split()

        print("Tiene: ", len(palabras), "palabras")
        print("Palabras al revés: ", " ".join(reversed(palabras)))

        for a in frase:
            if a == "a":
                contadorA += 1

        print("Tiene: ", contadorA, "letras(a)")
    case 6:
        """
        Escribe un programa que solicite al usuario una cadena de texto y, posteriormente, una palabra a buscar dentro de esa cadena. 
        El programa deberá comprobar si la palabra aparece en el texto.
        
        Si la palabra se encuentra, el programa debe imprimir el texto original pero eliminando únicamente la primera aparición de esa palabra.
        Si la palabra no se encuentra en la cadena:
	    El programa debe eliminar alguna palabra existente de la cadena (puede ser la primera, la última o 	cualquier otra, según prefieras diseñarlo).
	    Luego debe añadir la palabra buscada a la cadena, sin colocar nada delante de ella, aunque su posición 	resulte en que la nueva palabra quede en medio del texto.
	    Finalmente, debe mostrar la cadena resultante tras la modificación.
        """

        cadena = input("Escriba una cadena: ")
        palabra_buscar = input("Escriba una palabra a buscar: ")

        if palabra_buscar in cadena:
            cadena_modificada = cadena.replace(palabra_buscar, "", 1)
            print("Cadena modificada:", cadena_modificada)

        else:
            palabras = cadena.split()

            if palabras:
                palabras.pop(0)

            palabras.append(palabra_buscar)

            cadena_modificada = " ".join(palabras)
            print("Cadena modificada:", cadena_modificada)
    case 7:
        """
        El programa quiere poder contar cuantas de una letra tiene la cadena que ha metido el usuario, 
        después de sacar el número de letras sacara por pantalla los 4 últimos caracteres
        (tener cuidado de que no meta espacios en blanco).
        """
        def contarLetras(cadena, letra = "a"):

            contador = 0
            cadenaLimpia = cadena.replace(" ", "")
            for palabra in cadenaLimpia:
                if letra in palabra:
                    contador += 1
            return f"Hay {contador} {letra}, los 4 ultimos caracteres son: {cadenaLimpia[-4:]}"

        print(contarLetras("Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"))
    case 8:
        """
        Crear una función que cuente las vocales de una cadena
        """
        def contarVocales(cadena):
            contador = 0
            vocales = "aeiouAEIOU"

            for letra in cadena:
                if letra in vocales:
                    contador += 1

            return contador

        print(contarVocales("hola mundo"))
    case 9:
        """
        Buscar una letra, en una cadena cualquiera pedida por teclado y pasarla a mayúscula
        """
         #"Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"

        cadena = input("Escriba una cadena: ").lower()

        letra = "e".lower()
        if letra in cadena:
            print(cadena.replace(letra, letra.upper()))
        else:
            print("La letra no está en la cadena.")
    case 10:
        """
        Ejercicio(Oscar Pérez): Crea una función que al pasarle una frase cuente el numero de vocales que tiene en total
         y que pregunte por que otra vocal quiere cambiar todas las vocales de la frase, que retorne la frase cambiada 
         y el numero de vocales de la frase antes de cambiarlas.
        """

        cadena = input("Escriba una cadena: ")

        def ejercicio(cadena):
            contador = 0
            vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"

            for letra in cadena:
                if letra in vocales:
                    contador += 1

            vocalSustituta = input("Escriba una vocal a sustituir: ")

            while vocalSustituta not in vocales:
                vocalSustituta = input("Opción inválida, escriba una vocal a sustituir: ")

            frase = cadena
            for vocal in vocales:
                frase = frase.replace(vocal, vocalSustituta)

            return f"Total vocales: {contador} \nFrase cambiada: {frase}"

        print(ejercicio(cadena))
    case 11:
        """
        Invertir palabras de más de 5 letras
        """
        frase = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres"

        def invertirPalabras(frase):
            palabras = frase.split()
            palabras_invertidas = []

            for p in palabras:
                if len(p) > 5:
                    palabras_invertidas.append(p[::-1]) # para ir hacia atrás
                else:
                    palabras_invertidas.append(p)

            return ' '.join(palabras_invertidas)

        resultado = invertirPalabras(frase)
        print(resultado)
    case 12:
        ciudades = ["A", "B", "C", "D"]

        distancias = {
            ("A", "B"): 5, ("A", "C"): 9, ("A", "D"): 4,
            ("B", "A"): 5, ("B", "C"): 7, ("B", "D"): 6,
            ("C", "A"): 9, ("C", "B"): 7, ("C", "D"): 3,
            ("D", "A"): 4, ("D", "B"): 6, ("D", "C"): 3,
        }


        def distancia(ruta):
            total = 0
            for i in range(len(ruta) - 1):
                total += distancias[(ruta[i], ruta[i + 1])]
            return total


        inicio = "A"
        otras = [c for c in ciudades if c != inicio]

        mejor_ruta = None
        mejor_distancia = float("inf")

        for perm in itertools.permutations(otras):
            ruta = [inicio] + list(perm) + [inicio]
            d = distancia(ruta)
            if d < mejor_distancia:
                mejor_distancia = d
                mejor_ruta = ruta

        print("Mejor ruta:", " → ".join(mejor_ruta))
        print("Distancia total:", mejor_distancia)

    case 13:

        """
        Palindromos
        """




        def esPalindromo(frase):
            fraseLimpia = frase.replace(" ", "").lower()
            fraseLimpia = unicodedata.normalize("NFD", fraseLimpia)
            fraseLimpia = fraseLimpia.encode("ascii", "ignore")

            return fraseLimpia == fraseLimpia[::-1]

        if esPalindromo("Dábale arroz a la zorra el abad"):
            print("Palindromo")
        else:
            print("No palindromo")