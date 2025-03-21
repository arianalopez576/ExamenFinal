from modulos.microorganismo import Microorganismo
from datos.parametros_de_simulacion import Parametros_de_Simulacion
p_s = Parametros_de_Simulacion()


class Poblacion_MO:     
    
    def __init__(self):
        self.__cant_MO = int()  
        self.__lista_MO = []
        #se inicializa la lista de MO determinada por el parametro
        for i in range(p_s.dic_parametros['cant_MO_inicial']):
            MO = Microorganismo()
            self.__lista_MO.append(MO)
        
    #funcion para agregar MO que nacen
    def set_MO(self, MO, indice = None):
        if indice is None:
            self.__lista_MO.append(MO)
        else:
            self.__lista_MO[indice] = MO
      
    def get_MOs_vivos(self):
        MOs_vivos = []
        for mo in self.__lista_MO:
            if mo.verificar_vida() == True:
                MOs_vivos.append(mo)
        
        return MOs_vivos
    
    def devolver_MO(self, p_indice):
        return self.__lista_MO[p_indice]
    
    def devolver_lista_MO(self):
        return self.__lista_MO
    
    def calcular_cant_MO(self):
        MO_vivos = 0
        for MO in self.__lista_MO:
            if MO.verificar_vida() == True:
                MO_vivos += 1
        return MO_vivos
    
    #para calcular la inteligencia, tambien deberia verificar que los MO esten vivos?
    def calcular_inteligencia_promedio(self):
        inteligencia_total = 0
        for MO in self.__lista_MO:
            inteligencia_total += MO.devolver_inteligencia()
        inteligencia_prom = inteligencia_total/self.calcular_cant_MO() 
        return inteligencia_prom
        

    
    