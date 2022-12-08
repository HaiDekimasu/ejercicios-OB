# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
from operaciones import * 

a, b, c, d = (2, 4, 6, 10)

print( "{} + {} = {}".format(a, b, Suma(a, b) ) )
print( "{} - {} = {}".format(b, d, Resta(b, d) ) )
print( "{} * {} = {}".format(b, c, Multiplicar(b, c) ) ) 
print( "{} / {} = {}".format(d, a, Division(d, a) ) )