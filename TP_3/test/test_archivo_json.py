
from modulos.archivo_json import Archivo_Json
import unittest

class Test_Archivo_Json(unittest.TestCase):
    
    def setUp(self):
        self.__archi_json = Archivo_Json()
        print ('\nsetUp')
        
    def test_verificar_escritura_lectura(self):
        dicc = {"nombre":"juan"}
        archi = self.__archi_json
        
        archi.escribir_archi_json('archivo_prueba_json.json', dicc)
        lectura = archi.leer_archi_json('archivo_prueba_json.json')
        print(lectura)
        self.assertEqual(dicc, lectura)
    

    
        

if __name__ == '__main__':
    unittest.main()
    