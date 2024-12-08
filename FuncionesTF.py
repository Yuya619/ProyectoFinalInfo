#Yurany Mosquera Palacios, Adrian Martinez Esteban


import pymysql #Importo libreria para conectarse a la DB
from pymongo import MongoClient
import json
from datetime import datetime


def verificar_login(usuario, clave):
    """
    Verifica si el usuario y la clave proporcionados son válidos en la base de datos.
    
    Esta función se conecta a la base de datos, consulta la tabla de usuarios y valida
    si las credenciales proporcionadas (usuario y clave) coinciden con algún registro
    en la base de datos. Si el login es exitoso, devuelve `True` junto con el rol del usuario,
    de lo contrario, devuelve `False` y una cadena vacía como rol.
    
    Args:
        usuario (str): El nombre de usuario que se intenta verificar.
        clave (str): La contraseña del usuario.
        
    Returns:
        tuple: Un tupla que contiene un valor booleano (`True` si el login es correcto, `False` si es incorrecto)
               y el rol del usuario si el login es exitoso, o una cadena vacía si no lo es.
    
    Ejemplo:
        login, rol = verificar_login('mi_usuario', 'mi_clave')
        print(f"Login exitoso: {login}, Rol: {rol}")
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para verificar el usuario y la clave
        sql = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
        
        # Ejecuta la consulta pasando el nombre de usuario y la clave como parámetros
        conexion.execute(sql, (usuario, clave))
        
        # Obtiene todos los resultados de la consulta
        resultado = conexion.fetchall()  
        
        # Extrae el rol del primer resultado obtenido (si existe)
        if resultado:
            rol = resultado[0][3]  # Asume que el rol está en la columna 4 (índice 3)
        
        # Cierra la conexión a la base de datos
        conexion.close()

        # Si hay resultados, el login es exitoso
        if resultado:
            login = True
        else:
            login = False  # Si no hay resultados, el login falla
            rol=''
    except: 
        # Si ocurre algún error al conectar con la base de datos, muestra un mensaje y establece login como False
        print("\nNo se pudo conectar a la base de datos")
        login = False
        rol = ''  # Si hay error, no hay rol asociado

    # Devuelve el estado del login y el rol
    return login, rol

def agregar_usuario(user_id, username, password, role):
    """
    Agrega un nuevo usuario a la base de datos.
    
    Esta función se conecta a la base de datos y agrega un nuevo registro en la tabla 'usuarios'
    con los valores proporcionados para el ID de usuario, nombre de usuario, contraseña y rol.
    
    Args:
        user_id (int): El ID del usuario a agregar.
        username (str): El nombre de usuario.
        password (str): La contraseña del usuario.
        role (str): El rol del usuario (por ejemplo, 'admin', 'user').
        
    Returns:
        None: Si la operación es exitosa, no retorna ningún valor. Si ocurre un error, muestra un mensaje.
    
    Ejemplo:
        agregar_usuario(1, 'nuevo_usuario', 'mi_clave', 'administrador')
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para insertar un nuevo usuario en la tabla 'usuarios'
        sql = "INSERT INTO usuarios (user_id, username, password, role) VALUES (%s, %s, %s, %s)"
        
        # Ejecuta la consulta pasando los parámetros proporcionados
        conexion.execute(sql, (user_id, username, password, role))
        
        # Aplica los cambios a la base de datos (commit)
        cnx.commit()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        # Mensaje indicando que el usuario fue agregado exitosamente
        print("\nSe agregó el nuevo usuario a la base de datos")
    
    except: 
        # Si ocurre algún error en el proceso, muestra un mensaje de error
        print("\nNo se pudo agregar el nuevo usuario a la base de datos")
    
    # La función no retorna ningún valor
    return
