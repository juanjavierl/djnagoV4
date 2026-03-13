""" mi_tupla = (1, 2, "tres", 4, 5, 10, 20, 30, 40, 50)
print(mi_tupla[20]) """ #tres
""" for elemento in range(0, len(mi_tupla), 1):
    print(mi_tupla[elemento], end=" ") """

""" for elemento in mi_tupla:
    print(elemento, end=" ") """

#maneje de listas 
mi_lista = [1, 2, 0, 4, 5, 8, 4, 30, 40, 50]
""" 
for elemento in mi_lista:
    if elemento == 0:
        elemento = 100
    print(elemento, end=" ") """

""" mi_lista.append(10) #agrega un nuevo elemento al final de la lista
print(mi_lista) #tres
print(mi_lista.count(4))

l = mi_lista.sort()
print(l) """

#manejo de diccionarios
mi_diccionario = {"nombre": "jose", "apellido": "perez", "edad": 30, "ciudad": "Cochabamba"}
#print(mi_diccionario["nombre"], mi_diccionario["apellido"]) #dict

for clave, valor in mi_diccionario.items():
    #print(valor, ": ", mi_diccionario[valor]) #nombre apellido edad ciudad
    print(clave, ": ", valor) #nombre : jose apellido : perez edad : 30 ciudad : Cochabamba