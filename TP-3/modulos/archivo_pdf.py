from modulos.gestor_archivo import Archivo_Informe
from modulos.archivo_html import Archivo_Html
from datos.parametros_de_simulacion import Parametros_de_Simulacion
from weasyprint import HTML

class Archivo_PDF(Archivo_Informe):

    def __init__(self):
        super().__init__()
        
    def escribir_archivo(self): 
        archihtml = Archivo_Html()
        HTML('path_of_html').write_pdf('path_of_pdf')
        self.crear_histograma(self.__mundo.retornar_inteligencia_MOs())
 
        
if __name__ == '__main__':
    pdf = Archivo_PDF()
    ps = Parametros_de_Simulacion()
    pdf.escribir_archivo()