from flask import Flask, redirect,render_template,request,send_from_directory
from flaskext.mysql import MySQL
from clases import Clases
from  modificacion import Eliminar
from datetime import datetime
import hashlib
proyecto =  Flask(__name__)
mysql = MySQL()
proyecto.config['MYSQL_DATABASE_HOST'] = 'localhost'
proyecto.config['MYSQL_DATABASE_PORT'] = 3306
proyecto.config['MYSQL_DATABASE_USER'] = 'root'
proyecto.config['MYSQL_DATABASE_PASSWORD'] = ''
proyecto.config['MYSQL_DATABASE_DB'] = 'taller_velasco'
mysql.init_app(proyecto)
misClientes = Clases(mysql)
misModificaciones = Eliminar(mysql)



@proyecto.route('/')
def index():
    resultado = misClientes.consultar()
    return render_template("index.html",res=resultado)

@proyecto.route("/agregarpersonas")
def agregarpersonas():
    return render_template("agregar_persona.html",msg="")


@proyecto.route("/agregarpersonas",methods=['POST'])
def guardapersonas():
    id = request.form['id']
    nombre = request.form['nombre']
    estatura = request.form['estatura']
    peso = request.form['peso']
    fecha = request.form['fecha']
    contrasena = request.form['contrasena']
    cifrada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()
    contrasena = cifrada
    if misClientes.buscar(id):
        return render_template("agregar_persona.html",msg="Id de usuario ya existente")
    misClientes.agregar([id,nombre,estatura,peso,fecha,cifrada])
    return redirect("/")



@proyecto.route('/borrarpersonas/<id>')
def borrarpersonas(id):
    fecha_eliminacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = f"SELECT nombre FROM usuarios WHERE id={id}"
    misModificaciones.cursor.execute(sql)
    resultado = misModificaciones.cursor.fetchone()  
    if resultado:
        nombre = resultado[0]  
        modificacion = "eliminacio"
        fecha = fecha_eliminacion
        misModificaciones.eliminar(id, [modificacion, fecha, nombre])
        return redirect('/')


@proyecto.route('/editar/<id>')
def editar(id):
    usuario = misModificaciones.obtener_usuario_por_id(id) 
    if usuario:
        return render_template("modificar.html", usuario=usuario)
    else:
        return redirect('/')

@proyecto.route('/editar/<id>', methods=['POST'])
def editar_usuario(id):
    ID = request.form['id']
    nombre = request.form['nombre']
    estatura = request.form['estatura']
    peso = request.form['peso']
    fecha = request.form['fecha']
    misModificaciones.editar_usuario(id,ID, nombre, estatura, peso, fecha)

    return redirect('/')

    
    

    

    
    
    

if __name__=='__main__':
    proyecto.run(host='0.0.0.0',debug=True,port=5080)

    