#--------------------------------------------------------------------
# Importamos el framework Flask
from flask import Flask 

# Importamos la función que nos permit el render de los templates,
# recibir datos del form, redireccionar, etc.
from flask import render_template, request,redirect

# Importamos el módulo que permite conectarnos a la BS
from flaskext.mysql import MySQL

# Importamos las funciones relativas a fecha y hora
from datetime import datetime
#--------------------------------------------------------------------


# Creamos la aplicación
app = Flask(__name__) 

#--------------------------------------------------------------------
# Creamos la conexión con la base de datos:
mysql = MySQL()
# Creamos la referencia al host, para que se conecte a la base
# de datos MYSQL utilizamos el host localhost
app.config['MYSQL_DATABASE_HOST']='localhost' 
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
    # Creamos una variable que va a contener la consulta sql:
    sql = "SELECT * FROM `sistema`.`empleados`;"    
    # Nos conectamos a la base de datos 
    conn = mysql.connect()    
    # Sobre el cursor vamos a realizar las operaciones
    cursor = conn.cursor()     
    # Ejecutamos la sentencia SQL sobre el cursor
    cursor.execute(sql)     
    # Copiamos el contenido del cursor a una variable
    db_empleados = cursor.fetchall()
    # "Commiteamos" (Cerramos la conexión)
    conn.commit()     
    # Devolvemos código HTML para ser renderizado
    return render_template('empleados/index_v7.html', empleados = db_empleados)

#--------------------------------------------------------------------
# Función para eliminar un registro
@app.route('/destroy/<int:id>')
def destroy(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM `sistema`.`empleados` WHERE id=%s", (id))
    conn.commit()
    return redirect('/')

#--------------------------------------------------------------------
# Función para editar un registro
@app.route('/edit/<int:id>')
def edit(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `sistema`.`empleados` WHERE id=%s", (id))
    empleados=cursor.fetchall()
    conn.commit()
    return render_template('empleados/edit.html', empleados=empleados)

#--------------------------------------------------------------------
# Función para actualizar los datos de un registro
@app.route('/update', methods=['POST'])
def update():
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']
    id=request.form['txtID']
    sql = "UPDATE `sistema`.`empleados` SET `nombre`=%s, `correo`=%s WHERE id=%s;"
    datos=(_nombre,_correo,id)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/')





#--------------------------------------------------------------------
# Función para crear un registro nuevo.
@app.route('/create')
def create():
    return render_template('empleados/create.html')

#--------------------------------------------------------------------
#Función para almacenar los datos de un usuario.
@app.route('/store', methods=['POST'])
def storage():
    # Recibimos los valores del formulario y los pasamos a variables locales:
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']
    
    # Guardamos en now los datos de fecha y hora
    now = datetime.now()
    
    # Y en tiempo almacenamos una cadena con esos datos
    tiempo = now.strftime("%Y%H%M%S") 
    
    #Si el nombre de la foto ha sido proporcionado en el form...
    if _foto.filename!='':
        #...le cambiamos el nombre.
        nuevoNombreFoto=tiempo+_foto.filename 
        # Guardamos la foto en la carpeta uploads.
        _foto.save("uploads/"+nuevoNombreFoto)
    
    # Y armamos una tupla con esos valores:
    datos = (_nombre,_correo, nuevoNombreFoto)
        
    # Armamos la sentencia SQL que va a almacenar estos datos en la DB:
    sql = "INSERT INTO `sistema`.`empleados` \
          (`id`, `nombre`, `correo`, `foto`) \
          VALUES (NULL, %s, %s, %s);"

    conn = mysql.connect()     # Nos conectamos a la base de datos 
    cursor = conn.cursor()     # En cursor vamos a realizar las operaciones
    cursor.execute(sql, datos) # Ejecutamos la sentencia SQL en el cursor
    conn.commit()              # Hacemos el commit
    return render_template('empleados/index.html') # Volvemos a index.html




#--------------------------------------------------------------------
# Estas líneas de código las requiere python para que 
# se pueda empezar a trabajar con la aplicación
if __name__=='__main__':
    #Corremos la aplicación en modo debug
    app.run(debug=True) 
#--------------------------------------------------------------------