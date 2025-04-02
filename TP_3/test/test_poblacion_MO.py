
from modulos.microorganismo import Microorganismo
from modulos.poblacion_MO import Poblacion_MO
import unittest


class Test_Poblacion_MO(unittest.TestCase):
    
    
    def setUp(self):
        self.__poblacion_MO = Poblacion_MO()
        
    #verifica que la lista de MO contenga datos de tipo MO
    def test_verificar_tipo_MO(self):
        MO_ejemplo = Microorganismo()
        for MO in self.__poblacion_MO.devolver_lista_MO():
            tipo = type(MO)
            self.assertEqual(tipo, type(MO_ejemplo))
        
    #verifica que la inteligencia promedio que calcula sea de tipo float
    def test_verificar_tipo_int_prom(self):
        int_prom = self.__poblacion_MO.calcular_inteligencia_promedio()
        self.assertEqual(float, type(int_prom))

    #verifica que se crea una lista de energia con datos
    def test_crear_lista_energia(self):
        lista_energia = self.__poblacion_MO.crear_lista_energia_MOs()
        self.assertIsNotNone(lista_energia)
    
if __name__ == '__main__':
    unittest.main()