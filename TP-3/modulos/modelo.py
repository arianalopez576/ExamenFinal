
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
        self.__data_arreglo_comida = None
        self.__mundo = Mundo(ps)
             
    def cargar_parametros_simulacion(self):
        self.__data_arreglo_sembradores = self.__mundo.retornar_datos_sembradores()
        self.__data_arreglo_MOs = self.__mundo.retornar_datos_MOs()
        self.__epoca = 0
        
        
    def simular_un_paso(self):
        self.__mundo.vivir()
        
        '''simular un paso de los sembradores 
            i es un indice para recorrer los sembradores '''
         
        #le saco la transparencia self.__data_arreglo_sembradores["color"][:, 3] = np.maximum(0, self.__data_arreglo_sembradores["color"][:, 3] - 1 / len(self.__data_arreglo_sembradores))
    

        i = self.__epoca % len(self.__data_arreglo_sembradores)
        self.__data_arreglo_sembradores["position"][i] = np.random.uniform(0, 100, 2)
        self.__data_arreglo_sembradores["color"][i, 3] = 1
        
        j = self.__epoca % len(self.__data_arreglo_MOs)
        self.__data_arreglo_MOs["position"][j] = np.random.uniform(0, 100, 2)
        self.__data_arreglo_MOs["energia"][j] -= 0.1
        self.__data_arreglo_MOs["color"][j, 3] = 1
        self.__data_arreglo_MOs["color"][j, 3] = max(0, self.__data_arreglo_MOs["energia"][j])
        
        self.__epoca += 1
            
    def get_epoca(self):
        return self.__epoca
        
    def devolver_datos_MOs(self):
        return self.__data_arreglo_MOs

    def devolver_datos_semb(self):
        return self.__data_arreglo_sembradores
    
    # def devolver_datos_comida(self):
    #     return self.__data_arreglo_comida
    
# if __name__ == '__main__':
#     ps = Parametros_de_Simulacion()
#     mod_sim = InterfazModeloSimulacion()
    
#     mod_sim.cargar_parametros_MO()
#     print('inicial', mod_sim.devolver_datos_MO())
#     print('epoca1', mod_sim.get_epoca())
    
#     mod_sim.simular_un_paso()
#     print('luego', mod_sim.devolver_datos_MO())
#     print('epoca2', mod_sim.get_epoca())