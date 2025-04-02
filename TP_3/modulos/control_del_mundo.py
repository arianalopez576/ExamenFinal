from modulos.sembrador import Sembrador 
from modulos.poblacion_MO import Poblacion_MO
from modulos.gestor_de_alimento import Gestor_de_Alimento
from modulos.poblacion_sembradores import Poblacion_Sembradores
from datos.parametros_de_simulacion import Parametros_de_Simulacion  
 
import random

class Mundo:    
    def __init__(self):
        self.__parametros = Parametros_de_Simulacion()
        self.__gestor_de_alimento = Gestor_de_Alimento(self.__parametros)
        self.__poblacion_MO = Poblacion_MO()
        self.__poblacion_sembradores = Poblacion_Sembradores()
        self.__territorio = [0 for i in range(self.__parametros.dic_parametros['max_filas']) for j in range(self.__parametros.dic_parametros['max_columnas'])]
        self.__epoca = 0
        
    def vivir(self):
        epoca_reproduccion = False
        semb = Sembrador()
        self.__fila, self.__columna = semb.devolver_posicion()
        
        #epoca de reproduccion
        if self.__epoca != 0 and self.__epoca % self.__parametros.dic_parametros['epoca_rep'] == 0:
            epoca_reproduccion = True
       
        #invierno, se vacian todas las celdas de comida
        # if random.random()*100 <= int(self.__parametros.dic_parametros['invierno']):
        if self.__epoca % 10 == 0:
            self.__invierno()
            
        for sembrador in self.__poblacion_sembradores.devolver_lista_sem():
            sembrador.sembrar_alimento(self.__gestor_de_alimento) #esta funcion siembra y mueve al sembrador
            
        for mo in self.__poblacion_MO.devolver_lista_MO(): 
            mo.moverse(self.__epoca, self.__gestor_de_alimento)
            mo.comer(self.__gestor_de_alimento)
            
        if epoca_reproduccion == True:
            MOs = random.sample(self.__poblacion_MO.get_MOs_vivos(),2) #random sample devuelve elementos de la lista sin repetir
            MO1,MO2 = MOs[0],MOs[1]
            for i, mo in enumerate(self.__poblacion_MO.devolver_lista_MO()):
                if mo.verificar_vida() == False:
                    MOs = random.sample(self.__poblacion_MO.get_MOs_vivos(),2) #random sample devuelve elementos de la lista sin repetir
                    MO1,MO2 = MOs[0],MOs[1]
                    MO_hijo = MO1.reproduccion(MO2)
                    self.__poblacion_MO.set_MO(MO_hijo, i)
                    
        self.__epoca += 1


    def retornar_epoca(self):
        return self.__epoca
    
    def retornar_parametros_simulacion(self):
        return self.__parametros.get_parametros()
    
    def modificar_parametros_simulacion(self, p_datos):
        self.__parametros = p_datos
    
    def retornar_lista_MO(self):
        return self.__poblacion_MO.devolver_lista_MO()
            
    # def retornar_MO(self,indice):
    #     return self.__poblacion_MO.devolver_MO(indice)
    
    def __invierno(self):
        self.__gestor_de_alimento.vaciar_matriz_alimento()
    
    def retornar_posiciones_MOs(self):
        return(self.__poblacion_MO.devolver_posicion_MOs())
         
    def retornar_cantidad_MOs(self):
        return (len(self.__poblacion_MO.devolver_lista_MO()))
    
    # def retornar_cantidad_MO_vivos(self):
    #     MO_vivos = self.__poblacion_MO.calcular_cant_MO()
    #     return MO_vivos

    def retornar_inteligencia_promedio(self):
        return self.__poblacion_MO.calcular_inteligencia_promedio()
    
    def retornar_lista_inteligencia_MOs(self):
        return self.__poblacion_MO.crear_lista_inteligencia_MOs()
    
    def retornar_desviacion_estandar(self):
        return self.__poblacion_MO.calcular_desviacion_estandar()
    
    def retornar_lista_energia_MOs(self):
        return self.__poblacion_MO.crear_lista_energia_MOs()
    
    def retornar_posiciones_sembradores(self):
        return (self.__poblacion_sembradores.devolver_posicion_sembradores())
    
    def retornar_cantidad_sembradores(self):
        return (self.__poblacion_sembradores.calcular_cant_sembradores())
         
    def retornar_inteligencia_individual(self, indice):
        lista_MO = self.__poblacion_MO.devolver_lista_MO()
        return lista_MO[indice].devolver_inteligencia()
         

    def retornar_posicion_sembrador(self, indice_sem):
        lista_sembradores = self.__poblacion_sembradores.devolver_lista_sem()
        fila_sembrador = lista_sembradores[indice_sem].get_fila() 
        columna_sembrador = lista_sembradores[indice_sem].get_columna()
        return fila_sembrador, columna_sembrador   
    
    
    def retornar_datos_alimento(self):
        """ se debe devolver posiciones f c y cantidad de alimento"""
        return self.__gestor_de_alimento.retornar_posicion_y_cantidad_alimento()

   
# if __name__ == '__main__':
#     ps = Parametros_de_Simulacion
#     mundo = Mundo()
#     print('el mundo comienza')
#     mundo.vivir()
#     print(mundo.retornar_epoca())
    
#     mundo.vivir()
#     print(mundo.retornar_epoca())
    
#     mundo.vivir()
#     print(mundo.retornar_epoca())
    
#     mundo.vivir()
#     print(mundo.retornar_epoca())
    
    
    
    