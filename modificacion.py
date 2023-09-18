class Eliminar:
   def __init__(self, mysql):
        self.mysql = mysql
        self.mysql = mysql
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()
        
   def buscar(self,id):
        sql = f"SELECT * FROM usuarios WHERE id={id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        if len(resultado)>0:
            return True
        else:
            return False       

   def eliminar(self,id, usuario):
  
     if self.buscar(id):
        sql_delete = f"DELETE FROM usuarios WHERE id = {id}"
        self.cursor.execute(sql_delete)    
        sql_insert = f"INSERT INTO registro (modificacion, fecha,nombre ) \
                       VALUES ('{usuario[0]}','{usuario[1]}','{usuario[2]}')"
        self.cursor.execute(sql_insert)
        self.conexion.commit()
        return True
     else:
        return False
   def obtener_usuario_por_id(self, id):
        sql = f"SELECT * FROM usuarios WHERE id={id}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        return resultado
   
   
   def editar_usuario(self, id, ID, nombre, estatura, peso, fecha):
        usuario_anterior = self.obtener_usuario_por_id(id)
        nombre_anterior = usuario_anterior[1] if usuario_anterior else ""
        sql = f"UPDATE usuarios SET id = %s, nombre=%s, estatura=%s, peso=%s, fecha=%s WHERE id=%s"
        self.cursor.execute(sql, (ID , nombre, estatura, peso, fecha, id))
        modificacion = "modificación"
        fecha_modificacion = fecha
        sql_insert_modificacion = f"INSERT INTO registro (modificacion, fecha, nombre) \
                                    VALUES (%s, %s, %s)"
        self.cursor.execute(sql_insert_modificacion, (modificacion, fecha_modificacion, nombre_anterior))
        self.conexion.commit()
   
         
        
      
        