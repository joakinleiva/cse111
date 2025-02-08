import random
import os

def imprimir_tabla(intentos):
    for i in range(1, 51, 10):
        fila = []
        for j in range(i, i + 10):
            if j in intentos:
                fila.append(f"[~{j}~]")  # Formato tachado
            else:
                fila.append(f"{j:2}")  # Mantiene la alineación
        print(" ".join(fila))

def guardar_record(nombre, intentos):
    # Verifica si el archivo de records existe
    if not os.path.exists("records.txt"):
        with open("records.txt", "w") as f:
            f.write("NOMBRE   |   INTENTOS\n")  # Escribe la cabecera si el archivo no existe
    
    # Guarda los datos del jugador
    with open("records.txt", "a") as f:
        f.write(f"{nombre:<8} |   {len(intentos)}\n")

def mostrar_records():
    # Verifica si el archivo de records existe
    if not os.path.exists("records.txt"):
        print("No hay registros de jugadores aún.")
        return []
    
    # Muestra los records con formato y los devuelve
    print("\n--- Records de Jugadores ---")
    jugadores = []
    with open("records.txt", "r") as f:
        next(f)  # Salta la cabecera del archivo
        for i, line in enumerate(f):
            # Solo procesa líneas que contengan el formato esperado
            if " |   " in line:
                nombre, intentos = line.strip().split(" |   ")
                jugadores.append((nombre, int(intentos)))
                print(f"{i + 1} {nombre} - {intentos} intentos")  # Imprime números desde 1
    return jugadores

def elegir_jugador(jugadores):
    while True:
        try:
            opcion = input("\nElige tu nombre (número) o ingresa un nuevo nombre: ")
            if opcion.isdigit():
                opcion = int(opcion)
                if opcion < 1 or opcion > len(jugadores):
                    print("Opción no válida. Elige un número de la lista.")
                    continue
                return jugadores[opcion - 1][0]  # Restamos 1 para ajustar al índice de la lista
            elif opcion.strip() == "":  # No permitir nombres vacíos
                print("El nombre no puede estar vacío.")
                continue
            else:
                return opcion.strip()  # Devuelve el nuevo nombre
        except ValueError:
            print("Por favor, ingresa un número válido o un nombre.")

def juego():
    # Muestra los registros y elige al jugador
    jugadores = mostrar_records()

    nombre = elegir_jugador(jugadores)

    print(f"\n¡Bienvenido, {nombre}! Adivina el número entre 1 y 50.")
    
    numero_secreto = random.randint(1, 50)
    intentos = set()
    
    while True:
        try:
            intento = int(input("Ingresa un número: "))
            if intento < 1 or intento > 50:
                print("Número fuera de rango. Intenta de nuevo.")
                continue
        except ValueError:
            print("Entrada no válida. Ingresa un número.")
            continue

        if intento in intentos:
            print("Ya elegiste ese número, prueba otro.")
            continue
        
        intentos.add(intento)
        
        if intento == numero_secreto:
            print(f"¡Felicidades, {nombre}! Adivinaste el número {numero_secreto}.")
            print(f"Te tomó {len(intentos)} intentos.")
            guardar_record(nombre, intentos)
            break
        else:
            print("Número incorrecto. Intenta de nuevo.")
            if intento > numero_secreto:
                print("Pista: Muy alto.")
            else:
                print("Pista: Muy bajo.")
            imprimir_tabla(intentos)

if __name__ == "__main__":
    while True:
        juego()
        # Opción para jugar de nuevo
        jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
        if jugar_otra_vez.lower() != "s":
            print("¡Gracias por jugar!")
            break