//---------------------------------------
// Una función que obtiene un valor de 
// una propiedad se llama GETTER y una
// que establece el valor de una 
// propiedad se llama SETTER.
//---------------------------------------


// Creamos una CLASE, agregamos METODOS
// DINAMICOS, ESTÁTICOS y agregamos
// GETTERS, que son de "solo lectura" y 
// SETTERS, que son de "solo escritura":


//Declaro clase
class Perro { 
    static contador = 9  //Declaro el valor inicial de la propiedad estática
    constructor(nombre, edad, vivo = true){
        this._nombre = nombre;  //El "_" convierte la propiedad en "solo lectura"
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
    get Nombre() { return this._nombre }  // Sin "get" no podría mostrar el mensaje (probalo!)
    set Nombre(nombre) { this._nombre = nombre }
    get Edad() { return this.edad }
    set Edad(edad) { this.edad = edad }
    get Vivo() { return this.vivo }
    set Vivo(vivo) { this.vivo = vivo }            
}


//INSTANCIAMOS un objeto. Es decir, creamos
//un OBJETO de la CLASE perro:
var perro1 = new Perro ("Tati", 5, true)  

console.log (perro1.nombre) //No puedo acceder a la variable. 

// console.log (perro1.Nombre) //Pero si mediante el getter

// perro1.Nombre="Lassie"      // Le cambio el nombre mediante el setter
// console.log (perro1.Nombre) // Veo el nuevo nombre



