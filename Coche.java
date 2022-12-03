public class Coche {/* 1.Crear una clase coche. */

    /*
     * 2.Dentro de la clase coche, una variable numérica que almacene el número de
     * puertas que tiene.
     */
    int numeroP = 0;

    Coche() {

    };

    /* 3.Una función que incremente el número de puertas que tiene el coche. */
    public void agregarP() {
        numeroP++;
    };

    /* 5.Mostrar el número de puertas que tiene el objeto. */
    public void mostrarP() {
        System.out.println("la cantidad de puertas es: " + numeroP);
    }
};