def agregar_paciente(ID, nombre, edad, genero, historial):
    """
    Agrega un nuevo paciente a la base de datos.
    
    Esta función se conecta a la base de datos y agrega un nuevo registro en la tabla 'pacientes'
    con los valores proporcionados para el ID, nombre, edad, genero, historial
    
    Args:
        ID (int): El ID del paciente  a agregar.
        nombre (str): El nombre de paciente.
        edad (str): La contraseña del paciente.
        genero (str): El genero del paciente
        historial (str): La condicion del paciente
    Returns:
        None: Si la operación es exitosa, no retorna ningún valor. Si ocurre un error, muestra un mensaje.
    
    Ejemplo:
        agregar_paciente(12345, nombre, edad, genero, historial)
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para insertar un nuevo usuario en la tabla 'usuarios'
        sql = "INSERT INTO pacientes (ID, nombre, edad, genero, historial) VALUES (%s, %s, %s, %s, %s)"
        
        # Ejecuta la consulta pasando los parámetros proporcionados
        conexion.execute(sql, (ID, nombre, edad, genero, historial))
        
        # Aplica los cambios a la base de datos (commit)
        cnx.commit()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        # Mensaje indicando que el usuario fue agregado exitosamente
        print("\nSe agregó el nuevo paciente a la base de datos")
    
    except: 
        # Si ocurre algún error en el proceso, muestra un mensaje de error
        print("\nNo se pudo agregar el nuevo paciente a la base de datos")
    
    # La función no retorna ningún valor
    return

def consultar_usuarios():
    """
    Consulta todos los usuarios registrados en la base de datos.
    
    Esta función se conecta a la base de datos y ejecuta una consulta SQL para obtener
    todos los registros de la tabla 'usuarios'. Luego muestra los resultados de la consulta.

    Returns:
        None: Si la operación es exitosa, muestra los resultados de la consulta. Si ocurre un error,
              muestra un mensaje de error.
    
    Ejemplo:
        consultar_usuarios()
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para obtener todos los usuarios
        sql = "SELECT * FROM usuarios"
        
        # Ejecuta la consulta
        conexion.execute(sql)
        
        # Obtiene todos los resultados de la consulta
        resultado = conexion.fetchall()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        # Muestra los resultados obtenidos
        print("\n")
        print(resultado)
    
    except:
        # Si ocurre algún error en la conexión o consulta, muestra un mensaje de error
        print("\nNo se pudo consultar a la base de datos")
    
    # La función no retorna ningún valor
    return


def actualizar_usuario(user_id, user_id2, username, password, role):
    """
    Actualiza los datos de un usuario en la base de datos.
    
    Esta función se conecta a la base de datos y actualiza los registros del usuario en la tabla 'usuarios'
    según el ID de usuario original (user_id) con los nuevos valores proporcionados (user_id2, username, password, role).
    
    Args:
        user_id (int): El ID del usuario cuyo registro se desea actualizar.
        user_id2 (int): El nuevo ID de usuario que se actualizará.
        username (str): El nuevo nombre de usuario.
        password (str): La nueva contraseña del usuario.
        role (str): El nuevo rol del usuario (por ejemplo, 'admin', 'user').
        
    Returns:
        None: Si la operación es exitosa, muestra un mensaje indicando que los datos fueron actualizados. Si ocurre un error,
              muestra un mensaje de error.
    
    Ejemplo:
        actualizar_usuario(1, 2, 'usuario_modificado', 'nueva_clave', 'admin')
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para actualizar los datos del usuario en la tabla 'usuarios'
        sql = "UPDATE usuarios SET user_id=%s, username=%s, password=%s, role=%s WHERE user_id=%s"
        
        # Ejecuta la consulta pasando los parámetros proporcionados
        conexion.execute(sql, (user_id2, username, password, role, user_id))
        
        # Aplica los cambios a la base de datos (commit)
        cnx.commit()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        # Mensaje indicando que los datos del usuario fueron actualizados exitosamente
        print("\nSe actualizaron los datos del usuario")
    
    except:
        # Si ocurre algún error en el proceso, muestra un mensaje de error
        print("\nNo se pudo actualizar el nuevo usuario a la base de datos")
    
    # La función no retorna ningún valor
    return


def eliminar_usuario(user_id):
    """
    Elimina un usuario de la base de datos por su ID.
    
    Esta función se conecta a la base de datos y elimina el registro de un usuario en la tabla 'usuarios'
    cuyo ID coincida con el valor proporcionado.
    
    Args:
        user_id (int): El ID del usuario que se desea eliminar.
        
    Returns:
        None: Si la operación es exitosa, muestra un mensaje indicando que el usuario fue eliminado. Si ocurre un error,
              muestra un mensaje de error.
    
    Ejemplo:
        eliminar_usuario(1)
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para eliminar un usuario por su ID
        sql = "DELETE FROM usuarios WHERE user_id=%s"
        
        # Ejecuta la consulta con el ID del usuario
        conexion.execute(sql, (user_id))
        
        # Aplica los cambios a la base de datos (commit)
        cnx.commit()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        # Mensaje indicando que el usuario fue eliminado exitosamente
        print("\nSe eliminó el usuario")
    
    except:
        # Si ocurre algún error en el proceso, muestra un mensaje de error
        print("\nNo se pudo eliminar el usuario de la base de datos")
    
    # La función no retorna ningún valor
    return

