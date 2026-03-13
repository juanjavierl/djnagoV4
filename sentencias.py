
""" print("En el Ñágara encontré un Ñandú")
nombre = input("¿Cómo se llama? ") 
print("Hola como estas ", nombre) 
comentarios """

#sentencia if
    

""" edad = int(input("¿Cuántos años tienes? "))
if (edad >= 18):
    print("Eres mayor de edad")
    print("Puedes votar")
else:
    print("No eres mayor de edad") """

# determinar si un año es bisiesto o no
""" anio = int(input("Ingrese un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto") """


#setnecia while
""" contador = 0
while contador < 5:
    contador = contador + 1
    print("Contador: ", contador) """


""" suma=0
n=int(input("Número positivo:"))
while n!=0:
    digito=n%10
    suma+=digito
    n=n//10
    print("Dígito:", digito)
print("Suma de los dígitos:", suma) """

#sentencia for n-1

""" for i in range(10, -1, -1):
    if i == 5:
        continue
    print("Número: ", i)  """


# n = 5  proceso de factorial 5*4*3*2*1 = 120 
factorial = 1
try:
    n = int(input("Ingrese un número para calcular su factorial: "))
    for i in range(1, n + 1):
        factorial = factorial * i
    print("El factorial de", n, "es:", factorial)
except:
    print("Por favor, ingrese un número entero válido >1.")

