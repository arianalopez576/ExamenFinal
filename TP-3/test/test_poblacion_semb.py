
from modulos.poblacion_sembradores import Poblacion_Sembradores
import unittest


class Test_Poblacion_MO(unittest.TestCase):
    
    
    def setUp(self):
        self.__poblacion_semb = Poblacion_Sembradores()
        print ('\nsetUp')
        
    def test_verificar_tipo_lista_semb(self):
        lista_semb = self.__poblacion_semb.devolver_lista_sem()
        self.assertEqual(list, type(lista_semb))
    
    def test_verificar_cantidad_sembradores(self):
        cant = self.__poblacion_semb.calcular_cant_sembradores()
        cant_posiciones = len(self.__poblacion_semb.devolver_posicion_sembradores())
        self.assertEqual(cant, cant_posiciones)

if __name__ == '__main__':
    unittest.main()