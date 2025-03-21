from modulos.control_del_mundo import Mundo
from datos.parametros_de_simulacion import Parametros_de_Simulacion
from modulos.archivo_json import Gestor_de_Archivo_de_Param
from modulos.controlador import ControladorDeSimulador

import os

class InterfazUsuario:
    
    def __init__(self):
        self.__parametros = Parametros_de_Simulacion()
        self.__archi_param = Gestor_de_Archivo_de_Param()
        self.__mundo = Mundo(self.__parametros)
        self.__control = ControladorDeSimulador()
    
    def poner_funcionamiento(self):
        while (True):
            for _ in range(10):
                self.__control.simular_y_graficar() #esto solo grafica MO, falta incluir los otros
            print('''¿Desea continuar? S/N
                  ''')
            op_cont = input(str())
            if op_cont == 'N' or op_cont == 'n':
                break
    
    def modificar_param(self):
        lista = ['max_filas', 'max_columnas', 'cant_MO_inicial', 'energia_inicial', 'energia_max', 'cant_max_alimento_ingerir', 'energia_perdida', 'cant_semb_inicial', 'alimento_siembra', 'epoca_rep', 'prob_mutacion', 'prob_cambio_semb', 'prob_cambio_MO', 'cant_max_alimento_celda', 'invierno']
    
        while (True):
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
                  0- No realizar mas modificaciones, poner el mundo en funcionamiento
                  ''')
        
            op_modif = int(input())
            if 1<= op_modif <= 15:
                for pos_par, dato in self.__parametros.dic_parametros.items():
                    for i in range(0, 15):
                        if i == op_modif - 1:
                            pos_par_modif = lista[i]
                            if pos_par == pos_par_modif:
                                self.__parametros.dic_parametros[pos_par_modif] = int(input('Ingrese el dato'))
                                print('Usted modifico: ', pos_par, self.__parametros.dic_parametros[pos_par_modif])
            elif op_modif == 0:
                break
            else:
                print('Error, ingrese la opcion nuevamente')
    
    def leer_param_archi(self):
        cwd = os.getcwd()  #Devuelve la ubicacion de carpetas
        files = os.listdir(cwd)  # Devuelve los archivos en esa ubicacion
        print("Files in %r: %s" % (cwd, files))
        
        print('Ingrese el nombre del archivo que desea leer')
        nom_archi = input()
    
        self.__parametros.dic_parametros = self.__archi_param.leer_archi_json(nom_archi)
    
    def pausar(self):
        self.__control.pausar_simulacion()
    
    def guardar_datos_archivo(self):
        print('Ingrese el nombre del archivo que desea crear')
        nom_archi = input()
        self.__archi_param.escribir_archi_json(nom_archi, self.__parametros)
    
    def interaccion_usuario(self):
        
        while(True):
    
            print('''
                  Elija lo que desea realizar:
                      
                      Opcion 1: Poner en funcionamento el mundo con parámetros iniciales
                      Opcion 2: Modificar los parametros de la simulacion
                      Opcion 3: Poner en funcionamiento el mundo con parametros del archivo
                      Opcion 4: Guardar los datos en un archivo
                  
                  ''')
                  
            opcion_elegida = int(input())
            
            if opcion_elegida == 1:
                self.poner_funcionamiento()
                    
            elif opcion_elegida == 2:
                self.modificar_param()
                self.poner_funcionamiento()
                
            elif opcion_elegida == 3:
                self.leer_param_archi()
                self.poner_funcionamiento()
            
            elif opcion_elegida == 4:
                self.pausar()
                self.guardar_datos_archivo()
                 
            else:
                print('Error, ingrese nuevamente')
                opcion_elegida = True
           
        
        