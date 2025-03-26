from modulos.modelo import InterfazModeloSimulacion
from modulos.animador import Animador
import matplotlib.pyplot as plt
import numpy as np


class ControladorDeSimulador:
    
    def __init__(self):
        self.__interfaz = InterfazModeloSimulacion()
        self.__animador = Animador(p_func_ani = self._actualizar)
        
    def fijar_parametros_simulacion(self):
        self.__interfaz.cargar_parametros_simulacion()
    
    def _actualizar(self, frame, p_scatter):
        self.__interfaz.simular_un_paso()
        S = self.__interfaz.devolver_datos_semb()
        p_scatter.set_facecolors(S["color"])
        p_scatter.set_offsets(S["position"])
        print(S)
        
        # M = self.__interfaz.devolver_datos_MOs()
        # p_scatter.set_facecolors(M["color"])
        # p_scatter.set_offsets(M["position"])
        
        # A = self.__interfaz.devolver_datos_alimento()
        
        # posiciones = np.concatenate([S["position"], M["position"], A["position"]])
        # colores = np.concatenate([S["color"], M["color"], A["color"]])
        
        # p_scatter.set_facecolors(colores)
        # p_scatter.set_offsets(posiciones)
    
        return (p_scatter,)

    def simular_y_graficar(self):
        self.__interfaz.cargar_parametros_simulacion()
        self.__animador.animar()
    
    def pausar_simulacion(self):
        self.__animador.pausar()
    
    def continuar_simulacion(self):
        self.__animador.continuar()
    
        
if __name__ == "__main__":
    cs = ControladorDeSimulador()
    cs.simular_y_graficar()
    