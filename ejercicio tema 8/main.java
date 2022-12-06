public class main {
    public static void main(String[] args) {

/* 4. Crear un objeto persona en el main. */
/* 5. Utiliza los gets y sets para darle valores a las propiedades edad, nombre
      y telefono, por último muéstralas por consola.*/
        
        Persona persona = new Persona();
        persona.setNombre("Jefferson");
        System.out.println("Mi nombre es " + persona.getNombre());
        persona.setEdad(32);
        System.out.println("Tengo " + persona.getEdad() + " años");
        persona.setTelefono(958140151);
        System.out.println("Mi teléfono es " + persona.getTelefono());
    };
};

/* 1. Crear clase Persona. */
class Persona {
/* 2. Crear variables las privadas edad, nombre y telefono de la clase Persona.*/
    private String nombre;
    private int edad;
    private int telefono;
/* 3. Crear gets y sets de cada propiedad. */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    };

    public String getNombre() {
        return nombre;
    };

    public void setEdad(int edad) {
        this.edad = edad;
    };

    public int getEdad() {
        return edad;
    };

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    };

    public int getTelefono() {
        return telefono;
    };
};
