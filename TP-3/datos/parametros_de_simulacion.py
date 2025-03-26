

class Parametros_de_Simulacion:
    dic_parametros = {
    #Número de filas del territorio
    'max_filas': 100,
    #Número de0 de columnas del territorio
    'max_columnas': 100, 
    #Población (número de individuos) de Microorganismos 
    'cant_MO_inicial': 80,
    #Energía inicial de cada MO
    'energia_inicial': 80,
    #Energía máxima de cada MO
    'energia_max': 200, 
    #Cantidad máxima de alimento que puede ingerir un MO 
    'cant_max_alimento_ingerir': 20, 
    #Energía que consume cada MO al desplazarse 
    'energia_perdida': 1,
    #Población (número de individuos) de Sembradore
    'cant_semb_inicial': 5,
    #Cantidad alimento que siembra un sembrado
    'alimento_siembra': 50,
    #Épocas de reproducción
    'epoca_rep': 10,
    #Probabilidad de mutación
    'prob_mutacion': 2,
    #Probabilidad de cambio de dirección del sembrador
    'prob_cambio_semb': 5,
    #Probabilidad de cambio de dirección del MO
    'prob_cambio_MO': 10,
    #Cantidad máxima de alimento en cada celda del territorio
    'cant_max_alimento_celda': 50,
    #Probabilidad eliminación total del alimento (invierno)
    'invierno': 1
    }
    mov_relativo = [ (0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1) ] 
    
    def get_parametros(self):
        return self.dic_parametros
   