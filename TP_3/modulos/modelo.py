
from modulos.control_del_mundo import Mundo

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as animation


class InterfazModeloSimulacion:
    
    def __init__(self):
        self.__data_arreglo_MOs = None
        self.__data_arreglo_sembradores = None
        self.__data_arreglo_alimento = None
        self.__mundo = Mundo()
        self.__epoca = self.__mundo.retornar_epoca()
             
    def cargar_parametros_simulacion(self):
        #carga de datos sembradores
        cant_semb = self.__mundo.retornar_cantidad_sembradores()
        self.__data_arreglo_sembradores = np.zeros(cant_semb, dtype =[("position", float, (2,)), ("color", float, (4,))])
        
        self.__data_arreglo_sembradores["position"] = self.__mundo.retornar_posiciones_sembradores()
        self.__data_arreglo_sembradores["color"][:, 0] = 0
        self.__data_arreglo_sembradores["color"][:, 1] = 0
        self.__data_arreglo_sembradores["color"][:, 2] = 1 #color azul
        self.__data_arreglo_sembradores["color"][:, 3] = 1 #alpha
        
        #carga de datos MO
        parametros = self.__mundo.retornar_parametros_simulacion()
        cant_MOs = self.__mundo.retornar_cantidad_MOs()
        max_energia = int(parametros['energia_max'])
        lista_energia = self.__mundo.retornar_lista_energia_MOs()
        self.__data_arreglo_MOs = np.zeros(cant_MOs, dtype = [("position", float, (2,)), ("color", float, (4,))]) 
        
        self.__data_arreglo_MOs["position"] = self.__mundo.retornar_posiciones_MOs()
        self.__data_arreglo_MOs["color"][:, 0] = 0
        self.__data_arreglo_MOs["color"][:, 1] = 1 #color verde
        self.__data_arreglo_MOs["color"][:, 2] = 0
        for i in range (cant_MOs):
            self.__data_arreglo_MOs["color"][i, 3] = max(0, min(lista_energia[i]/max_energia, 1))
        
        #arreglo para guardar datos alimento
        cant_celdas_con_alimento = len(self.__mundo.retornar_datos_alimento())
        self.__data_arreglo_alimento = np.zeros(cant_celdas_con_alimento, dtype = [("position", float, (2,)), ("color", float, (4,))])
        
        self.__epoca = 0
        
        
    def simular_un_paso(self):
        self.__mundo.vivir()
        self.cargar_parametros_simulacion()
        
        #carga de datos alimento
        parametros = self.__mundo.retornar_parametros_simulacion()
        cant_max_alimento_por_celda = int(parametros['alimento_siembra'])
        datos_alimento = np.array(self.__mundo.retornar_datos_alimento())
        self.__data_arreglo_alimento["position"][:, 0] = datos_alimento[:, 0]
        self.__data_arreglo_alimento["position"][:, 1] = datos_alimento[:, 1]
        self.__data_arreglo_alimento["color"][:, 0] =  1 #color rojo
        self.__data_arreglo_alimento["color"][:, 1] =  0
        self.__data_arreglo_alimento["color"][:, 2] =  0
      
        self.__data_arreglo_alimento["color"][:, 3] = np.clip(datos_alimento[:, 2] / cant_max_alimento_por_celda, 0, 1)
            
            
        self.__epoca += 1
            
        
    def get_epoca(self):
        return self.__epoca
        
    def devolver_datos_MOs(self):
        return self.__data_arreglo_MOs

    def devolver_datos_semb(self):
        return self.__data_arreglo_sembradores
    
    def devolver_datos_alimento(self):
        return self.__data_arreglo_alimento
    
    
# from datos.parametros_de_simulacion import Parametros_de_Simulacion    
# if __name__ == '__main__':
#     ps = Parametros_de_Simulacion()
#     mod_sim = InterfazModeloSimulacion()
#     mod_sim.simular_un_paso()
    
    # mod_sim.cargar_parametros_simulacion()
    # print('inicial:', mod_sim.devolver_datos_alimento())
    # print('epoca:', mod_sim.get_epoca())
    
    # mod_sim.simular_un_paso()
    # print('luego:', mod_sim.devolver_datos_alimento())
    # print('epoca:', mod_sim.get_epoca())
    
    # print('arreglo alimento', mod_sim.devolver_datos_alimento())
    
    