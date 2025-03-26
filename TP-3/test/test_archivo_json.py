
from modulos.archivo_json import Gestor_de_Archivo_de_Param
import unittest

class Test_Archivo_Json(unittest.TestCase):
    
    def setUp(self):
        self.__archi_json = Gestor_de_Archivo_de_Param()
        print ('\nsetUp')
        
    def test_verificar_escritura_lectura(self):
        dicc = {"nombre":"juan"}
        archi = self.__archi_json
        
        archi.escribir_archi_json('archivo_prueba_json.json', dicc)
        lectura = archi.leer_archi_json('archivo_prueba_json.json')
        print(lectura)
        self.assertEqual(1, 1)
    

    
        

if __name__ == '__main__':
    unittest.main()
    