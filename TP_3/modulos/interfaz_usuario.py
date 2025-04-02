from modulos.control_del_mundo import Mundo
from modulos.archivo_json import Archivo_Json
from modulos.controlador import ControladorDeSimulador
from modulos.archivo_pdf import Archivo_PDF
from modulos.archivo_html import Archivo_Html

import os

class InterfazUsuario:
    
    def __init__(self):
        self.__archivo_parametros = Archivo_Json()
        self.__mundo = Mundo()
        self.__parametros = self.__mundo.retornar_parametros_simulacion()
        self.__control_simulador = ControladorDeSimulador()
        self.__informe_datos_pdf = Archivo_PDF()
        self.__informe_datos_html = Archivo_Html()
    
    def poner_funcionamiento(self):
        while (True):
            for _ in range(20):
                self.__control_simulador.simular_y_graficar()
            print('''¿Desea continuar? S/N
                  ''')
            op_cont = input(str())
            if op_cont == 'N' or op_cont == 'n':
                self.pausar()
                break
    
    def modificar_param(self):
        menu_anterior = True
        while menu_anterior == True:
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
                  0- Volver al menu anterior
                  ''')
        
            op_modif = int(input())
            
            if 1<= op_modif <= 15:
                print('Ingrese el nuevo valor')
                valor_modificar = int(input())
                for i, clave in enumerate(self.__parametros.keys()):
                    if i == op_modif - 1:
                        self.__parametros[clave] = valor_modificar
                        print('Valor modificado:', clave, valor_modificar)
                        break
            elif op_modif == 0:
                menu_anterior = False
                
            else:
                print('Error, ingrese la opcion nuevamente')
    
    def leer_param_archi(self):
        cwd = os.getcwd()  #Devuelve la ubicacion de carpetas
        files = os.listdir(cwd)  # Devuelve los archivos en esa ubicacion
        print("Files in %r: %s" % (cwd, files))
        
        print('Ingrese el nombre del archivo que desea leer')
        nom_archi = input()
        nuevos_datos = self.__archivo_parametros.leer_archi_json(nom_archi)
        
        self.__mundo.modificar_parametros_simulacion(nuevos_datos)
    
    def pausar(self):
        en_pausa = bool()
        self.__control_simulador.pausar_simulacion()
        en_pausa = True
        return en_pausa
    
    def continuar(self):
        self.__control_simulador.continuar_simulacion()
    
    def guardar_parametros_archivo(self):
        print('Ingrese el nombre del archivo que desea crear')
        nom_archi = input()
        self.__archivo_parametros.escribir_archi_json(nom_archi, self.__parametros)    
        
    def interaccion_usuario(self):
        
        while(True):
    
            print('''
                  Elija lo que desea realizar:
                      
                      Opcion 1: Poner en funcionamento el mundo con parámetros iniciales
                      Opcion 2: Modificar los parametros de la simulacion
                      Opcion 3: Poner en funcionamiento el mundo con parametros del archivo
                      Opcion 4: Guardar los parametros de simulacion en un archivo JSON
                      Opcion 5: Guardar los datos de la simulacion en un archivo PDF
                      Opcion 6: Guardar los datos de la simulacion en un archivo HTML
                  
                  ''')
                  
            opcion_elegida = int(input())
            
            if opcion_elegida == 1:
                self.poner_funcionamiento()
                    
            elif opcion_elegida == 2:
                while (True):
                    print('''
                          1- Realizar modificaciones de parametros
                          2-No realizar mas modificaciones, poner el mundo en funcionamiento''')
                    opcion = int(input())
                    if opcion == 1:
                        self.modificar_param()
                    elif opcion == 2:
                        self.poner_funcionamiento()
                    else:
                        print('Error, ingrese nuevamente')
                
                
            elif opcion_elegida == 3:
                self.leer_param_archi()
                self.poner_funcionamiento()
            
            elif opcion_elegida == 4:
                self.pausar()
                self.guardar_parametros_archivo()
                
            elif opcion_elegida == 5:
                self.pausar()
                print('Ingrese el nombre del archivo que desea crear')
                nom_archi = input()
                self.__informe_datos_pdf.escribir_archivo(nom_archi, 'Datos de la simulacion', self.__parametros, self.__mundo.retornar_epoca(), self.__mundo.retornar_inteligencia_MOs(), self.__mundo.retornar_inteligencia_promedio())
                
            elif opcion_elegida == 6:
                self.pausar()
                print('Ingrese el nombre del archivo que desea crear')
                nom_archi = input()
                datos = []
                # [1] epoca
                # [2] lista inteligencia
                # [3] inteligencia promedio
                # [4] desviacion estandar 
                datos.append(self.__mundo.retornar_epoca())
                datos.append(self.__mundo.retornar_lista_inteligencia_MOs())
                datos.append(self.__mundo.retornar_inteligencia_promedio())
                datos.append(self.__mundo.retornar_desviacion_estandar())
                self.__informe_datos_html.escribir_archivo(nom_archi, self.__parametros, datos)
                 
            else:
                print('Error, ingrese nuevamente')
                opcion_elegida = True
           
        
        