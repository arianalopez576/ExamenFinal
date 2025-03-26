
from modulos.poblacion_MO import Poblacion_MO
import unittest


class Test_Poblacion_MO(unittest.TestCase):
    
    
    def setUp(self):
        self.__poblacion_MO = Poblacion_MO()
        print ('\nsetUp')
        

if __name__ == '__main__':
    unittest.main()