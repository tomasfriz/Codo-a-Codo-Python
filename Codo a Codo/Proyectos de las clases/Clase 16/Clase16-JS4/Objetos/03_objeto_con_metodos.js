// Creamos una CLASE, y agregamos un METODO
// (una función que "vive" dentro del objeto)
// que le permite ladrar() a nuestros perros:

class Perro {
    constructor( nombre, edad, vivo){  
       this.nombre = nombre
       this.edad   = edad
       this.vivo   = vivo
   }

   // ladrar() { return "guau!" }
   ladrar() { return this.nombre + " dice guau!"}
}


//INSTANCIAMOS un objeto. Es decir, creamos
//un OBJETO de la CLASE perro:
var perro1 = new Perro ("Tati", 5, true)

console.log (perro1)

// Utilizamos el METODO ladrar():
console.log (perro1.ladrar())


// Intenta crear el METODO "quienSoy()"
// que devuelva "Soy" + nombre

// Intenta agregar un METODO que nos permita
// obtener un mensaje del tipo "Toby tiene 5 años"
// y "Toby está vivo / muerto"