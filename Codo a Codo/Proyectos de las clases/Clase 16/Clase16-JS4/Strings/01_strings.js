// En este script vamos a analizar las
// principales propiedades de los objetos 
// string.
// Excelente información aqui:
// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String
//----------------------------------------


// Creacion:
//                       1111111
//             01234567890123456
var cadena1 = "Método mas simple"
var cadena2 = new String ("Usando un constructor")

//----------------------------------------
// La propiedad .lenght nos proporciona 
// el número de caracteres que contiene 
// el string:

// document.write(cadena1.length , "<br>")
// document.write(cadena2.length , "<br>")

//----------------------------------------
// La propiedad .charAt nos devuelve el 
// caracter ubicado en una posición: 

// document.write(cadena1.charAt(3) , "<br>")
// document.write(cadena1.charAt(0) , "<br>")

//----------------------------------------
// La propiedad .concat une un string al  
// final del actual:

// document.write(cadena1.concat(" de crear una cadena") , "<br>")

//----------------------------------------
// La propiedad .indexOf(str, from) nos   
// devuelve la primera posicion en que srt
// aparece en la cadena:

// document.write(cadena1.indexOf("t") , "<br>")
// document.write(cadena1.indexOf("M") , "<br>")
// document.write(cadena1.indexOf("m") , "<br>")
// document.write(cadena1.indexOf("m", 10) , "<br>")

//----------------------------------------
// La propiedad .lastIndexOf(str, from) es
// similar pero contando desde el final.

// document.write(cadena1.lastIndexOf("m") , "<br>")
// document.write(cadena1.lastIndexOf("m", 10) , "<br>")

//----------------------------------------
// La propiedad .repeat(n) devuelve la 
// cadena repetida "n" veces:

// document.write("Hola! ".repeat(3) , "<br>")
// document.write("-".repeat(30) , "<br>")

//----------------------------------------
// .toLowerCase() y .toUpperCase() 
// convierten una cadena a minúsculas
// y mayúsculas respectivamente:

// document.write(cadena1               , "<br>")
// document.write(cadena1.toLowerCase() , "<br>")
// document.write(cadena1.toUpperCase() , "<br>")

//----------------------------------------
// .trim() elimina espacios a derecha e
// izquierda:

// var cadena = "    texto    "
// console.log("[" + cadena + "]")
// console.log("[" + cadena.trim() + "]")


//----------------------------------------
// .replace(str, newstr) reemplaza la 
// primera aparición del texto str por 
// newstr:

// var cadena = "El color del auto es azul"
// document.write(cadena, "<br>")
// document.write(cadena.replace("azul", "rojo")  , "<br>")

//----------------------------------------
// .substr(ini, len) devuelve el subtexto 
// desde la posición ini hasta ini+len.
//            0123456789012345678901234 
// var cadena = "Esta es una bonita cadena"
// document.write(cadena, "<br>")
// document.write(cadena.substr(12, 6)  , "<br>")

//----------------------------------------
// .substring(ini, end) devuelve el subtexto 
// desde la posición ini hasta end.
//            0123456789012345678901234 
// var cadena = "Esta es una bonita cadena"
// document.write(cadena, "<br>")
// document.write(cadena.substring(5,11)  , "<br>")


