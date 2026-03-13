""" def saludar(nombre, edad, es_estudiante, nacionalidad="Boliviano"):
    print("Bienvenidos a Python: ", nombre)
    print("Edad: ", edad)
    print("Es estudiante: ", es_estudiante)
    print("Nacionalidad: ", nacionalidad)

saludar("Jose Perez", 25, True, "Peruano") """

# C = n! / (r! * (n-r)!)

def calcular_factorial(num):#función para calcular el factorial de un número
    fac = 1
    for i in range(1, num+1, 1):
        fac = fac * i
    return fac

def calcular_formula(n, r):#función para calcular la formula
    valor_n = calcular_factorial(n)
    valor_r = calcular_factorial(r)
    valor_n_r = calcular_factorial(n-r)
    return valor_n // (valor_r * (valor_n_r)) #

def ejecutar():#function que ejecuta el programa
    n = int(input("ingrese valor de N:"))
    r = int(input("ingrese valor de r:"))
    print(calcular_formula(n, r))

ejecutar()





