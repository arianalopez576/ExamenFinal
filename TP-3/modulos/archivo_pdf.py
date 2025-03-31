from modulos.gestor_archivo import Archivo_Informe
from modulos.archivo_html import Archivo_Html
from datos.parametros_de_simulacion import Parametros_de_Simulacion
from reportlab.pdfgen import canvas

class Archivo_PDF(Archivo_Informe):

    def __init__(self):
        super().__init__()
        
    def _crear_archivo(self, p_archivo): 
        p_archivo.drawString(100, 750, 'Parametros de simulacion')

    def escribir_archivo(self, p_nom_archivo, p_titulo, p_ps, p_epoca, p_lista_inteligencia, p_inteligencia_prom):
        archivo = canvas.Canvas(p_nom_archivo) 
        self._crear_archivo(archivo)  
        
        archivo.setFont("Helvetica", 12)
        archivo.drawString(100, 680, "Época:")
        archivo.drawString(100, 665, p_epoca)
        
        archivo.drawString(100, 655, "Inteligencia:")
        archivo.drawString(100, 640, str(p_lista_inteligencia))
        
        archivo.drawString(100, 625, "Inteligencia promedio:")
        archivo.drawString(100, 610, str(p_inteligencia_prom))

        archivo.showPage()  
        
        self.crear_histograma(p_lista_inteligencia)
        archivo.drawString(100, 500, "Histograma con datos de la inteligencia de los microorganismos:")
        archivo.drawImage('grafico.png', 100, 425, width=400, height=300) 
        archivo.showPage()  
        
        archivo.save()  

        
if __name__ == '__main__':
    pdf = Archivo_PDF()
    ps = Parametros_de_Simulacion()
    lista_intel = [0, 5, 4, 2, 0, 0, 0]
    pdf.escribir_archivo('archi_prueba.pdf', 'Datos del programa', ps, '10', lista_intel, 20)