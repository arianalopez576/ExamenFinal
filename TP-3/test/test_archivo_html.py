from modulos.archivo_html import Archivo_Html
from datos.parametros_de_simulacion import Parametros_de_Simulacion
import unittest

parametros = Parametros_de_Simulacion

class Test_Archivo_Html(unittest.TestCase):
    
    def setUp(self):
        self.__archi_html = Archivo_Html()
        print ('\nsetUp')
        
    def test_crear_archivo(self):
        
        self.__archi_html.
       se_genero_correctamente = False
       
       archivos = os.listdir('./')
       if 'histograma.png' and 'informe.html' in archivos:
           se_genero_correctamente = True
       
       self.assertEqual(se_genero_correctamente,True)
    

if __name__ == '__main__':
    unittest.main()
    