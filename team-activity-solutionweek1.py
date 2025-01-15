def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def evaluar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
resultado = evaluar_imc(imc)

print("Su IMC es:", imc)
print("Según su IMC, usted se encuentra en:", resultado)