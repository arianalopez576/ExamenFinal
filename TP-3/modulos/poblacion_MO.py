from modulos.microorganismo import Microorganismo
from datos.parametros_de_simulacion import Parametros_de_Simulacion
p_s = Parametros_de_Simulacion()


class Poblacion_MO:     
    
    def __init__(self):
        self.__cant_MO = int()  
        self.__lista_MO = []
        for i in range(p_s.dic_parametros['cant_MO_inicial']):
            MO = Microorganismo()
            self.__lista_MO.append(MO)
        
    def set_MO(self, MO):
        self.__lista_MO.append(MO)
    
    #en el set MO y el init, no se está haciendo lo mismo?
    
    def devolver_MO(self,indice):
        return self.__lista_MO[indice]
    
    def devolver_lista_MO(self):
        return self.__lista_MO
    
    def calcular_cant_MO(self):
        return len(self.__lista_MO)  
    
    def calcular_inteligencia_promedio(self):
        inteligencia_total = 0
        for MO in self.__lista_MO:
            inteligencia_total += MO.devolver_inteligencia()
        inteligencia_prom = inteligencia_total/len(self.__lista_MO) 
        return inteligencia_prom
        

    
    