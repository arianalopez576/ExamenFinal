import random
from datos.parametros_de_simulacion import Parametros_de_Simulacion
from modulos.gestor_de_alimento import Gestor_de_Alimento

parametros_de_simulacion = Parametros_de_Simulacion()
class Sembrador: 
    def __init__(self):
        self.__direccion_movimiento = random.randint(0,7)
        self.__fila = random.randint(0, parametros_de_simulacion.dic_parametros['max_filas']-1) 
        self.__columna = random.randint(0, parametros_de_simulacion.dic_parametros['max_columnas']-1)
   
    def set_posicion(self, p_fila, p_columna):
        self.__fila = p_fila
        self.__columna = p_columna 
   #pero la posicion del sembrador no es random? por que tengo un set?
    
    def devolver_posicion_sembrador(self):
        return self.__fila, self.__columna
    
    def movimiento_sembrador (self):
        buscar_posicion = True
        while (buscar_posicion == True):
            if random.random()*100 < parametros_de_simulacion.dic_parametros['prob_cambio_semb']:
                self.__direccion_movimiento = random.randint(0,7)
            
            fila_nueva = self.__fila + parametros_de_simulacion.mov_relativo[self.__direccion_movimiento][0]
            columna_nueva = self.__columna + parametros_de_simulacion.mov_relativo[self.__direccion_movimiento][1]
            if self.__comprobar_dimension_fila_columna(fila_nueva, columna_nueva) == True:
               self.__fila = fila_nueva
               self.__columna = columna_nueva
               buscar_posicion = False 
            else:
               buscar_posicion = True


    def __comprobar_dimension_fila_columna(self, fila_nueva, columna_nueva):
        if (fila_nueva >= 0 and fila_nueva < parametros_de_simulacion.dic_parametros['max_filas']) and (columna_nueva >= 0 and columna_nueva < parametros_de_simulacion.dic_parametros['max_columnas']):
            return True 
        else:
            return False
        
        
    def sembrar_alimento (self , gestor_alimento):
        gestor_alimento.agregar_alimento_en_posicion(self.__fila, self.__columna)
        self.movimiento_sembrador()
        #el self movimiento para que se mueva luego de sembrar
 
'''
if __name__=="__main__":
    s = Sembrador()
    s.set_posicion(20, 59)
    fila, columna = s.devolver_posicion_sembrador()
    ga = Gestor_de_Alimento(parametros_de_simulacion, fila, columna)
  
    print('pos inicial', s.devolver_posicion_sembrador())
    s.sembrar_alimento(ga)
    print('se movio', s.devolver_posicion_sembrador())
    print(ga.retornar_alimento_en_posicion())
    '''