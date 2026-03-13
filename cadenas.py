nombre = "Jose Perez"

#print(nombre[:].count("e")) # 1

""" for letra in nombre:
    print(letra, end="") """

for letra in range(0, len(nombre),1):
    print(nombre[letra].upper(), end="")