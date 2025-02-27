from modulos.sembrador import Sembrador
from datos.parametros_de_simulacion import Parametros_de_Simulacion
from modulos.gestor_de_alimento import Gestor_de_Alimento 
import unittest

class TestSembrador(unittest.TestCase):
    
    def setUp(self):
        self.__sembrador = Sembrador()
        print('\nsetUp') 
        
    def test_mover_sembrador(self):
        sembrador = self.__sembrador
        mover = False
        fila_inicial, columna_inicial = sembrador.devolver_posicion_sembrador()
        sembrador.movimiento_sembrador()
        fila_final, columna_final = sembrador.devolver_posicion_sembrador()
        if fila_final != fila_inicial or columna_inicial != columna_final:
            mover = True
        self.assertTrue(mover)
    
    def test_sembrador_siembra(self):
        p_s = Parametros_de_Simulacion()
        sembrador = self.__sembrador
        p_gestor_alimento = Gestor_de_Alimento(p_s)
        sembrador.set_posicion(3,3)
        sembrar = False
        alimento_en_celda = p_gestor_alimento.retornar_alimento_en_posicion(3,3)
        self.__sembrador.sembrar_alimento(p_gestor_alimento)
        alimento_sembrado_celda = p_gestor_alimento.retornar_alimento_en_posicion(3,3)
        if alimento_en_celda < alimento_sembrado_celda:
            sembrar = True
        self.assertTrue(sembrar)
        print(alimento_en_celda, alimento_sembrado_celda)
    

if __name__ == '__main__':
    unittest.main()