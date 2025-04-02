from modulos.archivo_html import Archivo_Html
from datos.parametros_de_simulacion import Parametros_de_Simulacion
import unittest

parametros = Parametros_de_Simulacion

class Test_Archivo_Html(unittest.TestCase):
    
    def setUp(self):
        self.__archi_html = Archivo_Html()
        print ('\nsetUp')
        
    def test_crear_archivo(self):
        
        datos = [10, [0,4,3,2], 2, 0.94]
        self.__archi_html.escribir_archivo('informe.html', parametros, datos)
        se_genero_correctamente = False
       
        if 'histograma.png' and 'informe.html' in TP_3:
           se_genero_correctamente = True
       
        self.assertEqual(se_genero_correctamente,True)
    

if __name__ == '__main__':
    unittest.main()
    