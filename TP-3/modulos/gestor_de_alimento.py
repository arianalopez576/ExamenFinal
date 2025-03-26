
class Gestor_de_Alimento:
    
    def __init__(self, p_ps):
        self.__matriz_alimento = [[0 for i in range(p_ps.dic_parametros['max_columnas'])] for j in range(p_ps.dic_parametros['max_filas'])]
        self.__parametros = p_ps
      
    #para la siembra
    def agregar_alimento_en_posicion(self, p_fila, p_columna):
        if self.comprobar_dimension_fila_columna(p_fila, p_columna) == True:
            if self.retornar_alimento_en_posicion(p_fila, p_columna) + self.__parametros.dic_parametros['alimento_siembra'] >= self.__parametros.dic_parametros['cant_max_alimento_celda']:
                self.__matriz_alimento[p_fila][p_columna] = self.__parametros.dic_parametros['cant_max_alimento_celda']
            else:
                self.__matriz_alimento[p_fila][p_columna] = self.retornar_alimento_en_posicion() + self.__parametros.dic_parametros['alimento_siembra']
        else:
            pass # NO DEBERIA HACER NADA.
     
    #se utiliza en el invierno
    def vaciar_matriz_alimento(self):
        for i in range(self.__parametros.dic_parametros['max_filas']):
            for j in range(self.__parametros.dic_parametros['max_columnas']):
                self.__matriz_alimento[i][j] = 0
    
    #se utiliza cuando el MO come
    def quitar_alimento_en_posicion (self, p_fila, p_columna):
            alimento_quitado = 0
            if self.comprobar_dimension_fila_columna(p_fila, p_columna) == True: 
                alimento_en_posicion = self.retornar_alimento_en_posicion(p_fila, p_columna)
                if alimento_en_posicion > 0:
                    if alimento_en_posicion >= self.__parametros.dic_parametros['cant_max_alimento_ingerir']:
                        self.__matriz_alimento[p_fila][p_columna] = self.__matriz_alimento[p_fila][p_columna] - self.__parametros.dic_parametros['cant_max_alimento_ingerir']
                        alimento_quitado = self.__parametros.dic_parametros['cant_max_alimento_ingerir']
                    else:
                        alimento_quitado = self.retornar_alimento_en_posicion(p_fila, p_columna)
                        self.__matriz_alimento[p_fila][p_columna] = 0
            else:
                pass
            return alimento_quitado
            
                    
    def retornar_alimento_en_posicion(self, p_fila, p_columna):
        posicion_en_rango = self.comprobar_dimension_fila_columna(p_fila, p_columna)
        if posicion_en_rango == True:
            cant_alimento = int(self.__matriz_alimento[p_fila][p_columna])
            return cant_alimento
        else:
            return 0
        
        
    def comprobar_dimension_fila_columna(self, p_fila, p_columna):
        if (p_fila >= 0) and (p_fila < self.__parametros.dic_parametros['max_filas']) and (p_columna >= 0) and (p_columna < self.__parametros.dic_parametros['max_columnas']):
            return True 
        else:
            return False
