//---------------------------------------
// Una función que obtiene un valor de 
// una propiedad se llama GETTER y una
// que establece el valor de una 
// propiedad se llama SETTER.
//---------------------------------------
// Mas datos:
// https://desarrolloweb.com/articulos/static-clases-javascript-es6.html

// Creamos una CLASE, agregamos METODOS
// DINAMICOS, ESTÁTICOS y agregamos
// GETTER y SETTER.
// Las propiedades o métodos creadas de esta
// manera (static) no pertenen al objeto, 
// sino a la clase.
//---------------------------------------


//Declaro clase
class Perro { 
    static contador = 0  //Declaro el valor inicial de la propiedad estática
    constructor(nombre, edad, vivo = true){
        this.nombre = nombre;
        this.edad = edad;
        this.vivo = vivo;
        Perro.contador++;  // Se antepone el nombre de la clase
    }
    static presentacionPerro(){
        return "Soy un método de clase, no de cada objeto. [" + this.contador + "] <br>"
    }

    //Metodos
    ladrar() { return "Guau!" }
    presentar() { return "Soy " + this.nombre + " y tengo " + this.edad +" años. <br>" }
}
// Fin de la declaracion de la clase


//INSTANCIAMOS un objeto. Es decir, creamos
//un OBJETO de la CLASE perro:
const perro1 = new Perro("Juan", 3 )
console.log(Perro.presentacionPerro())
console.log(perro1.presentar())


//---------------------------------------------
//Los métodos estáticos se ejecutan
// directamente sobre la clase
//---------------------------------------------