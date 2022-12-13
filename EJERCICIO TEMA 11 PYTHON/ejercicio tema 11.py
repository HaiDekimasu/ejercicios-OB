##crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto. Una vez creada la tabla, tienen que insertarle datos, como mínimo tienen que insertar 8 alumnos a la tabla. Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola
import sqlite3

db_connection = sqlite3.connect('ejercicio.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'Jefferson', 'Cadevilla')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Carlos', 'Medina')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Jose', 'Lopez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'Carolina', 'Melendi')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Leonel', 'Messi')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Cristiano', 'Ronaldo')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'Roberto', 'Carlos')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'Iker', 'Casillas')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Jefferson'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()


