from modulos.sembrador import Sembrador 
from datos.parametros_de_simulacion import Parametros_de_Simulacion
p_s = Parametros_de_Simulacion()

class Poblacion_Sembradores:
    
    def __init__(self):
        
        self.__cant_sembradores = int()
        self.__lista_sembradores = []
        for i in range(p_s.dic_parametros['cant_semb_inicial']):
            sembrador = Sembrador()
            self.__lista_sembradores.append(sembrador)
        # ver esto
        
    def devolver_lista_sem(self):
        return self.__lista_sembradores
    
    def calcular_cant_sembradores(self):
        return len(self.__lista_sembradores)
    
    


