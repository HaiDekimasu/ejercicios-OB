public class Main {

    public static void main(String[] args) {
        /*
         * 3. Crea ahora un objeto de la clase Cliente que debe tener como propiedades
         * la edad, el telefono, el nombre y el credito, tienes que darles valor y
         * mostrarlas por pantalla.
         */
        /*
         * 4. Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de
         * Persona, y con una variable salario que solo tenga la clase Trabajador.
         */
        Cliente cliente = new Cliente();
        Trabajador trabajador = new Trabajador();
        cliente.nombre = "Jefferson";
        cliente.edad = 32;
        cliente.telefono = 958140151;
        cliente.credito = 200.78;
        System.out.println(
                "Soy: " + cliente.nombre + ", tengo: " + cliente.edad + " años y mi telefono es: " + cliente.telefono
                        + " y mi credito disponible es: " + cliente.credito + "$");
        trabajador.nombre = "carlos";
        trabajador.edad = 25;
        trabajador.telefono = 958140152;
        trabajador.salario = 3000.99;
        System.out.println("Soy: " + trabajador.nombre + ", tengo: " + trabajador.edad + " años y mi telefono es: "
                + trabajador.telefono
                + " y mi salario es de: " + trabajador.salario + "$");

    };
};

/*
 * 1. Crea una clase Persona con las siguientes variables:
 * La edad
 * El nombre
 * El teléfono
 */
class Persona {
    int edad;
    int telefono;
    String nombre;
};

/*
 * 2. Una vez creada la clase, crea una nueva clase Cliente que herede de
 * Persona, esta nueva clase tendrá la variable credito solo para esa clase.
 */
class Cliente extends Persona {
    double credito;
};

/*
 * 4. Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de
 * Persona, y con una variable salario que solo tenga la clase Trabajador.
 */
class Trabajador extends Persona {
    double salario;
};