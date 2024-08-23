"""
4-Se requiere un programa para calcular el promedio final de los estudiantes.
Cada estudiante tiene un nombre, código y tres calificaciones. El programa
debe calcular el promedio de las tres calificaciones y determinar si el
estudiante aprueba o reprueba (se aprueba con un promedio mayor o igual a
60). Las notas tienen los siguientes valores: Laboratorio 1 (30%), Laboratorio 2
(30%) y Parcial (40%)
"""
class Estudiante():
    def __init__(self):
        self.nombre = ""
        self.codigo = ""
        self.laboratorio1 = 0.0
        self.laboratorio2 = 0.0
        self.parcial = 0.0
        self.promedio = 0.0

    def registrar_estudiante(self):
        print("__Registro de Estudiante__")
        self.nombre = input("Ingrese el nombre del estudiante: ")
        self.codigo = input("Ingrese el código del estudiante: ")
        self.laboratorio1 = float(input("Ingrese la nota del Laboratorio 1 (30%): "))
        self.laboratorio2 = float(input("Ingrese la nota del Laboratorio 2 (30%): "))
        self.parcial = float(input("Ingrese la nota del Parcial (40%): "))

    def calcular_promedio(self):
        # Calcular el promedio ponderado
        self.promedio = (self.laboratorio1 * 0.3) + (self.laboratorio2 * 0.3) + (self.parcial * 0.4)

    def mostrar_resultado(self):
        print(f"\n__Resultado del Estudiante__")
        print(f"Nombre: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Laboratorio 1: {self.laboratorio1}")
        print(f"Laboratorio 2: {self.laboratorio2}")
        print(f"Parcial: {self.parcial}")
        print(f"Promedio: {self.promedio:.2f}")
        
        if self.promedio >= 60:
            print("Estado: Aprobado")
        else:
            print("Estado: Reprobado")
            print("___________________________________")

    def procesar_estudiante(self):
        self.registrar_estudiante()
        self.calcular_promedio()
        self.mostrar_resultado()


# Creación de una instancia
estudiante1 = Estudiante()
estudiante1.procesar_estudiante()