def eliminar_paciente(ID):
    """
    Elimina un paciente de la base de datos por su ID.
    
    Esta función se conecta a la base de datos y elimina el registro de un paciente en la tabla 'pacientes'
    cuyo ID coincida con el valor proporcionado.
    
    Args:
       ID (int): El ID del paciente que se desea eliminar.
        
    Returns:
        None: Si la operación es exitosa, muestra un mensaje indicando que el paciente fue eliminado. Si ocurre un error,
              muestra un mensaje de error.
    
    Ejemplo:
        eliminar_paciente(ID)
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para eliminar un usuario por su ID
        sql = "DELETE FROM pacientes WHERE ID=%s"
        
        # Ejecuta la consulta con el ID del usuario
        conexion.execute(sql, (ID))
        
        # Aplica los cambios a la base de datos (commit)
        cnx.commit()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        # Mensaje indicando que el usuario fue eliminado exitosamente
        print("\nSe eliminó el paciente")
    
    except:
        # Si ocurre algún error en el proceso, muestra un mensaje de error
        print("\nNo se pudo eliminar el paciente de la base de datos")
    
    # La función no retorna ningún valor
    return


def ver_pacientes(user_id):
    """
    Consulta los datos de un paciente por su ID.
    
    Esta función se conecta a la base de datos y obtiene los datos de un paciente en la tabla 'pacientes'
    cuyo ID coincida con el proporcionado.
    
    Args:
        user_id (int): El ID del paciente cuya información se desea consultar.
        
    Returns:
        None: Si la operación es exitosa, muestra los datos del paciente. Si no se encuentra al paciente o ocurre un error,
              muestra un mensaje correspondiente.
    
    Ejemplo:
        ver_pacientes(1)
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para obtener los datos de un paciente por su ID
        sql = "SELECT * FROM pacientes WHERE ID=%s"
        
        # Ejecuta la consulta con el ID del paciente
        conexion.execute(sql, (user_id,))
        
        # Obtiene todos los resultados de la consulta
        resultado = conexion.fetchall()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        # Si no se encuentra ningún paciente, muestra un mensaje
        if len(resultado) < 1:
            print("\nNo se encontró el paciente")
        else:
            # Si se encuentra el paciente, muestra los datos
            print("\n")
            print(resultado)
    
    except:
        # Si ocurre algún error en el proceso, muestra un mensaje de error
        print("\nNo se pudo consultar a la base de datos")
    
    # La función no retorna ningún valor
    return



def actualizar_paciente(ID, ID2, nombre, edad, genero, historial):
    """
    Actualiza los datos de un paciente en la base de datos.
    
    Esta función se conecta a la base de datos y actualiza los registros del paciente en la tabla 'pacientes'
    según el ID de paciente original (ID) con los nuevos valores proporcionados (ID2, nombre, edad, genero, historial).
    
    Args:
        ID (int): El ID del paciente cuyo registro se desea actualizar.
        ID2 (int): El nuevo ID del paciente que se actualizará.
        nombre (str): El nuevo nombre del paciente.
        edad (int): La nueva edad del paciente.
        genero (str): El nuevo género del paciente.
        historial (str): El nuevo historial médico del paciente.
        
    Returns:
        None: Si la operación es exitosa, muestra un mensaje indicando que los datos fueron actualizados. Si ocurre un error,
              muestra un mensaje de error.
    
    Ejemplo:
        actualizar_paciente(1, 2, 'Juan Pérez', 30, 'Masculino', 'Historial actualizado')
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para actualizar los datos del paciente en la tabla 'pacientes'
        sql = "UPDATE pacientes SET ID=%s, nombre=%s, edad=%s, genero=%s, historial=%s WHERE ID=%s"
        
        # Ejecuta la consulta pasando los parámetros proporcionados
        conexion.execute(sql, (ID2, nombre, edad, genero, historial, ID))
        
        # Aplica los cambios a la base de datos (commit)
        cnx.commit()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        # Mensaje indicando que los datos del paciente fueron actualizados exitosamente
        print("\nSe actualizaron los datos del paciente")
    
    except:
        # Si ocurre algún error en el proceso, muestra un mensaje de error
        print("\nNo se pudo actualizar el paciente en la base de datos")
    
    # La función no retorna ningún valor
    return


def actualizar_id_diagnostico(ID, ID2):
    """
    Actualiza el ID de un diagnóstico en la base de datos.
    
    Esta función se conecta a la base de datos y actualiza el ID del diagnóstico en la tabla 'diagnosticos'
    para el registro cuyo ID coincida con el proporcionado, con el nuevo ID proporcionado (ID2).
    
    Args:
        ID (int): El ID del diagnóstico cuyo registro se desea actualizar.
        ID2 (int): El nuevo ID para el diagnóstico.
        
    Returns:
        None: Si la operación es exitosa, muestra un mensaje indicando que el diagnóstico fue asociado al nuevo ID. 
              Si ocurre un error, muestra un mensaje de error.
    
    Ejemplo:
        actualizar_id_diagnostico(1, 2)
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para actualizar el ID de un diagnóstico en la tabla 'diagnosticos'
        sql = "UPDATE diagnosticos SET ID=%s WHERE ID=%s"
        
        # Ejecuta la consulta pasando los parámetros proporcionados
        conexion.execute(sql, (ID2, ID))
        
        # Aplica los cambios a la base de datos (commit)
        cnx.commit()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        # Mensaje indicando que el ID del diagnóstico fue actualizado exitosamente
        print("\nSe asoció el diagnóstico al nuevo ID")
    
    except:
        # Si ocurre algún error en el proceso, muestra un mensaje de error
        print("\nNo se pudo actualizar el id del paciente en la base de datos de diagnósticos")
    
    # La función no retorna ningún valor
    return


