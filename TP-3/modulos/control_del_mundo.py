from modulos.sembrador import Sembrador 
from modulos.poblacion_MO import Poblacion_MO
from modulos.gestor_de_alimento import Gestor_de_Alimento
from modulos.poblacion_sembradores import Poblacion_Sembradores
from datos.parametros_de_simulacion import Parametros_de_Simulacion
import numpy as np
import random

#parametros_de_simulacion.max_filas = 10  Una forma de modificarlo

class Mundo:    
    def __init__(self, p_ps):
        self.__parametros = p_ps
        self.__poblacion_MO = Poblacion_MO()
        self.__poblacion_sembradores = Poblacion_Sembradores()
        self.__epoca = 0
        self.__territorio = [0 for i in range(p_ps.dic_parametros['max_filas']) for j in range(p_ps.dic_parametros['max_columnas'])]
        
    def vivir(self):
        epoca_reproduccion = False
        semb = Sembrador()
        self.__fila, self.__columna = semb.devolver_posicion_sembrador()
        ga = Gestor_de_Alimento(self.__parametros)
        
        #epoca de reproduccion
        if self.__epoca != 0 and self.__epoca % self.__parametros.dic_parametros['epoca_rep'] == 0:
            epoca_reproduccion = True
       
        #invierno, se vacian todas las celdas de comida
        if random.random()*100 <= self.__parametros.dic_parametros['invierno']:
            self.__invierno()
            
        for sembrador in self.__poblacion_sembradores.devolver_lista_sem():
            sembrador.sembrar_alimento(ga)
            
        for mo in self.__poblacion_MO.devolver_lista_MO(): 
            mo.moverse(ga)
            
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
            
    def retornar_cantidad_MO_vivos(self):
        MO_vivos = self.__poblacion_MO.calcular_cant_MO()
        return MO_vivos

    def retornar_inteligencia_promedio(self):
        return self.__poblacion_MO.calcular_inteligencia_promedio()

    def retornar_inteligencia_MOs(self):
        lista_inteligencia = []
        for mo in self.__poblacion_MO.devolver_lista_MO():
            inteligencia = mo.devolver_inteligencia()
            lista_inteligencia.append(inteligencia)
        return lista_inteligencia
    
    # def retornar_inteligencia_individual(self, indice):
    #     lista_MO = self.__poblacion_MO.devolver_lista_MO()
    #     return lista_MO[indice].devolver_inteligencia()
         
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
    
    
    ''' funciones que devuelven los datos para pasarle al graficador'''
    
    def retornar_datos_sembradores(self):
        """ se debe devolver posiciones f c de los sembradores"""
        
        #datos aleatorios de pueba
        cant_semb = self.__poblacion_sembradores.calcular_cant_sembradores()
        
        arreglo_sembradores = np.zeros(cant_semb, dtype =[("position", int, (2,)), ("color", float, (4,))])
        print(cant_semb)
        for i in range (cant_semb):    
            arreglo_sembradores["position"][i] = np.random.uniform(0, 100, 2)
            arreglo_sembradores["color"][i, 2] = 1 #color azul
        
        # cant_semb = self.__poblacion_sembradores.calcular_cant_sembradores()
        
        # arreglo_sembradores = np.zeros(cant_semb, dtype =[("position", float, (2,)), ("color", float, (4,))])
        # arreglo_sembradores["position"] = self.__poblacion_sembradores.devolver_posicion_sembradores()
        # arreglo_sembradores["color"][:, 2] = 1 #color azul
        
        return (arreglo_sembradores)
           
    def retornar_datos_MOs(self):
        """ se debe devolver posiciones f c energía de los MOs"""
        cant_MOs = 200
            
        arreglo_MOs = np.zeros(cant_MOs, dtype = [("position", float, (2,)), ("energia", float, (1,)), ("color", float, (4,))]) 
        
        arreglo_MOs["position"] = np.random.uniform(0, 100, (cant_MOs, 2))
        arreglo_MOs["energia"] = 1
        arreglo_MOs["color"][:, 1] = 1 #color verde
        
        return (arreglo_MOs)
        
        
    def retornar_datos_alimento(self):
        """ se debe devolver posiciones f c y cantidad de alimento"""
        #valores aleatorios para el grafico del alimento
        cant_alimento = 50
            
        arreglo_alimento = np.zeros(cant_alimento, dtype = [("position", float, (2,)), ("cantidad", float, (1,)), ("color", float, (4,))]) 
        
        arreglo_alimento["position"] = np.random.uniform(0, 100, (cant_alimento, 2))
        arreglo_alimento["cantidad"] = 50
        arreglo_alimento["color"][:, 0] = 1 #color 
        
        # cant_alimento = 1000
        # cant_max_alimento = int(self.__parametros.dic_parametros['alimento_siembra'])  
        
        # arreglo_alimento = np.zeros(cant_alimento, dtype = [("position", float, (2,)), ("cantidad", float, (1,)), ("color", float, (4,))]) 
        
        # arreglo_alimento["position"] = 
        # for f in range (100):
        #     for c in range (100):
        #         arreglo_alimento["cantidad"] = 0
        # arreglo_alimento["color"][:, 0] = 1.0  # Rojo
        # arreglo_alimento["color"][:, 1] = 0.0  # Verde
        # arreglo_alimento["color"][:, 2] = 0.0  # Azul
        # arreglo_alimento["color"][:, 3] = 0#(arreglo_alimento["cantidad"]/cant_max_alimento).ravel()
        
        return (arreglo_alimento)
        
    # def devolver_comida(self):
    #     return(self.__poblacion_sembradores.devolver_lista_comida())

if __name__ == '__main__':
    ps = Parametros_de_Simulacion
    mundo = Mundo(ps)
    mundo.vivir()
    # print(mundo.devolver_comida())
    # lista = mundo.retornar_lista_MO()
    # print(lista)
    print(mundo.retornar_inteligencia_MOs())
