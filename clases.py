""" class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
obj1 = Persona("Jose Perez", 30)
print(obj1.saludar()) """

class operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No se puede dividir por cero"
        
obj2 = operaciones(10, 5)
print("Suma: ", obj2.suma())
print("Resta: ", obj2.resta())