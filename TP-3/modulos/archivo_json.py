
from datos.parametros_de_simulacion import Parametros_de_Simulacion
import json

class Gestor_de_Archivo_de_Param:
    #para almacenar los parametros de simulacion o establecer estos valores
    
    def __init__(self):
        pass
    
    def escribir_archi_json(self, p_nom_archi, p_datos):
        nuevo_json = open(p_nom_archi,"w")
        json.dump(p_datos, nuevo_json)
    
    
    def leer_archi_json(self, p_nom_archi):
        with open (p_nom_archi, 'r') as archi_json:
            datos_json = json.load(archi_json)
        return datos_json