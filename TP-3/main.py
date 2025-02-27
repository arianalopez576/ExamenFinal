
from datos.parametros_de_simulacion import Parametros_de_Simulacion
from modulos.gestor_archivo_json import Gestor_de_Archivo_de_Param
from modulos.control_del_mundo import Mundo
from modulos.cromosoma import Cromosoma
from modulos.microorganismo import Microorganismo
import os
import time
p_s = Parametros_de_Simulacion()

while(True):


    print('''
          Elija lo que desea realizar:
              
              Opcion 1: Poner en funcionamente el mundo con parámetros iniciales
              Opcion 2: Modificar los parametros de la simulacion
              Opcion 3: Poner en funcionamiento el mundo con parametros del archivo
              Opcion 4: Guardar los datos en un archivo
          
          ''')
          
    opcion_elegida = int(input())
    if opcion_elegida == 1:  
        mundo = Mundo(p_s)
        while(True):
            for i in range(10):            
                mundo.vivir()
            frenar = input("Quiere frenar? (S/N): ")
            if frenar == 's' or frenar == 'S':
                nom_archi = input('Ingrese el nombre del archivo que desea crear')
                gestor_archivo = Gestor_de_Archivo_de_Param()
                ps = Parametros_de_Simulacion()
                parametros = ps.get_parametros()
                param_crear_archi = gestor_archivo.escribir_archi_json(nom_archi, parametros)
                print("Para continuar pulse 1, y para finalizar con todo 2: ")
                while(True):
                    tecla = input()
                    if tecla == "1":
                        break
                    if tecla == "2":
                        break
                if tecla == "2":
                    break
    
    if opcion_elegida == 2:
        par_usuario = Parametros_de_Simulacion()
        lista = ['max_filas', 'max_columnas', 'cant_MO_inicial', 'energia_inicial', 'energia_max', 'cant_max_alimento_ingerir', 'energia_perdida', 'cant_semb_inicial', 'alimento_siembra', 'epoca_rep', 'prob_mutacion', 'prob_cambio_semb', 'prob_cambio_MO', 'cant_max_alimento_celda', 'invierno']
        opcion = True
        while opcion == True:
            print('''
                  Ingrese el numero del parametro que desea modificar:
                  1- Número de filas del territorio
                  2- Número de columnas del territorio
                  3- Población (número de individuos) de Microorganismos
                  4- Energía inicial de cada MO
                  5- Energía máxima de cada MO
                  6- Cantidad máxima de alimento que puede ingerir un MO
                  7- Energía que consume cada MO al desplazarse
                  8- Población (número de individuos) de Sembradores
                  9- Cantidad alimento que siembra un sembrador
                  10- Épocas de reproducción
                  11- Probabilidad de mutación
                  12- Probabilidad de cambio de dirección del sembrador
                  13- Probabilidad de cambio de dirección del MO
                  14- Cantidad máxima de alimento en cada celda del territorio
                  15- Probabilidad eliminación total del alimento (invierno)
                  -1- No realizar mas modificaciones, poner el mundo en funcionamiento
                  ''')
            
            op_modif = int(input())
            if op_modif >=0 and op_modif <= 15:
                for par, dato in par_usuario.dic_parametros.items():
                    for i in range(0, 15):
                        if i == op_modif-1:
                            par_m = lista[i]
                            if par == par_m:
                                par_usuario.dic_parametros[par_m] = int(input('Ingrese el dato'))
                                print('Usted modifico: ', par, par_usuario.dic_parametros[par_m])
            if op_modif == -1:
                break
            if op_modif < -1 or op_modif > 16:
                print('Error, ingrese la opcion nuevamente')
                opcion = True
                
            
    if opcion_elegida == 3:
        cwd = os.getcwd()  #Devuelve la ubicacion de carpetas
        files = os.listdir(cwd)  # Devuelve los archivos en esa ubicacion
        print("Files in %r: %s" % (cwd, files))
        
        print('Ingrese el nombre del archivo que desea leer')
        nom_archi = input()
        
        gestor_archivo = Gestor_de_Archivo_de_Param()
        param_archi = Parametros_de_Simulacion()
        param_archi.dic_parametros = gestor_archivo.leer_archi_json(nom_archi)
        mundo_archi = Mundo(param_archi)
        
    if opcion_elegida == 4:
        print('Ingrese el nombre del archivo que desea crear')
        nom_archi = input()
        gestor_archivo = Gestor_de_Archivo_de_Param()
        ps = Parametros_de_Simulacion()
        ps = ps.dic_parametros
        param_crear_archi = ps
        param_crear_archi = gestor_archivo.escribir_archi_json(nom_archi, param_crear_archi)
        
    if opcion_elegida < 0 or opcion_elegida > 4:
        print('Error, ingrese nuevamente')
        op_elegida = True
       