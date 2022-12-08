##ejercicio_2_tema_6_Python
##En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

##imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)
    def resultado(self):
        if self.nota < 5:
            print("El alumno NO Aprobo")
        else:
            print("El alumno ha aprobado")

##Deberéis de definir los métodos para inicializar sus atributos. 
alumno1=Alumno()
alumno2=Alumno()
alumno1.inicializar("Jefferson",7)
alumno2.inicializar("Carlos",3)
alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()   