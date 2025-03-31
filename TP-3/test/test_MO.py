
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
        self.__nuevo_MO = Microorganismo()
        print ('\nsetUp')
        
    # #verifica que la energía aumenta cuando el MO se alimenta
    # def test_aumentar_energia(self):
    #     p_s = Parametros_de_Simulacion()
    #     MO = self.__microorganismo
    #     p_gestor_alimento = Gestor_de_Alimento(p_s)
    #     p_gestor_alimento.agregar_alimento_en_posicion(6,5)
    #     p_gestor_alimento.agregar_alimento_en_posicion(6,6)
    #     p_gestor_alimento.agregar_alimento_en_posicion(5,6)
    #     p_gestor_alimento.agregar_alimento_en_posicion(6,4)
    #     p_gestor_alimento.agregar_alimento_en_posicion(4,6)
    #     p_gestor_alimento.agregar_alimento_en_posicion(4,5)
    #     p_gestor_alimento.agregar_alimento_en_posicion(4,4)
    #     p_gestor_alimento.agregar_alimento_en_posicion(5,4)
        
    #     aumento_energia = False
    #     MO.set_posicion_MO(100,100)
    #     energia_inicial = MO.get_energia()
    #     print ("Energia inicial: ", energia_inicial)
    #     MO.moverse(p_gestor_alimento)
    #     energia_final = MO.get_energia()
    #     print("Energia final: ", energia_final)
    #     if energia_inicial < energia_final:
    #         aumento_energia = True
            
    #     self.assertTrue(aumento_energia)
            
    # #verifica que el nuevo MO, producto de la reproduccion sea de tipo Microorganismo()        
    # def test_tipo_nuevo_MO(self):
    #     MO = self.__microorganismo
    #     MO1 = Microorganismo()
    #     self.nuevo_MO = MO.reproduccion(MO1)
    #     if type(self.nuevo_MO) == type(self.__microorganismo):
    #         pass
    #     else:
    #         raise TypeError('El nuevo microorganismo no es de tipo Microorganismo')

    # #verifica el funcionamiento correcto de la funcion verificar vida
    # def test_verificar_vida(self):
    #     MO = self.__microorganismo
    #     energia = MO.get_energia()
    #     if energia != 0:
    #         vida = True
        
    #     self.assertEqual(vida, MO.verificar_vida())
        
    
    # #verifica que la energia aumente cuando el MO se alimenta
    # def test_restar_energia(self):
    #     p_s = Parametros_de_Simulacion()
    #     MO = self.__microorganismo
    #     MO.set_posicion_MO(10,10)
    #     p_gestor_alimento = Gestor_de_Alimento(p_s)
    #     aumento_energia = False
    #     energia_inicial = MO.get_energia()
    #     p_gestor_alimento.agregar_alimento_en_posicion(20,20) 
    #     MO.moverse(p_gestor_alimento)
    #     energia_final = MO.get_energia()
    #     if energia_inicial < energia_final:
    #             aumento_energia = True
    #     self.assertFalse(aumento_energia)
    #     print('energia que pierde', energia_inicial, energia_final)
    
    def test_movimiento(self):
        p_s = Parametros_de_Simulacion()
        p_gestor_alimento = Gestor_de_Alimento(p_s)
        MO = self.__microorganismo
        MO.set_posicion_MO(100,100)
        for i in range(10):
            movimiento = False
            pos_inicial = MO.get_posicion()
            # fila_inicial = MO.get_fila()
            # columna_inicial = MO.get_columna()
            MO.moverse(p_gestor_alimento)
            pos_final = MO.get_posicion()
            # fila_final = MO.get_fila()
            # columna_final = MO.get_columna()
            print(pos_inicial, pos_final)
            if pos_inicial != pos_final:
                movimiento = True
            self.assertTrue(movimiento)
        
if __name__ == '__main__':
    unittest.main()
