
import json

class Archivo_Json:
    #para almacenar los parametros de simulacion o establecer nuevos valores
    
    def __init__(self):
        pass
    
    def escribir_archi_json(self, p_nom_archi, p_datos):
        nuevo_json = open(p_nom_archi,"w")
        json.dump('Parametros de la simulacion:', nuevo_json)
        json.dump(p_datos, nuevo_json)
        nuevo_json.close()
    
    
    def leer_archi_json(self, p_nom_archi):
        with open (p_nom_archi, 'r') as archi_json:
            datos_json = json.load(archi_json)
        if datos_json is not None:
            return datos_json
        else:
            return 'Error, los datos no se cargaron correctamente'
    
    
if __name__=="__main__":
    archi_json = Archivo_Json()
    datos = archi_json.leer_archi_json(r'C:\Users\Usuario\Desktop\ProgAvanzada\ExamenFinal_ProgAv\ExamenFinal\TP-3\pruebalectura.json')
    print(datos)