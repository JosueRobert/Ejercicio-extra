"""
1-Un restaurante vende únicamente hamburguesas y gaseosas. Las
hamburguesas pueden ser de carne de res o de pollo, y las gaseosas pueden
ser de tamaño pequeño o grande. Se requiere un programa que registre las
ordenes de un cliente el cual lleva descrito cuántos productos lleva y su total
además de pedir con cuánto va a pagar y darle su cambio respectivo.
"""
class Resta():
    def _init_(self):
        self.Hamb = ""
        self.Soda = ""
        self.Cantidadhamb = 0
        self.Cantidadsoda = 0
        self.PrecioVenta = 0
        self.Preciosoda = 0
        self.Ganancia = 0
        self.Ordenhamb = ""
        self.Ordensoda = ""
        self.Cambio = 0
        self.mepagan = 0
        self.Llevashamb = ""
        self.Llevassoda = ""

    def TipoHamb(self):
        if self.Hamb == "res":
            self.PrecioVenta = round((self.Cantidadhamb * 4.50) * 1.30, 2)
            print(f"Llevas {self.Cantidadhamb} Hamburguesa de Res y su precio es {self.PrecioVenta}")
            print("Marca AFK")
        elif self.Hamb == "pollo":
            self.PrecioVenta = round((self.Cantidadhamb * 4.75) * 1.30, 2)
            print(f"Llevas {self.Cantidadhamb} Hamburguesa de Pollo y su precio es {self.PrecioVenta}")
            print("Marca AFK")
        else:
            print("Opción desconocida")

    def TipoSoda(self):
        if self.Soda == "grande":
            self.Preciosoda = round((self.Cantidadsoda * 2.50) * 1.30, 2)
            print(f"Llevas {self.Cantidadsoda} Sodas grandes y su precio es {self.Preciosoda}")
            print("Marca Pepsi")
        elif self.Soda == "pequeño":
            self.Preciosoda = round((self.Cantidadsoda * 1.25) * 1.30, 2)
            print(f"Llevas {self.Cantidadsoda} Sodas pequeñas y su precio es {self.Preciosoda}")
            print("Marca Pepsi")
        else:
            print("Opción desconocida")

    def Factura(self):
        self.Registrarpedidos()
        self.TipoHamb()
        self.TipoSoda()
        total = round(self.PrecioVenta + self.Preciosoda, 2)
        print(f"El total de tu compra es: {total}")
        self.mepagan = float(input("¿Con cuánto va a pagar?: "))
        self.Vuelto()

    def Registrarpedidos(self):
        print("__Bienvenido a AFK__")
        self.Llevashamb = input("¿Llevarás Hamburguesas? (S/N): ").lower()
        if self.Llevashamb == "s":
            self.Hamb = input("¿De qué tipo? (res/pollo): ").lower()
            self.Cantidadhamb = int(input("¿Cuántas llevas?: "))
        else:
            print("No tenemos hamburguesas.")

        print("____")
        self.Llevassoda = input("¿Llevarás Soda? (S/N): ").lower()
        if self.Llevassoda == "s":
            self.Soda = input("¿Tamaño? (grande/pequeño): ").lower()
            self.Cantidadsoda = int(input("¿Cuántas llevas?: "))
        else:
            print("No tenemos soda.")

    def Vuelto(self):
        total = round(self.PrecioVenta + self.Preciosoda, 2)
        if self.mepagan >= total:
            self.Cambio = round(self.mepagan - total, 2)
            print(f"Tu cambio es: {self.Cambio}")
        else:
            print(f"Faltan {round(total - self.mepagan, 2)} para completar el pago.")

    def MostrarDatosCompras(self):
        print("_Bienvenido a AFK__")
        if self.Llevashamb == "s":
            self.TipoHamb()
        else:
            print("No has comprado hamburguesas.")

        print("_____")
        if self.Llevassoda == "s":
            self.TipoSoda()
        else:
            print("No has comprado sodas.")

        print("_____")
        print(f"Total a pagar: {round(self.PrecioVenta + self.Preciosoda, 2)}")
        print(f"Pago recibido: {self.mepagan}")
        print(f"Cambio: {self.Cambio}")


# Creación de una instancia
Compra1 = Resta()
print("________________________")
Compra1.Factura()
print("______________________")
Compra1.MostrarDatosCompras()
print("_______________________")