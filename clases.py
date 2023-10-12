from datetime import datetime
class Clases:
    def __init__(self, mysql):
        self.mysql = mysql
        self.mysql = mysql
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()
    def consultar(self):
        sql = "SELECT * FROM usuarios WHERE activo=0"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado 
    def agregar(self, usuario):
       sql = f"INSERT INTO usuarios (id, nombre,estatura,peso,fecha,contrasena) \
       VALUES ('{usuario[0]}', '{usuario[1]}', '{usuario[2]}', {usuario[3]}, \
       '{usuario[4]}','{usuario[5]}')"
       self.cursor.execute(sql)
       self.conexion.commit()
    

    def buscar(self,id):
        sql = f"SELECT nombre FROM usuarios WHERE id={id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        if len(resultado)>0:
            return True
        else:
            return False   

       
    