def ver_diagnostico(user_id):
    """
    Consulta y muestra el diagnóstico de un paciente desde la base de datos.

    Esta función se conecta a la base de datos y obtiene los datos del diagnóstico 
    del paciente correspondiente al `user_id` proporcionado.

    Args:
        user_id (int): El ID del paciente cuyo diagnóstico se desea consultar.

    Returns:
        list: Una lista con los resultados del diagnóstico, o una lista vacía si no se encuentra el diagnóstico.

    Ejemplo:
        resultado = ver_diagnostico(1)
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para obtener los datos del diagnóstico del paciente
        sql = "SELECT * FROM diagnosticos WHERE ID=%s"
        
        # Ejecuta la consulta pasando el user_id como parámetro
        conexion.execute(sql, (user_id,))
        
        # Almacena los resultados de la consulta en una variable
        resultado = conexion.fetchall()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        # Si no se encuentran resultados, se muestra un mensaje indicativo
        if len(resultado) < 1:
            print("\nNo se encontró el diagnóstico del paciente")
        else:
            # Muestra los resultados encontrados
            print("\n")
            print(resultado)
    
    except:
        # Si ocurre algún error al consultar, muestra un mensaje de error
        print("\nNo se pudo consultar a la base de datos")
    
    # Retorna los resultados del diagnóstico (vacío si no se encuentra nada)
    return resultado


def actualizar_diagnostico(ID, tipo_imagen, resultado_IA, fecha_imagen, fecha_diagnostico, estado):
    """
    Actualiza los datos de un diagnóstico en la base de datos.

    Esta función se conecta a la base de datos y actualiza la información de un diagnóstico 
    (como el tipo de imagen, el resultado de la IA, la fecha de la imagen, la fecha del diagnóstico y el estado)
    para el diagnóstico cuyo ID coincida con el proporcionado.

    Args:
        ID (int): El ID del diagnóstico a actualizar.
        tipo_imagen (str): El tipo de imagen del diagnóstico.
        resultado_IA (str): El resultado proporcionado por la IA sobre la imagen.
        fecha_imagen (str): La fecha en que se tomó la imagen (formato 'AAAA-MM-DD').
        fecha_diagnostico (str): La fecha en que se realizó el diagnóstico (formato 'AAAA-MM-DD').
        estado (str): El estado del diagnóstico (por ejemplo, "pendiente", "finalizado").

    Returns:
        None: Si la operación es exitosa, muestra un mensaje indicando que los datos del diagnóstico fueron actualizados.
              Si ocurre un error, muestra un mensaje de error.

    Ejemplo:
        actualizar_diagnostico(1, "Radiografía", "Positivo", "2024-11-01", "2024-11-02", "finalizado")
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para actualizar los datos del diagnóstico en la tabla 'diagnosticos'
        sql = "UPDATE diagnosticos SET tipo_imagen=%s, resultado_IA=%s, fecha_imagen=%s, fecha_diagnostico=%s, estado=%s WHERE ID=%s"
        
        # Ejecuta la consulta pasando los parámetros proporcionados
        conexion.execute(sql, (tipo_imagen, resultado_IA, fecha_imagen, fecha_diagnostico, estado, ID))
        
        # Aplica los cambios a la base de datos (commit)
        cnx.commit()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        # Mensaje indicando que los datos del diagnóstico fueron actualizados exitosamente
        print("\nSe actualizaron los datos del diagnóstico")
    
    except:
        # Si ocurre algún error, muestra un mensaje de error
        print("\nNo se pudo actualizar el diagnóstico del paciente en la base de datos")
    
    # La función no retorna ningún valor
    return
 

