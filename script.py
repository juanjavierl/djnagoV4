#from funciones import calcular_factorial

#print("El factorial es: ",calcular_factorial(5))

""" import math

print(math.factorial(5)) """


import requests

# URL de la API
url = "https://jsonplaceholder.typicode.com/users"

# hacer la petición
respuesta = requests.get(url)


# convertir a JSON
usuarios = respuesta.json()

#print(usuarios) #imprime la lista de usuarios obtenida de la API
# recorrer usuarios
for user in usuarios:
    print("ID:", user["id"])
    print("Nombre:", user["name"])
    print("Email:", user["email"])
    print("ciudad", user["address"]["city"])
    print("-" * 30) 
