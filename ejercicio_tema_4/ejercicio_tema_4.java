package ejercicio_tema_4;

public class ejercicio_tema_4 {

    public static void main(String[] args) {
        /*
         * 1. Usando un if, crear una condición que compare si la variable numeroIf es
         * positivo, negativo, o 0.
         * Pista: Los números inferiores a 0 son negativos y los superiores, positivos.
         */

        int numeroif = 2;

        if (numeroif < 0) {
            System.out.println("La variable numeroif:" + numeroif + " y es negativo.");
        } else if (numeroif > 0) {
            System.out.println("La variable numeroif:" + numeroif + " y es positivo.");
        } else {
            System.out.println("La variable numeroif es: 0");
        }
        ;
        /*
         * 2. Crea un bucle While, este bucle tendrá que tener como condición que la
         * variable numeroWhile sea inferior a 3, el bloque de código que tendrá el
         * bucle deberá:
         * Incrementar el valor de la variable en uno cada vez que se ejecute
         * Mostrarlo por pantalla cada vez que se ejecute.
         */

        int numerowhile = 1;

        while (numerowhile < 3) {
            numerowhile++;
            System.out.println("La variable numerowhile ahora vale: " + numerowhile);
        }
        ;

        /*
         * 3. Para el bucle Do While, deberás crear la misma estructura que en el While,
         * pero solo se debe ejecutar una vez.
         */

        int numerodowhile = 0;
        do {
            numerodowhile++;
            System.out.println("La variable numerodowhile ahora vale: " + numerodowhile);
        } while (numerodowhile < 3);

        /*
         * 4. Para el bucle For, crea una variable numeroFor, esta variable tendrá como
         * valor 0 y su condición será que la variable sea igual o menor que 3, se irá
         * incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por
         * pantalla.
         */

        for (int numerofor = 0; numerofor <= 3; numerofor++) {
            System.out.println("La variable numerofor ahora vale: " + numerofor);
        }

        /*
         * 5. Por último, para el Switch, deberás crear la variable estacion, y
         * distintos case para las cuatro estaciones del año. Dependiendo del valor de
         * la variable estacion se deberá mandar un mensaje por consola informando de la
         * estación en la que está. También habrá que poner un default para cuando el
         * valor de la variable no sea una estación.
         */

        String estacion = "invierno";
        switch (estacion) {
            case "verano":
                System.out.println("Estamos en verano");
                break;
            case "primavera":
                System.out.println("Estamos en primavera");
                break;
            case "otoño":
                System.out.println("Estamos en otoño");
                break;
            case "invierno":
                System.out.println("Estamos en invierno");
                break;
            default:
                System.out.println("No es una estación");
        }
        ;
    };
};