def actualizar_estado(user_id, estado):
    """
    Actualiza el estado de un diagnóstico en la base de datos.

    Esta función se conecta a la base de datos y actualiza el estado de un diagnóstico 
    (por ejemplo, cambiarlo a "revisado") para el diagnóstico cuyo ID coincida con el `user_id` proporcionado.

    Args:
        user_id (int): El ID del diagnóstico a actualizar.
        estado (str): El nuevo estado del diagnóstico (por ejemplo, "revisado").

    Returns:
        None: Si la operación es exitosa, muestra un mensaje indicando que el estado fue actualizado.
              Si ocurre un error, muestra un mensaje de error.

    Ejemplo:
        actualizar_estado(1, "revisado")
    """
    # Intento de conexión a la base de datos
    try:
        # Establece la conexión con la base de datos
        cnx = pymysql.connect(user='root', password='', host='127.0.0.1', database='informatica1_pf')
        
        # Crea un cursor para ejecutar consultas SQL
        conexion = cnx.cursor()
        
        # Consulta SQL para actualizar el estado del diagnóstico en la tabla 'diagnosticos'
        sql = "UPDATE diagnosticos SET estado=%s WHERE ID=%s"
        
        # Ejecuta la consulta pasando el estado y el user_id como parámetros
        conexion.execute(sql, (estado, user_id))
        
        # Aplica los cambios a la base de datos (commit)
        cnx.commit()
        
        # Cierra la conexión con la base de datos
        conexion.close()
        
        # Mensaje indicando que el estado del diagnóstico fue actualizado exitosamente
        print("\nSe actualizó el estado del paciente a revisado")
    
    except:
        # Si ocurre algún error, muestra un mensaje de error
        print("\nNo se pudo actualizar el estado del paciente a revisado")
    
    # La función no retorna ningún valor
    return


def agregar_imagen(id_imagen, id_paciente, fecha, tipo_imagen, parte_cuerpo, imagen_path, condicion_sugerida, probabilidad, notas, id_tecnica, fecha_nota, texto):
    """
    Agrega un nuevo reporte técnico de imagen en la base de datos MongoDB.

    Esta función inserta los detalles de una imagen médica (junto con análisis de IA y notas técnicas) 
    en la colección 'reportes_tecnicos' de la base de datos 'informatica1_PF'.

    Args:
        id_imagen (int): El ID único de la imagen.
        id_paciente (int): El ID del paciente asociado con la imagen.
        fecha (str): La fecha en que se tomó la imagen (formato 'AAAA-MM-DD').
        tipo_imagen (str): El tipo de imagen tomada (por ejemplo, "Radiografía").
        parte_cuerpo (str): La parte del cuerpo que fue fotografiada.
        imagen_path (str): La ruta de la imagen almacenada.
        condicion_sugerida (str): La condición sugerida por la IA basada en la imagen.
        probabilidad (float): La probabilidad de la condición sugerida (en porcentaje).
        notas (str): Notas adicionales del análisis de IA sobre la imagen.
        id_tecnica (int): El ID de la técnica usada para obtener la imagen.
        fecha_nota (str): La fecha en que se escribió la nota técnica (formato 'AAAA-MM-DD').
        texto (str): El contenido de la nota técnica.

    Returns:
        None: Si la operación es exitosa, muestra un mensaje indicando que los datos fueron insertados correctamente.
              Si ocurre un error, muestra un mensaje de error.

    Ejemplo:
        agregar_imagen(1, 101, "2024-11-01", "Radiografía", "Tórax", "/path/to/image.jpg", 
                       "Neumonía", 95.5, "Condición grave", 123, "2024-11-02", "Se observan signos de infección.")
    """
    # Intento de conexión a MongoDB
    try:
        # Conexión a la base de datos MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        
        # Accede a la base de datos 'informatica1_PF' y a la colección 'reportes_tecnicos'
        db = client['informatica1_PF']
        collection = db['reportes_tecnicos']
        
        # Crea el objeto JSON con los datos que se insertarán
        json = {
            "id_imagen": id_imagen,
            "id_paciente": id_paciente,
            "fecha": fecha,
            "tipo_imagen": tipo_imagen,
            "parte_cuerpo": parte_cuerpo,
            "imagen_path": imagen_path,
            "analisis_IA": {
                "condicion_sugerida": condicion_sugerida,
                "probabilidad_%": probabilidad,
                "notas": notas
            },
            "notas_tecnicas": [
                {
                    "id_tecnica": id_tecnica,
                    "fecha_nota": fecha_nota,
                    "texto": texto
                }
            ]
        }
        
        # Inserta el documento JSON en la colección 'reportes_tecnicos'
        result = collection.insert_one(json)
        
        # Cierra la conexión con la base de datos
        client.close()
        
        # Mensaje indicando que los datos fueron insertados correctamente
        print("\nLos datos han sido insertados correctamente en MongoDB.")
        
    except:
        # Si ocurre algún error, muestra un mensaje de error
        print("\nNo fue posible insertar los datos")
    
    # La función no retorna ningún valor
    return

        
