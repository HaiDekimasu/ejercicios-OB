##En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
file = open('archivo.txt', 'w')
file.write('¡creado archivo!\n')
file.close()

file = open('archivo.txt', 'r+')
file.readline()
file.write('segunda apertura de archivo.\n')

file.seek(0)
print(file.read())
file.close()