
from modulos.control_del_mundo import Mundo
from datos.parametros_de_simulacion import Parametros_de_Simulacion
import unittest

parametros = Parametros_de_Simulacion

class Test_Archivo_Html(unittest.TestCase):
    
    def setUp(self):
        self.__mundo = Mundo(parametros)
        print ('\nsetUp')
        
    def test_aumentar_epoca(self):
        epoca1 = self.__mundo.retornar_epoca()
        self.__mundo.vivir()
        epoca2 = self.__mundo.retornar_epoca()
        
        self.assertEqual(epoca1+1, epoca2)
        


if __name__ == '__main__':
    unittest.main()
    