
from modulos.gestor_archivo import Archivo_Informe


class Archivo_Html(Archivo_Informe):
    def __init__(self):
        super().__init__()
        self.__archi = None
        
    def escribir_archivo(self, p_nom_archivo, p_parametros, p_datos):
       self.__archi = open(p_nom_archivo,'w')
       #p_datos es una lista que contiene 
           # [0] epoca
           # [1] lista inteligencia
           # [2] inteligencia promedio
           # [3] desviacion estandar 
       self.crear_histograma(p_datos[1])
       mensaje = f''' <html>
       <head>
       <title> {'Datos de la simulacion'} </title>
       </head>
       <body>
       <h3>Fecha y hora actuales: </h3>
       {
        self.obtener_fecha_hora()
        }
       <h3>Parametros de simulacion: </h3>
       {
        p_parametros
        }
       <h3>Epoca: </h3>
       {
        p_datos[0]
        }
        <h3>Inteligencia: </h3>
        {
        p_datos[1]
        }
       <h3>Inteligencia promedio: </h3>
       {
        p_datos[2]
        }
       <h3>Desviacion estandar: </h3>
       {
        p_datos[3]
        }
       <h3>Histograma con datos de la inteligencia de los microorganismos</h3>
       <img src="grafico.png" alt="Gráfico generado">
       
       </body>
       </html>
       
       '''
       self.__archi.write(mensaje)
       self.__archi.close()       
       
    def get_archivo(self):
        return self.__archi
    
from datos.parametros_de_simulacion import Parametros_de_Simulacion   
if __name__ == '__main__':
    archihtml = Archivo_Html()
    ps = Parametros_de_Simulacion()
    lista_intel = [0, 5, 4, 2, 0, 0, 0]
    archihtml.escribir_archivo('archivo.html', ps, '10', lista_intel, 20, 21)
    