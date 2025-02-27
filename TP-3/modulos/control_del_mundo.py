
from modulos.gestor_de_alimento import Gestor_de_Alimento
# from modulos.microorganismo import Microorganismo
# from modulos.sembrador import Sembrador
from datos.parametros_de_simulacion import Parametros_de_Simulacion
from modulos.poblacion_MO import Poblacion_MO
from modulos.poblacion_sembradores import Poblacion_Sembradores
import random

parametros_de_simulacion = Parametros_de_Simulacion()
#parametros_de_simulacion.max_filas = 10  Una forma de modificarlo

class Mundo:    
    def __init__(self, parametros_de_simulacion):
        self.__gestor_alimento = Gestor_de_Alimento(parametros_de_simulacion)
        self.__poblacion_MO = Poblacion_MO()
        self.__poblacion_sembradores = Poblacion_Sembradores()
        self.__epoca = 0
        self.__territorio = [0 for i in range(parametros_de_simulacion.dic_parametros['max_filas']) for j in range(parametros_de_simulacion.dic_parametros['max_columnas'])]
    
    def vivir(self):
        epoca_reproduccion = bool()
        gestor_alimento = self.__gestor_alimento
        if self.__epoca % parametros_de_simulacion.dic_parametros['epoca_rep'] == 0:
            epoca_reproduccion = True
        #esta raro esto porque epoca siempre esta en 0, dividido cualquier cosa es 0.
            
        for sembrador in self.__poblacion_sembradores.devolver_lista_sem():
            sembrador.movimiento_sembrador()
            sembrador.sembrar_alimento(gestor_alimento)
        for mo in self.__poblacion_MO.devolver_lista_MO(): 
            mo.moverse(gestor_alimento)
            
        if epoca_reproduccion == True:
            indice_random = random.randint(0,len(self.__poblacion_MO.devolver_lista_MO())-1)
            while self.__poblacion_MO.devolver_MO(indice_random).retornar_nivel_energia() == 0:
                indice_random = random.randint(0,len(self.__poblacion_MO.devolver_lista_MO())-1)
            MO_hijo = mo.reproduccion(self.retornar_MO(indice_random))
            self.__poblacion_MO.set_MO(MO_hijo) 
           
        # print("Epoca N° " + str(self.__epoca) + ":")
        # indice_mo = 0
        # for mo in self.__poblacion_MO.devolver_lista_MO(): 
        #     print("MO N°" + str(indice_mo+1) + ":")
        #     print("Fila: " + str(mo.get_fila()))
        #     print("Columna: " + str(mo.get_columna()))
        #     print("\n")
        #     indice_mo = indice_mo + 1
        # indice_sembrador = 0
        # for sembrador in self.__poblacion_sembradores.devolver_lista_sem(): 
        #     print("Sembrador N°" + str(indice_sembrador+1) + ":")
        #     print("Fila: " + str(mo.get_fila()))
        #     print("Columna: " + str(mo.get_columna()))
        #     print("\n")
        #     indice_sembrador = indice_sembrador + 1
        
        self.__epoca = self.__epoca + 1
            
    def retornar_MO(self,indice):
        return self.__poblacion_MO.devolver_MO(indice)
    
    def __invierno(self):
        gestor_alimento = self.__gestor_alimento
        if  random.random()*100 < parametros_de_simulacion.dic_parametros['invierno']:
            gestor_alimento.vaciar_matriz_alimento()
            
    def retornar_MO_vivos(self):
        MO_vivos = 0
        for mo in self.__poblacion_MO.devolver_lista_MO():
            if mo.verificar_vida() == True:
                MO_vivos += 1
        return MO_vivos

    def retornar_inteligencia_promedio(self):
        return self.__poblacion_MO.calcular_inteligencia_promedio()

    def retornar_inteligencia_MOs(self):
        lista_inteligencia = []
        for mo in self.__poblacion_MO.devolver_lista_MO():
            inteligencia = mo.devolver_inteligencia()
            lista_inteligencia.append(inteligencia)
        return lista_inteligencia
    
    def retornar_inteligencia_individual(self, indice):
        lista_MO = self.__poblacion_MO.devolver_lista_MO()
        return lista_MO[indice].devolver_inteligencia()
         
    
    def retornar_posicion_MO(self, indice_MO):
        lista_MO = self.__poblacion_MO.devolver_lista_MO()
        fila_MO = lista_MO[indice_MO].get_fila() 
        columna_MO = lista_MO[indice_MO].get_columna()
        return fila_MO, columna_MO   

    def retornar_posicion_Sembrador(self, indice_sem):
        lista_sembradores = self.__poblacion_sembradores.devolver_lista_sem()
        fila_sembrador = lista_sembradores[indice_sem].get_fila() 
        columna_sembrador = lista_sembradores[indice_sem].get_columna()
        return fila_sembrador, columna_sembrador   
    

        
# FALTAN LAS ÉPOCAS
# ARCHIVO
# ¡¡¡GRAFICADORR!!!           
        

