public class Suma {
    public static void main(String[] args) {
        int a = 5;
        int b = 10;
        int c = 20;

        /* 2.Llamar a la función en el main y darle valores. */
        System.out.println("El resultado de la Suma de a+b+c es:" + sumar(a, b, c));
    };

    /*
     * 1.Crear una función con tres parámetros que sean números que se suman entre
     * sí.
     */
    public static int sumar(int a, int b, int c) {
        return a + b + c;
    }
};
