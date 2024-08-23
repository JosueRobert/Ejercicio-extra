"""
2-Una empresa se dedica a rentar bicicletas para dar paseos en la ciudad. Las
bicicletas pueden ser deportivas o tradicionales. Se requiere un programa que
permita registrar los datos principales del cliente que renta y por cuánto
tiempo en horas. También determine el costo de renta según el tipo de
bicicleta: las deportivas tienen un costo de renta más alto (precio base
multiplicado por 1.5). 
"""

class RentaBicicletas():
    def __init__(self):
        self.nombre_cliente = ""
        self.tipobicicleta = ""
        self.tiemporenta = 0  
        self.precio_base = 10.0  
        self.costo_total = 0.0

    def registrar_cliente(self):
        print("__Bienvenido a Renta de Bicicletas__")
        self.nombrecliente = input("Ingrese su nombre: ")
        self.tipo_bicicleta = input("¿Qué tipo de bicicleta desea rentar? (tradicional/deportiva): ").lower()
        self.tiemporenta = int(input("¿Cuántas horas desea rentar?: "))

    def calcular_costo(self):
        if self.tipo_bicicleta == "tradicional":
            self.costo_total = self.precio_base * self.tiemporenta
        elif self.tipo_bicicleta == "deportiva":
            self.costo_total = (self.precio_base * 1.5) * self.tiemporenta
        else:
            print("Tipo de bicicleta desconocido. No se puede calcular el costo.")

    def mostrar_factura(self):
        print(f"\n__Factura de la Renta__")
        print(f"El Nombre del cliente: {self.nombre_cliente}")
        print(f"El tipo de bicicleta: {self.tipo_bicicleta.capitalize()}")
        print(f"El tiempo de renta: {self.tiemporenta} horas")
        print(f"El Costo total: ${round(self.costo_total, 2)}")

    def realizar_renta(self):
        self.registrar_cliente()
        self.calcular_costo()
        self.mostrar_factura()


# Creación de una instancia
renta1 = RentaBicicletas()
renta1.realizar_renta()