def ver_imagen(id_paciente):
    """
    Consulta y muestra los reportes técnicos de imagen asociados a un paciente en MongoDB.

    Esta función busca en la colección 'reportes_tecnicos' todos los documentos 
    que tengan el campo 'id_paciente' igual al proporcionado y los imprime.

    Args:
        id_paciente (int): El ID del paciente cuyo historial de imágenes se desea consultar.

    Returns:
        None: La función no retorna ningún valor. Solo imprime los resultados de la consulta.

    Ejemplo:
        ver_imagen(101)
    """
    # Intentar realizar la consulta a la base de datos
    try:
        # Conexión a la base de datos MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        
        # Accede a la base de datos 'informatica1_PF' y la colección 'reportes_tecnicos'
        db = client['informatica1_PF']
        collection = db['reportes_tecnicos']
        
        # Realiza la consulta buscando todos los reportes de imagen para el 'id_paciente' proporcionado
        datos = collection.find({"id_paciente": id_paciente})
        
        # Cierra la conexión con la base de datos
        client.close()
        
        # Imprimir los documentos encontrados
        print("\n")
        for dato in datos:
            print(dato)
    
    # Si ocurre un error durante la conexión o consulta, captura el error y muestra un mensaje
    except Exception as e:
        print("\nNo fue posible consultar los datos. Error:", str(e))

    # La función no tiene valor de retorno
    return

    
def actualizar_imagen(id_imagen, id_paciente, id_paciente2, fecha, tipo_imagen, parte_cuerpo, imagen_path, condicion_sugerida, probabilidad, notas, id_tecnica, fecha_nota, texto):
    """
    Actualiza los datos de una imagen de diagnóstico en MongoDB.

    Esta función actualiza el documento en la colección 'reportes_tecnicos' de MongoDB
    correspondiente al paciente con 'id_paciente', reemplazando los campos relevantes
    con los nuevos valores proporcionados.

    Args:
        id_imagen (str): ID único de la imagen.
        id_paciente (str): ID del paciente original (el que se desea reemplazar).
        id_paciente2 (str): Nuevo ID de paciente al que se le asignará la imagen.
        fecha (str): Fecha en que se tomó la imagen.
        tipo_imagen (str): Tipo de imagen (por ejemplo, radiografía, resonancia).
        parte_cuerpo (str): Parte del cuerpo que se escaneó.
        imagen_path (str): Ruta del archivo de imagen.
        condicion_sugerida (str): Condición sugerida por la IA.
        probabilidad (float): Probabilidad asociada a la condición sugerida.
        notas (str): Notas relacionadas con el análisis de la IA.
        id_tecnica (str): ID de la técnica aplicada para el análisis de la imagen.
        fecha_nota (str): Fecha en que se creó la nota técnica.
        texto (str): Texto de la nota técnica.

    Returns:
        None: La función no retorna un valor. Solo imprime el resultado de la operación.

    Ejemplo:
        actualizar_imagen('imagen_123', 'paciente_456', 'paciente_789', '2024-12-01', 'radiografía', 'tórax', 'ruta/imagen.jpg', 'neumonía', 85.5, 'Alta probabilidad de neumonía', 'tecnica_1', '2024-12-01', 'Texto de la nota técnica')
    """
    # Intentar realizar la actualización en la base de datos
    try:
        # Conexión a MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['informatica1_PF']
        collection = db['reportes_tecnicos']
        
        # Crear el documento con los nuevos datos para la actualización
        json = {
            "id_imagen": id_imagen,
            "id_paciente": id_paciente2,  # Se actualiza el ID del paciente
            "fecha": fecha,
            "tipo_imagen": tipo_imagen,
            "parte_cuerpo": parte_cuerpo,
            "imagen_path": imagen_path,
            "analisis_IA": {
                "condicion_sugerida": condicion_sugerida,
                "probabilidad_%": probabilidad,
                "notas": notas
            },
            "notas_tecnicas": [
                {
                    "id_tecnica": id_tecnica,
                    "fecha_nota": fecha_nota,
                    "texto": texto
                }
            ]
        }

        # Realizar la actualización en la colección
        result = collection.update_one(
            {"id_paciente": id_paciente},  # Filtro: buscamos el documento con el id_paciente
            {"$set": json}  # Operador $set: actualiza los campos con los valores del json
        )

        # Cerrar la conexión con MongoDB
        client.close()
        
        # Imprimir mensaje de éxito
        print("\nLos datos han sido actualizados correctamente en MongoDB.")
    
    # Si ocurre un error durante la actualización, captura el error y muestra un mensaje
    except Exception as e:
        print("\nNo fue posible actualizar los datos. Error:", str(e))

    # La función no tiene valor de retorno
    return

        
def eliminar_imagen(id_paciente):
    """
    Elimina un documento de la colección 'reportes_tecnicos' en MongoDB basado en el ID del paciente.

    Esta función elimina el documento correspondiente al paciente con el 'id_paciente'
    proporcionado en la colección 'reportes_tecnicos' de MongoDB.

    Args:
        id_paciente (str): El ID del paciente cuyo documento se desea eliminar.

    Returns:
        None: La función no retorna un valor. Solo imprime el resultado de la operación.

    Ejemplo:
        eliminar_imagen('paciente_123')
    """
    # Intentar eliminar el documento de la base de datos
    try:
        # Conexión a MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['informatica1_PF']
        collection = db['reportes_tecnicos']
        
        # Eliminar el documento que coincide con el id_paciente proporcionado
        datos = collection.delete_one({"id_paciente": id_paciente})

        # Cerrar la conexión con MongoDB
        client.close()
        
        # Imprimir mensaje de éxito
        print("\nInformación eliminada correctamente")

    # Si ocurre un error durante la eliminación, captura el error y muestra un mensaje
    except Exception as e:
        print("\nNo fue posible eliminar los datos. Error:", str(e))

    # La función no tiene valor de retorno
    return

        
