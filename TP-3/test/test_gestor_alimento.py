
from modulos.gestor_de_alimento import Gestor_de_Alimento
from datos.parametros_de_simulacion import Parametros_de_Simulacion
import unittest

ps = Parametros_de_Simulacion()
class TestGestorAlimento(unittest.TestCase):
    
    def setUp(self):
        self.__gestor_alimento = Gestor_de_Alimento(ps)
        print ('\nsetUp')
        
    def test_agregar_alimento_en_posicion(self):
        g_alimento = self.__gestor_alimento
        alimento_inicial = g_alimento.retornar_alimento_en_posicion(1, 1)
        g_alimento.agregar_alimento_en_posicion(1, 1)
        alimento_final = g_alimento.retornar_alimento_en_posicion(1, 1)
        agrego_alimento = False
        if g_alimento.retornar_alimento_en_posicion(1, 1) > 0:
            agrego_alimento = True
        self.assertTrue(agrego_alimento)
        print(alimento_inicial, alimento_final)
            
     
    def test_quitar_alimento(self):
        g_alimento = self.__gestor_alimento
        g_alimento.agregar_alimento_en_posicion(1, 1)
        cantidad_agregada = g_alimento.retornar_alimento_en_posicion(1, 1)
        alimento_quitado = g_alimento.quitar_alimento_en_posicion(1, 1)
        cantidad_final = g_alimento.retornar_alimento_en_posicion(1, 1)
        alimento_quitado = False
        if cantidad_final < cantidad_agregada:
            alimento_quitado = True
        self.assertTrue(alimento_quitado)
        print(cantidad_agregada, cantidad_final, alimento_quitado)
            
    def test_quitar_alimento_invierno(self):
        g_alimento = self.__gestor_alimento
        al_total_eliminado = False
        for i in range(ps.dic_parametros['max_filas']):
            for j in range(ps.dic_parametros['max_columnas']):
                g_alimento.agregar_alimento_en_posicion(i,j)
        g_alimento.vaciar_matriz_alimento()
        for i in range(ps.dic_parametros['max_filas']):
             for j in range(ps.dic_parametros['max_columnas']):
                if g_alimento.retornar_alimento_en_posicion(i, j) == 0:
                    al_total_eliminado = True
                else:
                    al_total_eliminado = False
                    break
        self.assertTrue(al_total_eliminado)
                
        
    def test_comprobar_posicion(self):
        g_alimento = self.__gestor_alimento
        fuera_de_territorio = g_alimento.comprobar_dimension_fila_columna(300,300)
        self.assertEqual(fuera_de_territorio, False)
        
    def test_comprobar_dimension(self):
        g_alimento = self.__gestor_alimento
        fuera_de_rango = g_alimento.comprobar_dimension_fila_columna(200, 200)
        self.assertFalse(fuera_de_rango)
       

if __name__ == '__main__':
    unittest.main()