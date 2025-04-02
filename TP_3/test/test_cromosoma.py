
from modulos.cromosoma import Cromosoma
import unittest
import random

class TestCromosoma(unittest.TestCase):
    
    def setUp(self):
        self.__cromosoma = Cromosoma()
        print ('\nsetUp')
        
    def test_valor_gen_en_rango(self):
        cromo = self.__cromosoma
        valor_en_rango = False
        lista_genes = []
        for i in range (8):
            gen = random.randint(0, 7)
            lista_genes.append(gen)
        cromo.agregar_gen_a_cromosoma(lista_genes)
        for posicion in range(8):
            valor_gen = cromo.devolver_gen_en_posicion_dada(posicion)
            if valor_gen >= 0 and valor_gen <= 7:
                valor_en_rango = True
        self.assertTrue(valor_en_rango)
      
    def test_verificar_tipo_cromo_hijo(self):
        c1 = self.__cromosoma
        c2 = Cromosoma()
        cromo_hijo = c1.cruzar(c2)
        
        self.assertEqual(type(c1), type(cromo_hijo))
    
    #test para verificar que el cromo hijo sea distinto al del padre y al de la madre
    def test_verificar_cruza(self):
        c1 = self.__cromosoma
        c2 = Cromosoma()
        
        cromo_hijo = c1.cruzar(c2)
        datos_cromo = False #False son distintos
        
        if cromo_hijo.devolver_cromosoma() == c1.devolver_cromosoma() or cromo_hijo.devolver_cromosoma() == c2.devolver_cromosoma():
            datos_cromo = True
        
        self.assertFalse(datos_cromo)
        
       
if __name__ == '__main__':
    unittest.main()