def crear_reporte(user_id, tipo_imagen, resultado_IA, fecha_imagen, fecha_diagnostico, estado, notas):
    """
    Crea e inserta un nuevo reporte médico en la colección 'reportes_medicos' en MongoDB.

    Esta función toma los detalles del reporte médico, los formatea adecuadamente y los inserta en la 
    base de datos MongoDB. Se asegura de que las fechas de la imagen y diagnóstico estén en el formato 
    adecuado 'aaaa-mm-dd'.

    Args:
        user_id (str): El ID del usuario que genera el reporte.
        tipo_imagen (str): El tipo de imagen tomada (por ejemplo, "radiografía").
        resultado_IA (str): El resultado de la evaluación realizada por inteligencia artificial.
        fecha_imagen (datetime): La fecha en que se tomó la imagen (debe ser un objeto datetime).
        fecha_diagnostico (datetime): La fecha en que se realizó el diagnóstico (debe ser un objeto datetime).
        estado (str): El estado del reporte (por ejemplo, "pendiente", "revisado").
        notas (str): Notas adicionales sobre el diagnóstico o las imágenes.

    Returns:
        None: La función no retorna ningún valor, pero imprime un mensaje indicando el éxito o error de la operación.

    Ejemplo:
        crear_reporte('user123', 'radiografía', 'normal', datetime(2024, 12, 1), datetime(2024, 12, 1), 'revisado', 'Todo correcto.')
    """
    try:
        # Verificar si fecha_diagnostico es un objeto datetime
        fecha_diagnostico = fecha_diagnostico.strftime('%Y-%m-%d')  # Convertir la fecha a formato 'aaaa-mm-dd'
        fecha_imagen = fecha_imagen.strftime('%Y-%m-%d')  # Convertir la fecha a formato 'aaaa-mm-dd'

        # Conexión a la base de datos MongoDB
        with MongoClient('mongodb://localhost:27017/') as client:
            db = client['informatica1_PF']  # Seleccionar la base de datos
            collection = db['reportes_medicos']  # Seleccionar la colección de reportes médicos
            
            # Crear el documento a insertar como un diccionario de Python
            reporte = {
                "user_id": user_id,
                "tipo_imagen": tipo_imagen,
                "resultado_IA": resultado_IA,
                "fecha_imagen": fecha_imagen,
                "fecha_diagnostico": fecha_diagnostico,
                "estado": estado,
                "notas": notas
            }
            
            # Insertar el documento en la colección
            result = collection.insert_one(reporte)
            
            # Imprimir mensaje de éxito
            print("\nLos datos han sido insertados correctamente en MongoDB.")
        
    except Exception as e:
        # Imprimir el error específico si ocurre uno
        print(f"\nNo fue posible insertar los datos. Error: {e}")


def actualizar_id_pacientes_reportes_tecnicos(id_paciente, id_paciente_2):
    """
    Actualiza el ID de un paciente en los reportes técnicos en la base de datos MongoDB.

    Esta función busca un documento en la colección 'reportes_tecnicos' que tenga el 'id_paciente' 
    especificado y actualiza su valor a un nuevo 'id_paciente_2'. Si no se encuentra un documento 
    con el 'id_paciente' dado, no se realiza ninguna actualización.

    Args:
        id_paciente (str): El ID actual del paciente que se desea actualizar.
        id_paciente_2 (str): El nuevo ID que se asignará al paciente en los reportes.

    Returns:
        None: La función no retorna ningún valor, pero imprime un mensaje indicando el éxito o error de la operación.

    Ejemplo:
        actualizar_id_pacientes_reportes_tecnicos("12345", "67890")
    """
    try:
        # Conexión a la base de datos MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['informatica1_PF']
        collection = db['reportes_tecnicos']

        # Actualiza solo el campo id_paciente
        result = collection.update_one(
            {"id_paciente": id_paciente},  # Filtro: buscamos el documento con el id_paciente
            {"$set": {"id_paciente": id_paciente_2}}  # Operador $set: actualiza el campo id_paciente con el nuevo valor
        )

        # Verificar si se actualizó algún documento
        if result.modified_count == 1:
            print(f"El ID del paciente se ha actualizado correctamente a {id_paciente_2}")
        else:
            print(f"No se encontró ningún documento con id_paciente={id_paciente}")

    except Exception as e:
        # Imprimir el error específico si ocurre uno
        print(f"Error al actualizar el documento: {str(e)}")

    finally:
        # Cerrar la conexión con la base de datos
        client.close()


