import string 
import pickle
import os

archivo = os.path.join(os.getcwd(), "Alumno.pkl")

class Alumno:
    nombre: str
    edad: int
    genero: str
    def llenar(self):
        self.nombre = input("Nombre: ")
        self.edad = int(input("Edad: "))
    def imprimir(self):
        print("Nombre: " + self.nombre + "\nEdad: " + str(self.edad))
    def guardar(self, ruta):
        with open(ruta, "wb") as f:
            pickle.dump(self, f)
    def leer(self, ruta):
        if not os.path.exists(ruta):
            return Alumno()
        with open(ruta, "rb") as f:
            return pickle.load(f)

alumno = Alumno()
alumno.llenar()

alumno.guardar(archivo)
result = alumno.leer(archivo)
print(result.nombre)
print(result.edad)




















def esmayor(edad):
    #edad es mayor o igual a 18?
    return edad >= 18

def mayusculas(nombre):
    return nombre.upper()

def iniciales(nombres):
    iniciales = []
    palabras = nombres.split()
    for palabra in palabras:
        iniciales.append(palabra[0])
    return ''.join(iniciales)


#nombres = ["asasas","asadad","asadasd"]
#nombre1 = "aldo"
#nombre = input("Nombre: ")
#print(iniciales(mayusculas(nombre)))
# *******************************

#nombre = input("dime tu nombre chico: ")
#edad = int(input("cual es tu edad: "))

#if esmayor(edad):
#    print("eres mayor de edad")
#else:
#    print("FBI open up!")

