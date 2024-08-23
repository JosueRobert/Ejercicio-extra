"""
3-Un cine requiere un programa que permita registrar datos de los clientes
que atienden a las funciones como cantidad de boletos, el título de la película,
la hora de la función, el tipo de función, y el número de sala. El programa debe
mostrar el total del cliente dependiendo de la cantidad de boletos que
compró y si es miércoles tiene un descuento del 2x1.
"""
class Cine:
    def __init__(self):
        self.nombrecliente = ""
        self.titulo = ""
        self.hora = ""
        self.tipo_funcion = ""
        self.num_sala = 0
        self.cantidad_boletos = 0
        self.precio_boleto = 5.00
        self.total = 0
        self.es_miercoles = False

    def registrar_datos(self):
        self.nombrecliente = input("Ingrese su nombre: ")
        self.titulo = input("Título de la película: ")
        self.hora = input("Hora de la función: ")
        self.tipo_funcion = input("Tipo de función (2D/3D): ").lower()
        self.num_sala = int(input("Número de sala: "))
        self.cantidad_boletos = int(input("Cantidad de boletos: "))
        dia = input("¿Es miércoles? (S/N): ").lower()
        self.es_miercoles = dia == "s"

    def calculartotal(self):
        if self.es_miercoles:
            boletos_a_pagar = (self.cantidad_boletos + 1) // 2 
            self.total = boletos_a_pagar * self.precio_boleto
        else:
            self.total = self.cantidad_boletos * self.precio_boleto
        print(f"El total a pagar por {self.cantidad_boletos} boletos es: ${self.total:.2f}")

    def mostrarfactura(self):
        print("____Factura____")
        print(f"Nombre del cliente: {self.nombrecliente}")
        print(f"Título: {self.titulo}")
        print(f"Hora: {self.hora}")
        print(f"Tipo de función: {self.tipo_funcion}")
        print(f"Número de sala: {self.num_sala}")
        print(f"Cantidad de boletos: {self.cantidad_boletos}")
        print(f"Total a pagar: ${self.total:.2f}")

    def realizarcompra(self):
        self.registrar_datos()
        self.calculartotal()
        self.mostrarfactura()

# Creación de una instancia
compra1 = Cine()
compra1.realizarcompra()
