import random

print("¡Bienvenido al juego de adivinar el número!")

# bucle
while True:
    # la maquina elige un numero entre 0 y 50
    num_maquina = random.randint(0, 50)
    # el jugador hace lo mismo
    jugador = int(input("Elegí un número entre 0 y 50: "))
    # comparar los números
    if jugador == num_maquina:
        print("¡Ganaste!")
        # bucle para repetir el juego si gana el jugador
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? ").lower()
        if jugar_de_nuevo == "si":
            continue
        else:
            # si no quiere seguir jugando, se termina el juego
            print("¡Gracias por jugar!")
            break
    # si elige un numero fuera del rango       
    elif jugador < 0 or jugador > 50:
        print("El número no pertenece. Introduce un número entre 0 y 50")
        continue
    else:
        print("Perdiste, intentá de nuevo")
        continue
    