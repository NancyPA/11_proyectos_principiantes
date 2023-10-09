print("---Piedra, papel o tijeras---")
import random
while True:
    aleatorio=random.randrange(0,3)
    eligePc = ""
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijeras")
    opcion = int(input("Elige un numero de opcion: "))

    if opcion == 1:
        eligeUsuario = "Piedra"
    elif opcion == 2:
        eligeUsuario = "Papel"
    elif opcion == 3:
        eligeUsuario = "Tijeras"
    print("Elejiste: ", eligeUsuario)

    if aleatorio == 0:
        eligePc = "Piedra"
    elif aleatorio == 1:
        eligePc = "Papel"
    elif aleatorio == 2:
        eligePc = "Tijeras"
    print("La maquina elijio: ", eligePc)
    if eligePc == "Piedra" and eligeUsuario == "Papel":
        print("Ganaste, papel envuelve piedra")
    elif eligePc == "Papel" and eligeUsuario == "Tijeras":
        print("Ganaste, tijeras cortan papel")
    elif eligePc == "Tijeras" and eligeUsuario == "Piedra":
        print("Ganaste, piedra rompe tijeras")
    elif eligePc == "Papel" and eligeUsuario == "Piedra":
        print("Perdiste, papel envuelve piedra")
    elif eligePc == "Tijeras" and eligeUsuario == "Papel":
        print("Perdiste, tijeras cortan papel")
    elif eligePc == "Piedra" and eligeUsuario == "Tijeras":
        print("Perdiste, piedra rompe tijeras")
    elif eligePc == eligeUsuario:
        print("Empate")

    seguir = input("Otra vez? (s / n): ")
    if seguir.lower() != "s":
        break