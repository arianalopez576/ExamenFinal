from modulos.sembrador import Sembrador 
from datos.parametros_de_simulacion import Parametros_de_Simulacion
from modulos.gestor_de_alimento import Gestor_de_Alimento
p_s = Parametros_de_Simulacion()

class Poblacion_Sembradores:
    
    def __init__(self):
        
        self.__lista_sembradores = []
        for _ in range(p_s.dic_parametros['cant_semb_inicial']):
            sembrador = Sembrador()
            self.__lista_sembradores.append(sembrador)
        # ver esto
        
    def devolver_lista_sem(self):
        return self.__lista_sembradores
    
    #devuelve una lista con las posiciones de todos los sembradores
    def devolver_posicion_sembradores(self):
        lista_posiciones = []
        for sembrador in self.__lista_sembradores:
            lista_posiciones.append(sembrador.devolver_posicion())
        return (lista_posiciones)
    
    def devolver_alimento(self, p_fila, p_columna):
        for sembrador in self.__lista_sembradores:
            return sembrador.devolver_cant_comida(p_fila, p_columna)     
    
    def calcular_cant_sembradores(self):
        return len(self.__lista_sembradores)
    
   
    
# if __name__ == '__main__':
#     ga = Gestor_de_Alimento(p_s)
#     s = Sembrador()
#     s.sembrar_alimento(ga)
#     s.sembrar_alimento(ga)
#     s.sembrar_alimento(ga)
#     poblacion_semb = Poblacion_Sembradores()
#     print(poblacion_semb.devolver_posicion_sembradores())
#     print(poblacion_semb.calcular_cant_sembradores())
    
#     print('datos_comida', poblacion_semb.retornar_posicion_y_cantidad_alimento(ga))
