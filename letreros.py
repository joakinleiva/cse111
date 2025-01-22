import math
# Programa para calcular la cantidad de tiras de metal necesarias y sus cortes

# Longitud de una tira de metal en cm
LARGO_TIRA_METAL = 600
# Grosor de la tira de metal en cm
GROSOR_TIRA_METAL = 2

# Solicitar dimensiones al usuario
ancho = int(input("Ingrese el ancho del letrero en cm: "))
alto = int(input("Ingrese el alto del letrero en cm: "))

# Calcular los cortes considerando el grosor
cortes_horizontal = 2 * [ancho]  # Dos cortes del ancho total
cortes_vertical = 2 * [alto - 2 * GROSOR_TIRA_METAL]  # Dos cortes del alto ajustado

# Combinar todos los cortes
cortes = cortes_horizontal + cortes_vertical

# Calcular la cantidad total de material necesario
material_necesario = sum(cortes)

# Calcular la cantidad de tiras necesarias (redondeo hacia arriba)
cantidad_tiras = -(-material_necesario // LARGO_TIRA_METAL)  # División entera hacia arriba

# Función para calcular los sobrantes por tira
def calcular_sobrantes(cortes, largo_tira):
    sobrantes = []
    largo_restante = largo_tira
    for corte in cortes:
        if corte <= largo_restante:
            largo_restante -= corte
        else:
            sobrantes.append(largo_restante)
            largo_restante = largo_tira - corte
    sobrantes.append(largo_restante)  # Sobrante de la última tira
    return sobrantes

# Calcular los sobrantes
sobrantes = calcular_sobrantes(cortes, LARGO_TIRA_METAL)

# Resultados
print(f"\nPara un letrero de {ancho} cm x {alto} cm:")
print(f"- Se necesitan {cantidad_tiras} tiras completas de metal.")
print("- Cortes requeridos:")
for i, corte in enumerate(cortes, start=1):
    print(f"  Corte {i}: {corte} cm")

print("- Sobrantes por tira:")
for i, sobrante in enumerate(sobrantes, start=1):
    print(f"  Tira {i}: {sobrante} cm sobrantes")



def calcular_diagonal(x,y):
    
    # Calcular la diagonal
    diagonal = math.sqrt(x**2 + y**2)
    
    # Imprimir el resultado
    print(f"La diagonal del rectángulo es: {diagonal:.2f} cm")

# Llamar a la función
calcular_diagonal(ancho, alto)
