##EJERCICIO_TEMA_6_PYTHON
##En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:Color,Ruedas,Puertas

class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.puertas, self.color, self.ruedas  )
##Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:Velocidad,Cilindrada
class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Descripcion de Coche: color {},{} ruedas ,{} puertas ,{} km/h , {} cc".format( self.color,self.ruedas ,self.puertas ,self.velocidad , self.cilindrada )

##Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
coche = Coche("ROJO", 4, 4, 240, 2000)
print(coche)