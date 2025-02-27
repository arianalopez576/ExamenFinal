
from modulos.cromosoma import Cromosoma
import unittest
import random

class TestCromosoma(unittest.TestCase):
    
    def setUp(self):
        self.__gen = int()
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
       

    def test_verificar_tipo_gen(self):
        cruza = False
        c1 = Cromosoma()
        c2 = Cromosoma()
        cromo_hijo = Cromosoma()
    
        cromosoma_antes_de_cruza = cromo_hijo.devolver_cromosoma()
        print(cromosoma_antes_de_cruza)
        cromo_hijo.agregar_gen_a_cromosoma(c1.cruzar(c2).devolver_cromosoma())
        cromosoma_despues_de_cruza = cromo_hijo.devolver_cromosoma()
        print(cromosoma_despues_de_cruza)
        for i in cromosoma_antes_de_cruza:
            for j in cromosoma_despues_de_cruza:
                if i != j:
                    cruza = True
                    break
        
        self.assertTrue(cruza)
        
       
if __name__ == '__main__':
    unittest.main()