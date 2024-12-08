#Yurany Mosquera Palacios, Adrian Martinez Esteban

from FuncionesTF import * #Importo todas las funciones del archivo

#Solicitar al usuario por teclado sus datos de ingreso
usuario=input("Ingrese su usuario: ")
clave=input("Ingrese su clave: ")

[login,rol]=verificar_login(usuario, clave)

if login:
    print("\nInicio de sesión correcto")
else:
    print("\nUsuario o contraseña invalida")
    
while login:
    
    if rol=='administrador':
        print("\n1. Añadir nuevo usuario \n2. Consultar los usuarios registrados \n3. Modificar usuarios \n4. Eliminar usuarios \n5. Crear paciente \n6. Eliminar paciente \n7. Salir")
        seleccion=valida_numero("Seleccione una opción: ")
        if int(seleccion)==1:
            user_id=valida_numero("Ingrese el ID del nuevo usuario: ")
            username=valida_texto("Ingrese el nombre de usuario: ")
            password=input("Ingrese la clave: ")
            role=valida_texto("Ingrese el rol (administrador,tecnico o medico): ")
            agregar_usuario(user_id,username,password,role)
        elif int(seleccion)==2:
            consultar_usuarios()
        elif int(seleccion)==3:
            user_id=valida_numero("Ingrese el ID del usuario a modificar: ")
            user_id2=valida_numero(("Ingrese el nuevo ID: "))
            username=valida_texto("Ingrese el nuevo nombre de usuario: ")
            password=input("Ingrese la nueva clave: ")
            role=valida_texto("Ingrese el nuevo rol (administrador,tecnico o medico): ")
            actualizar_usuario(user_id,user_id2,username,password,role)
        elif int(seleccion)==4:
            user_id=valida_numero(("Ingrese el ID del usuario a eliminar: "))
            eliminar_usuario(user_id)
        elif int(seleccion)==5:
            ID=valida_numero("Ingrese el ID del nuevo paciente: ")
            nombre=valida_texto("Ingrese el nombre de paciente: ")
            edad=valida_numero("Ingrese la edad del paciente: ")
            genero=valida_texto("Ingrese el genero del paciente (masculino, femenino u otro): ")
            historial=valida_texto("Ingrese el historial del paciente: ")
            agregar_paciente(ID, nombre, edad, genero, historial)
        elif int(seleccion)==6:
             ID=valida_numero(("Ingrese el ID del paciente a eliminar: "))
             eliminar_paciente(ID)
        elif int(seleccion)==7:
            break
        else:
            print("Opción seleccionada no válida")
    
    if rol=='medico':
        print("\n1. Ver pacientes \n2. Actualizar pacientes\n3. Ver diagnósticos de pacientes \n4. Actualizar diagnósticos de pacientes \n5. Consultar información de imágenes diagnósticas \n6. Generar reporte médico \n7. Salir")
        seleccion=valida_numero("\nSeleccione una opción: ")
        if int(seleccion)==1:
            user_id=valida_numero(("\nIngrese el ID del paciente: "))
            ver_pacientes(user_id)
        elif int(seleccion)==2:
            ID=valida_numero(("Ingrese el ID del paciente a modificar: "))
            ID2=valida_numero(("Ingrese el nuevo ID del paciente: "))
            nombre=valida_texto("Ingrese el nuevo nombre del paciente: ")
            edad=valida_numero(("Ingrese la edad del paciente: "))
            genero=valida_texto("Ingrese el genero (masculino, femenino, otros): ")
            historial=valida_texto("Ingrese el nuevo historial del paciente: ")
            actualizar_paciente(ID,ID2,nombre,edad,genero,historial)
            actualizar_id_diagnostico(ID,ID2)
            actualizar_id_pacientes_reportes_medicos(str(ID,),str(ID2))
            actualizar_id_pacientes_reportes_tecnicos(str(ID,),str(ID2))
        elif int(seleccion)==3:
            user_id=valida_numero(("\nIngrese el ID del paciente: "))
            ver_diagnostico(user_id)
        elif int(seleccion)==4:
            ID=valida_numero(("Ingrese el ID del paciente a modificar diagnóstico: "))
            tipo_imagen=valida_texto("Ingrese el tipo de imagen (mri,ct,rx): ")
            resultado_IA=valida_numero("Ingrese el resultado generado por IA en %: ")
            fecha_imagen=valida_fechas("Ingrese fecha de toma de la imagen (aaaa-mm-dd): ")
            fecha_diagnostico=valida_fechas("Ingrese fecha del diagnóstico (aaaa-mm-dd): ")
            estado=valida_texto("Ingrese estado (revisado, no revisado): ")
            actualizar_diagnostico(ID,tipo_imagen,resultado_IA,fecha_imagen,fecha_diagnostico,estado)
        elif int(seleccion)==5:
            id_paciente=valida_numero(("Ingrese el ID del paciente a consultar: "))
            ver_imagen(id_paciente)
        elif int(seleccion)==6:
            user_id=valida_numero("\nIngrese el ID del paciente: ")
            resultado=ver_diagnostico(user_id)
            tipo_imagen=resultado[0][1]
            resultado_IA=resultado[0][2]
            fecha_imagen=resultado[0][3]
            fecha_diagnostico=resultado[0][4]
            estado='revisado'
            notas=valida_texto("\nIngrese comentarios del diagnóstico: ")
            crear_reporte(user_id,tipo_imagen,resultado_IA,fecha_imagen,fecha_diagnostico,estado,notas)
            actualizar_estado(user_id,estado)
        elif int(seleccion)==7:
            break
        
    if rol=='tecnico':
        print("\n1. Ingresar datos de imágenes diagnósticas de pacientes \n2. Consultar datos de imágenes diagnósticas de pacientes\n3. Actualizar datos de imágenes diagnósticas de pacientes \n4. Eliminar datos de imágenes diagnósticas de pacientes \n5. Salir")
        seleccion=valida_numero("\nSeleccione una opción: ")
        if int(seleccion)==1:
        
            id_imagen=valida_texto("\nIngrese el ID de la imagen: ")
            id_paciente=valida_numero("Ingrese el ID del paciente: ")
            fecha=valida_fechas("Ingrese fecha de toma de la imagen (aaaa-mm-dd): ")
            tipo_imagen=valida_texto("Ingrese el tipo de imagen (MRI,CT,RX): ")
            parte_cuerpo=valida_texto("Ingrese parte del cuerpo: ")
            imagen_path=valida_texto("Ingrese el path de la imagen: ")
            condicion_sugerida=valida_texto("Ingrese condición sugerida: ")
            probabilidad=valida_numero("Ingrese el resultado generado por IA en %: ")
            notas=''
            id_tecnico=valida_texto("Ingrese identificación del técnico: ")
            fecha_nota=valida_fechas("Ingrese fecha de la nota (aaaa-mm-dd): ")
            texto=valida_texto("Ingrese sus comentarios: ")
            
            agregar_imagen(id_imagen,id_paciente,fecha,tipo_imagen,parte_cuerpo,imagen_path,condicion_sugerida,probabilidad,notas,id_tecnico,fecha_nota,texto)
            
        elif int(seleccion)==2:
            id_paciente=valida_numero("Ingrese el ID del paciente a consultar: ")
            ver_imagen(id_paciente)
            
        elif int(seleccion)==3:
            
            id_imagen=valida_texto("\nIngrese el ID de la imagen: ")
            id_paciente=valida_numero("Ingrese el ID del paciente: ")
            id_paciente2=valida_numero("Ingrese el nuevo ID del paciente: ")
            fecha=valida_fechas("Ingrese fecha de toma de la imagen (aaaa-mm-dd): ")
            tipo_imagen=valida_texto("Ingrese el tipo de imagen (MRI,CT,RX): ")
            parte_cuerpo=valida_texto("Ingrese parte del cuerpo: ")
            imagen_path=valida_texto("Ingrese el path de la imagen: ")
            condicion_sugerida=valida_texto("Ingrese condición sugerida: ")
            probabilidad=valida_numero("Ingrese el resultado generado por IA en %: ")
            notas=''
            id_tecnico=valida_texto("Ingrese identificación del técnico: ")
            fecha_nota=valida_fechas("Ingrese fecha de la nota (aaaa-mm-dd): ")
            texto=valida_texto("Ingrese sus comentarios: ")
            actualizar_imagen(id_imagen,id_paciente,id_paciente2,fecha,tipo_imagen,parte_cuerpo,imagen_path,condicion_sugerida,probabilidad,notas,id_tecnico,fecha_nota,texto)
            
        elif int(seleccion)==4:
            id_paciente=valida_numero("Ingrese el ID del paciente a eliminar: ")
            eliminar_imagen(id_paciente)
        elif int(seleccion)==5:
            break
    
    