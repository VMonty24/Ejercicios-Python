import random

def mostrar_menu():
    while True:
        print("Elije un juego:")
        print("0 - Salir")
        print("1 - Adivina el numero")
        print("2 - Piedra,Papel,Tijeras")
        print("3 - El ahorcado")
 
        
        opcion = input("Opcion: ")

        if opcion == '1':
            adivina_numero()
        elif opcion == '2':
            piedra_papel_tijeras()
        elif opcion == '3':
            ahorcado()
        elif opcion == '0':
            break
        else:
            print("Opcion no valida")

def adivina_numero():
    print("Bienvenido a 'Adivina el numero'")
    print("Despues de cada intento se te indicara si el numero es inferior o supeior")
    print("Tienes 3 intentos para adivinar un numero del 1 al 10,  buena suerte")

    numeroSecreto = random.randint(1,10)
    intentos = 0

    while intentos < 3:
        numeroUsuario = int(input("Introduce tu numero: "))
        if numeroUsuario not in [1,2,3,4,5,6,7,8,9,10]:
            print("Valor no valido")
        else:
            if numeroUsuario == numeroSecreto:
                print("Enhorabuena has acertado, el numero era ", numeroSecreto)
            elif numeroUsuario < numeroSecreto: 
                print("El numero es mayor al indicado")
                intentos += 1
            else:
                print("El numero es menor al indicado")
                intentos += 1


def piedra_papel_tijeras():
    opciones = ["piedra", "papel","tijeras"]
    playerScore = 0
    machineScore = 0

    while playerScore < 3 and machineScore < 3:
        eleccion = input("Escoge Piedra - Papel - Tijeras: ").lower()    
        if eleccion not in opciones:
            print("Valor no valido")
        else:
            maquina = random.choice(opciones)
            if eleccion == maquina:
                print("Emapte")
            elif (eleccion == "piedra" and maquina == "tijeras") or \
            (eleccion == "tijeras" and maquina == "papel") or \
            (eleccion == "papel" and maquina == "piedra"):
                print("Enhorabuena has ganado esta ronda")
                playerScore += 1
                print("Tu: ", playerScore, " - Maquina: ", machineScore)
            else:
                print("La maquina ha ganado esta ronda")
                machineScore += 1
                print("Tu: ", playerScore, " - Maquina: ", machineScore)

    if playerScore == 3:
        print("Enhorabuena has ganado")
    else:
        print("Lo siento, la Maquina ha ganado") 

def ahorcado():
    with open("C:\\Users\\Victor\\Desktop\\Bernat el Ferrer\\Ejercicios Python\\Avaluable\\palabras.txt", "r") as archivo:
        palabra = archivo.read().splitlines()

    palabra_random = random.choice(palabra)
    intentos = len(palabra_random) * 2 
    letras_correctas = []  

    print(f"La palabra tiene {len(palabra_random)} letras.")

    while (intentos > -1):
        tablero = ""
        for letra in palabra_random:  
            if letra in letras_correctas:
                tablero += letra + " "
            else:
                tablero += "_ "
        
        print("Palabra:", tablero)
        print(f"Intentos restantes: {intentos}")

        letra = input("Introduce una letra: ").lower()

        if letra in letras_correctas:
            print("Ya has probado esa letra.")
        else:
            letras_correctas.append(letra)

            if letra not in palabra_random:
                intentos -= 1  

        todas_acertadas = True 

        for letra in palabra_random: 
            if letra not in letras_correctas:
                todas_acertadas = False

        if todas_acertadas:
            print("Has acertado, la palabra era: ", palabra_random,)
            intentos = -1

    if intentos == 0:
        print("Has perdido. La palabra era:", palabra_random)
        

menu = mostrar_menu()