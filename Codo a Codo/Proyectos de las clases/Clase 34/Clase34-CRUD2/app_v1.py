#--------------------------------------------------------------------
# Importamos el framework Flask
from flask import Flask 

# Importamos la función que nos permit el render de los templates
from flask import render_template 

# Importamos el módulo que permite conectarnos a la BS
from flaskext.mysql import MySQL
#--------------------------------------------------------------------


# Creamos la aplicación
app = Flask(__name__) 

#--------------------------------------------------------------------
# Creamos la conexión con la base de datos:
mysql = MySQL()
# Creamos la referencia al host, para que se conecte a la base
# de datos MYSQL utilizamos el host localhost
app.config['MYSQL_DATABASE_HOST']='localhost' 
# Si no tengo el puerto por defecto, lo cambio
#app.config['MYSQL_DATABASE_PORT']=3366
# Indicamos el usuario, por defecto es user
app.config['MYSQL_DATABASE_USER']='root' 
# Sin contraseña, se puede omitir
app.config['MYSQL_DATABASE_PASSWORD']='' 
# Nombre de nuestra BD
app.config['MYSQL_DATABASE_BD']='sistema' 
# Creamos la conexión con los datos
mysql.init_app(app) 
#--------------------------------------------------------------------


# Proporcionamos la ruta a la raiz del sitio
@app.route('/') 
def index():
    # Devolvemos código HTML para ser renderizado
    return render_template('empleados/index.html')

#--------------------------------------------------------------------
# Estas líneas de código las requiere python para que 
# se pueda empezar a trabajar con la aplicación
if __name__=='__main__':
    #Corremos la aplicación en modo debug
    app.run(debug=True) 
#--------------------------------------------------------------------