# Importamos el framework Flask
from flask import Flask 

# Importamos la función que nos permit el render de los templates
from flask import render_template 

# Creamos la aplicación
app = Flask(__name__) 

# Proporcionamos la ruta a la raiz del sitio
@app.route('/') 
def index():
    # Devolvemos código HTML para ser renderizado
    return "<h1>Hola Codo a Codo!</h1>Todo a salido bien." 

# Estas lìneas de código las requiere python para que 
# se pueda empezar a trabajar con la aplicación
if __name__=='__main__':
    #Corremos la aplicación en modo debug
    app.run(debug=True) 