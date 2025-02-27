
from modulos.gestor_archivo import Archivo_Informe
from datos.parametros_de_simulacion import Parametros_de_Simulacion

class Archivo_Html(Archivo_Informe):
    def __init__(self):
        super().__init__()
        self.__archi = None
        
    def escribir_archivo(self, p_nom_archivo, p_titulo,  p_ps, p_epoca, p_inteligencia):
       self.__archi = open('holamundo.html','w')
       parametros = p_ps.get_parametros()
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
        p_inteligencia
            
        }
       </body>
       </html>
       
       '''
       self.__archi.write(mensaje)
       archi.close()
    def get_archivo(self):
        return self.archi
if __name__ == '__main__':
    archihtml = Archivo_Html()
    ps = Parametros_de_Simulacion()
    archihtml.escribir_archivo('archihtml.html', 'Datos de el programa', ps, '10', '20')