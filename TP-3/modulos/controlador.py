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
        R = self.__interfaz.devolver_datos_semb()
        p_scatter.set_facecolors(R["color"])
        p_scatter.set_offsets(R["position"])
        
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
    