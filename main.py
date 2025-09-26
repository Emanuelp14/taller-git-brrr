# Equipo: brrrr
# Descripción: Proyecto de prueba para practicar Git y GitHub.
# Contiene funciones básicas de operaciones matemáticas simples.

# Función de suma
def suma(a, b):
    return a + b

# Función de resta
def resta(a, b):
    return a - b

#funcion de multiplicar
def multiplicar(a, b):
    return a * b

# Función potencia
def potencia(a, b):
    return a ** b

# Función de dividir 
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división entre cero"

# Función módulo
def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: división entre cero"


# Bloque principal
if __name__ == "__main__":
    print("Suma 3 + 5 =", suma(3, 5))
    print("Resta 10 - 4 =", resta(10, 4))
    print("5 * 3 =", multiplicar(5, 3))
    print("2 ** 3 =", potencia(2, 3))
    print("División 20 / 5 =", dividir(20, 5))
    print("10 % 3 =", modulo(10, 3))
