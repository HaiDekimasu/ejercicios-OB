##EJERCICIO_TEMA_5_PYTHON
##Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def anobisiesto():
  ano: int = int(input("Introduce un año y vamos a ver si es bisiesto... "))

  if(ano % 4 == 0):
      return(f"¡El año {ano} es bisiesto!")
  else:
      return(f"Lo sentimos. El año {ano} NO es bisiesto!");

print(anobisiesto());
