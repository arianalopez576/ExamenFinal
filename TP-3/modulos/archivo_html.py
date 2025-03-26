
from modulos.gestor_archivo import Archivo_Informe
from datos.parametros_de_simulacion import Parametros_de_Simulacion


class Archivo_Html(Archivo_Informe):
    def __init__(self):
        super().__init__()
        self.__archi = None
        
    def escribir_archivo(self, p_nom_archivo, p_titulo, p_ps, p_epoca, p_lista_inteligencia, p_inteligencia_prom):
       self.__archi = open('holamundo.html','w')
       parametros = Parametros_de_Simulacion()
       mensaje = f''' <html>
       <head>
       <title> {p_titulo} </title>
       </head>
       <body>
       <p>Parametros de simulacion: </p>
       {
        parametros
        }
       <p>Epoca: </p>
       {
        p_epoca
        }
        <p>Inteligencia: </p>
        {
        p_lista_inteligencia
        }
       <p>Inteligencia promedio: </p>
       {
        p_inteligencia_prom
        }
       
       </body>
       </html>
       
       '''
       self.__archi.write(mensaje)
       self.crear_histograma(p_lista_inteligencia)
       self.__archi.close()       
       
    def get_archivo(self):
        return self.__archi
    
    
if __name__ == '__main__':
    archihtml = Archivo_Html()
    ps = Parametros_de_Simulacion()
    lista_intel = [0, 5, 4, 2, 0, 0, 0]
    archihtml.escribir_archivo('informe_html.html', 'Datos del programa', ps, '10', lista_intel, 20)
    