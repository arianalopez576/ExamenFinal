
from datos.parametros_de_simulacion import Parametros_de_Simulacion
from modulos.control_del_mundo import Mundo

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as animation


ps = Parametros_de_Simulacion()

class InterfazModeloSimulacion:
    
    def __init__(self):
        self.__data_arreglo_MOs = None
        self.__epoca = None
        self.__data_arreglo_sembradores = None
        self.__data_arreglo_alimento = None
        self.__mundo = Mundo(ps)
             
    def cargar_parametros_simulacion(self):
        self.__data_arreglo_sembradores = self.__mundo.retornar_datos_sembradores()
        self.__data_arreglo_MOs = self.__mundo.retornar_datos_MOs()
        self.__data_arreglo_alimento = self.__mundo.retornar_datos_alimento()
        self.__epoca = 0
        
        
    def simular_un_paso(self):
        self.__mundo.vivir()
        
        '''simular un paso de los sembradores 
            i es un indice para recorrer los sembradores '''
       
        
        self.__data_arreglo_sembradores = self.__mundo.retornar_datos_sembradores()
        # print (self.__data_arreglo_sembradores)
        
        # '''simular un paso de los microscopios y modificar su tranparencia'''
        # j = self.__epoca % len(self.__data_arreglo_MOs)
        # self.__data_arreglo_MOs["position"][j] = np.random.uniform(0, 100, 2)
        # self.__data_arreglo_MOs["energia"][j] -= 0.1
        # self.__data_arreglo_MOs["color"][j, 3] = 1
        #self.__data_arreglo_MOs["color"][j, 3] = max(0, self.__data_arreglo_MOs["energia"][j].item())
        
        # '''actualizacion del alimento'''
        # k = self.__epoca % len(self.__data_arreglo_alimento)
        # fila = int(self.__data_arreglo_alimento["position"][k, 0])
        # columna = int(self.__data_arreglo_alimento["position"][k, 1])
        
        # cant_max_alimento = int(ps.dic_parametros["alimento_siembra"])
        # self.__data_arreglo_alimento["cantidad"][k] = 50 #self.__mundo.retornar_cant_alimento(fila, columna)
        # self.__data_arreglo_alimento["color"][k, 3] = (self.__data_arreglo_alimento["cantidad"][k].item()/cant_max_alimento)
        
        self.__epoca += 1
            
    def get_epoca(self):
        return self.__epoca
        
    def devolver_datos_MOs(self):
        return self.__data_arreglo_MOs

    def devolver_datos_semb(self):
        return (self.__data_arreglo_sembradores)
    
    def devolver_datos_alimento(self):
        return self.__data_arreglo_alimento
    
if __name__ == '__main__':
    ps = Parametros_de_Simulacion()
    mod_sim = InterfazModeloSimulacion()
    
    mod_sim.cargar_parametros_simulacion()
    print('inicial', mod_sim.devolver_datos_alimento())
    print('epoca1', mod_sim.get_epoca())
    
    mod_sim.simular_un_paso()
    print('luego', mod_sim.devolver_datos_alimento())
    print('epoca2', mod_sim.get_epoca())