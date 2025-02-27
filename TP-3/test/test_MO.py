
from modulos.microorganismo import Microorganismo
from modulos.gestor_de_alimento import Gestor_de_Alimento
from modulos.cromosoma import *
from datos.parametros_de_simulacion import Parametros_de_Simulacion
import unittest
import random


parametros_de_simulacion = Parametros_de_Simulacion()

class Test_MO(unittest.TestCase):
    
    
    def setUp(self):
        self.__microorganismo = Microorganismo()
        self.nuevo_MO = Microorganismo()
        print ('\nsetUp')
        
        
    def test_mover_y_comer(self):
        p_s = Parametros_de_Simulacion()
        MO = self.__microorganismo
        p_gestor_alimento = Gestor_de_Alimento(p_s)
        mover_y_comer = False
        MO.set_posicion_MO(5,5)
        energia_inicial = MO.retornar_nivel_energia()
        print ("Energia inicial: ", energia_inicial)
        print(MO.moverse(p_gestor_alimento))
        p_gestor_alimento.agregar_alimento_en_posicion(6,5)
        p_gestor_alimento.agregar_alimento_en_posicion(6,6)
        p_gestor_alimento.agregar_alimento_en_posicion(5,6)
        p_gestor_alimento.agregar_alimento_en_posicion(6,4)
        p_gestor_alimento.agregar_alimento_en_posicion(4,6)
        p_gestor_alimento.agregar_alimento_en_posicion(4,5)
        p_gestor_alimento.agregar_alimento_en_posicion(4,4)
        p_gestor_alimento.agregar_alimento_en_posicion(5,4)
        MO.moverse(p_gestor_alimento)
        energia_final = MO.retornar_nivel_energia()
        print("Energia final: ", energia_final)
        if energia_inicial < energia_final:
            mover_y_comer = True
        self.assertTrue(mover_y_comer)
            # TODO: VERRIFICAR QUE LA ENERGIA DE MO DISMINUYA EN LA CANTIDAD APROPIADA
    def test_tipo_nuevo_MO(self):
        MO = self.__microorganismo
        MO1 = Microorganismo()
        self.nuevo_MO = MO.reproduccion(MO1)
        if type(self.nuevo_MO) == type(self.__microorganismo):
            pass
        else:
            raise TypeError('El nuevo microorganismo no es de tipo Microorganismo')

    
    def test_verificar_vida(self):
        MO = self.__microorganismo
        energia = MO.retornar_nivel_energia()
        if energia != 0:
            vida = True
        self.assertTrue(vida)
        
    

    def test_sumar_energia(self):
        p_s = Parametros_de_Simulacion()
        MO = self.__microorganismo
        MO.set_posicion_MO(1,1)
        p_gestor_alimento = Gestor_de_Alimento(p_s)
        aumento_energia = False
        MO.set_energia(10)
        energia_inicial = MO.retornar_nivel_energia()
        p_gestor_alimento.agregar_alimento_en_posicion(1,1) 
        MO.comer(p_gestor_alimento)
        energia_final = MO.retornar_nivel_energia()
        if energia_inicial < energia_final:
                aumento_energia = True
        self.assertTrue(aumento_energia)
        print("sumar energia: ", energia_inicial, energia_final)
  
    
        
    def test_no_comer_en_ausencia_de_comida(self):
        p_s = Parametros_de_Simulacion()
        MO = self.__microorganismo
        MO.set_posicion_MO(1,1)
        p_gestor_alimento = Gestor_de_Alimento(p_s)
        no_aumenta_energia = False
        MO.set_energia(10)
        energia_inicial = MO.retornar_nivel_energia()
        p_gestor_alimento.quitar_alimento_en_posicion(1,1) 
        MO.comer(p_gestor_alimento)
        energia_final = MO.retornar_nivel_energia()
       
        if energia_inicial == energia_final:
                no_aumenta_energia = True
        self.assertTrue(no_aumenta_energia)
        print("No comer: ", energia_inicial, energia_final)
        
     
    
    def test_gastar_energia(self):
        p_s = Parametros_de_Simulacion()
        MO = self.__microorganismo
        p_gestor_alimento = Gestor_de_Alimento(p_s)
        gasto_energia = False
        MO.set_posicion_MO(2,2)
        energia_inicial = MO.retornar_nivel_energia()
        print ("Energia inicial: ", energia_inicial)
        p_gestor_alimento.quitar_alimento_en_posicion(3,2)
        p_gestor_alimento.quitar_alimento_en_posicion(3,3)
        p_gestor_alimento.quitar_alimento_en_posicion(2,3)
        p_gestor_alimento.quitar_alimento_en_posicion(1,3)
        p_gestor_alimento.quitar_alimento_en_posicion(1,2)
        p_gestor_alimento.quitar_alimento_en_posicion(1,1)
        p_gestor_alimento.quitar_alimento_en_posicion(2,1)
        p_gestor_alimento.quitar_alimento_en_posicion(3,1)
        MO.moverse(p_gestor_alimento)
        energia_final = MO.retornar_nivel_energia()
        print("Energia final: ", energia_final)
        if energia_inicial > energia_final:
            gasto_energia = True
        self.assertTrue(gasto_energia)
        print ("Gastar energia: ", energia_inicial, energia_final)
     
    
    def test_movimiento(self):
        p_s = Parametros_de_Simulacion()
        p_gestor_alimento = Gestor_de_Alimento(p_s)
        MO = self.__microorganismo
        for i in range(3000):
            movimiento = False
            fila_inicial = MO.get_fila()
            columna_inicial = MO.get_columna()
            p_gestor_alimento.agregar_alimento_en_posicion(fila_inicial+1, columna_inicial+1)
            MO.moverse(p_gestor_alimento)
            fila_final = MO.get_fila()
            columna_final = MO.get_columna()
            
            if fila_inicial != fila_final or columna_inicial != columna_final:
                movimiento = True
            self.assertTrue(movimiento)
    
    def test_no_incrementar_energia(self):
        p_s = Parametros_de_Simulacion()
        MO = self.__microorganismo
        MO.set_posicion_MO(1,1)
        p_gestor_alimento = Gestor_de_Alimento(p_s)
        energia_max = False
        MO.set_energia(160)
        energia_inicial = MO.retornar_nivel_energia()
        p_gestor_alimento.agregar_alimento_en_posicion(1,1) 
        MO.comer(p_gestor_alimento) #1
        p_gestor_alimento.agregar_alimento_en_posicion(1,1) 
        MO.comer(p_gestor_alimento) #2
        p_gestor_alimento.agregar_alimento_en_posicion(1,1) 
        MO.comer(p_gestor_alimento) #3
        energia_final = MO.retornar_nivel_energia()
        if energia_final == 200:
                energia_max = True
        self.assertTrue(energia_max)
        print("No incrementar energia: ", energia_inicial, energia_final)
    
        
if __name__ == '__main__':
    unittest.main()