def actualizar_id_pacientes_reportes_medicos(id_paciente, id_paciente_2):
    """
    Actualiza el ID de un paciente en los reportes médicos en la base de datos MongoDB.

    Esta función busca un documento en la colección 'reportes_medicos' que tenga el 'user_id' 
    especificado y actualiza su valor a un nuevo 'user_id' (id_paciente_2). Si no se encuentra 
    un documento con el 'user_id' dado, no se realiza ninguna actualización.

    Args:
        id_paciente (str): El ID actual del paciente que se desea actualizar.
        id_paciente_2 (str): El nuevo ID que se asignará al paciente en los reportes.

    Returns:
        None: La función no retorna ningún valor, pero imprime un mensaje indicando el éxito o error de la operación.

    Ejemplo:
        actualizar_id_pacientes_reportes_medicos("12345", "67890")
    """
    try:
        # Conexión a la base de datos MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['informatica1_PF']
        collection = db['reportes_medicos']

        # Actualiza solo el campo user_id
        result = collection.update_one(
            {"user_id": id_paciente},  # Filtro: buscamos el documento con el user_id (id_paciente)
            {"$set": {"user_id": id_paciente_2}}  # Operador $set: actualiza el campo user_id con el nuevo valor
        )

        # Verificar si se actualizó algún documento
        if result.modified_count == 1:
            print(f"El ID del paciente se ha actualizado correctamente a {id_paciente_2}")
        else:
            print(f"No se encontró ningún documento con id_paciente={id_paciente}")

    except Exception as e:
        # Imprimir el error específico si ocurre uno
        print(f"Error al actualizar el documento: {str(e)}")

    finally:
        # Cerrar la conexión con la base de datos
        client.close()

        
def valida_numero(texto):
    """
    Solicita al usuario que ingrese un número entero válido.
    
    Esta función sigue solicitando la entrada hasta que el usuario ingrese un número entero válido.
    
    Args:
        texto (str): El mensaje que se le muestra al usuario para pedir la entrada.
        
    Returns:
        int: El número entero ingresado por el usuario.
        
    Ejemplo:
        numero = valida_numeros("Por favor, ingresa tu edad: ")
        print(f"La edad ingresada es: {numero}")
    """

    while True:
        entrada = input(texto)
        try:
            # Intentamos convertir la entrada a un entero
            numero = int(entrada)
            return numero  # Si la conversión es exitosa, retornamos el número
        except ValueError:
            # Si ocurre un error (por ejemplo, la entrada no es un número entero)
            print("¡Error! Se ingresó texto en lugar de números.")
            

def valida_fechas(texto):
    
    """
    Solicita al usuario que ingrese una fecha en formato 'aaaa-mm-dd'.
    
    Esta función valida que la fecha ingresada siga el formato adecuado y que
    sea una fecha válida. Si la entrada no cumple con el formato o es una fecha
    inválida (por ejemplo, '2024-02-30'), la función continuará solicitando la 
    entrada hasta que se ingrese una fecha válida.
    
    Returns:
        datetime: Un objeto datetime que representa la fecha válida ingresada.
    
    Ejemplo:
        fecha = obtener_fecha_valida()
        print(f"Fecha ingresada: {fecha.strftime('%Y-%m-%d')}")
    
    Raises:
        ValueError: Si la fecha ingresada no tiene el formato correcto o es inválida,
                    se solicita nuevamente la fecha.
    """
    while True:
        entrada = input(texto)

        # Verificamos si la longitud es 10 (formato aaaa-mm-dd) y si los caracteres son correctos
        if len(entrada) == 10 and entrada[4] == '-' and entrada[7] == '-':
            # Intentamos convertir la fecha usando datetime
            try:
                fecha = datetime.strptime(entrada, "%Y-%m-%d")
                return entrada  # Si es válido, retornamos el objeto datetime
            except ValueError:
                # Si la conversión falla, significa que la fecha no es válida
                print("¡Error! La fecha no es válida. Asegúrate de que sea en formato aaaa-mm-dd.")
        else:
            print("¡Error! La fecha debe tener el formato aaaa-mm-dd.")
            
def valida_texto(texto):
    """
    Solicita al usuario que ingrese un número texto válido.
    
    Esta función sigue solicitando la entrada hasta que el usuario ingrese un texto válido.
    
    Args:
        texto (str): El mensaje que se le muestra al usuario para pedir la entrada.
        
    Returns:
        str: El texto ingresado por el usuario.
        
    """
    while True:
        entrada = input(texto)
        try:
            # Intentamos convertir la entrada a un entero
            numero = int(entrada)
            print("¡Error! Se ingresaron números en lugar de texto.")
        except ValueError:
            # Si ocurre un error (por ejemplo, la entrada no es un número entero)
           
            return entrada  # Si la conversión es exitosa, retornamos el número