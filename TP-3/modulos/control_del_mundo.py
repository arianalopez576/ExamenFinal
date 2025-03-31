from modulos.sembrador import Sembrador 
from modulos.poblacion_MO import Poblacion_MO
from modulos.gestor_de_alimento import Gestor_de_Alimento
from modulos.poblacion_sembradores import Poblacion_Sembradores
from datos.parametros_de_simulacion import Parametros_de_Simulacion

import random

#parametros_de_simulacion.max_filas = 10  Una forma de modificarlo

class Mundo:    
    def __init__(self, p_ps):
        self.__parametros = p_ps
        self.__gestor_de_alimento = Gestor_de_Alimento(p_ps)
        self.__poblacion_MO = Poblacion_MO()
        self.__poblacion_sembradores = Poblacion_Sembradores()
        self.__territorio = [0 for i in range(p_ps.dic_parametros['max_filas']) for j in range(p_ps.dic_parametros['max_columnas'])]
        self.__epoca = 0
        
    def vivir(self):
        epoca_reproduccion = False
        semb = Sembrador()
        self.__fila, self.__columna = semb.devolver_posicion()
        
        #epoca de reproduccion
        if self.__epoca != 0 and self.__epoca % self.__parametros.dic_parametros['epoca_rep'] == 0:
            epoca_reproduccion = True
       
        #invierno, se vacian todas las celdas de comida
        if random.random()*100 <= self.__parametros.dic_parametros['invierno']:
            self.__invierno()
            
        for sembrador in self.__poblacion_sembradores.devolver_lista_sem():
            sembrador.sembrar_alimento(self.__gestor_de_alimento)
            
        for mo in self.__poblacion_MO.devolver_lista_MO(): 
            mo.moverse(self.__gestor_de_alimento)
            
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
    
    def retornar_lista_MO(self):
        return self.__poblacion_MO.devolver_lista_MO()
            
    # def retornar_MO(self,indice):
    #     return self.__poblacion_MO.devolver_MO(indice)
    
    def __invierno(self):
        ga = Gestor_de_Alimento(self.__parametros)
        if  random.random()*100 < self.__parametros.dic_parametros['invierno']:
            ga.vaciar_matriz_alimento()
    
    def retornar_posiciones_MOs(self):
        return(self.__poblacion_MO.devolver_posicion_MOs())
         
    def retornar_cantidad_MOs(self):
        return (len(self.__poblacion_MO.devolver_lista_MO()))
    
    # def retornar_cantidad_MO_vivos(self):
    #     MO_vivos = self.__poblacion_MO.calcular_cant_MO()
    #     return MO_vivos

    def retornar_inteligencia_promedio(self):
        return self.__poblacion_MO.calcular_inteligencia_promedio()
    
    def retornar_energia_MOs(self):
        lista_energia = []
        for MO in self.__poblacion_MO.devolver_lista_MO():
            lista_energia.append(MO.get_energia())
        return lista_energia

    def retornar_inteligencia_MOs(self):
        lista_inteligencia = []
        for mo in self.__poblacion_MO.devolver_lista_MO():
            inteligencia = mo.devolver_inteligencia()
            lista_inteligencia.append(inteligencia)
        return lista_inteligencia
    
    def retornar_posiciones_sembradores(self):
        return (self.__poblacion_sembradores.devolver_posicion_sembradores())
    
    def retornar_cantidad_sembradores(self):
        return (self.__poblacion_sembradores.calcular_cant_sembradores())
         
    
    def retornar_inteligencia_individual(self, indice):
        lista_MO = self.__poblacion_MO.devolver_lista_MO()
        return lista_MO[indice].devolver_inteligencia()
         
    #devuelve una tupla con la posicion del MO indicado
    # def retornar_posicion_MO(self, indice_MO):
    #     lista_MO = self.__poblacion_MO.devolver_lista_MO()
    #     fila_MO = lista_MO[indice_MO].get_fila() 
    #     columna_MO = lista_MO[indice_MO].get_columna()
    #     return fila_MO, columna_MO   

    def retornar_posicion_sembrador(self, indice_sem):
        lista_sembradores = self.__poblacion_sembradores.devolver_lista_sem()
        fila_sembrador = lista_sembradores[indice_sem].get_fila() 
        columna_sembrador = lista_sembradores[indice_sem].get_columna()
        return fila_sembrador, columna_sembrador   
    
    
    def retornar_datos_alimento(self):
        """ se debe devolver posiciones f c y cantidad de alimento"""
        return self.__gestor_de_alimento.retornar_posicion_y_cantidad_alimento()
        
        #valores aleatorios para el grafico del alimento

       
if __name__ == '__main__':
    ps = Parametros_de_Simulacion
    mundo = Mundo(ps)
    print('el mundo comienza')
    mundo.vivir()
    # print(mundo.devolver_comida())
    # lista = mundo.retornar_lista_MO()
    # print(lista)
    print(mundo.retornar_datos_alimento())
    