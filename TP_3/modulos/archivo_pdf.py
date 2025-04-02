from modulos.gestor_archivo import Archivo_Informe
from modulos.archivo_html import Archivo_Html
from datos.parametros_de_simulacion import Parametros_de_Simulacion
from reportlab.pdfgen import canvas
from textwrap import wrap

class Archivo_PDF(Archivo_Informe):

    def __init__(self):
        super().__init__()
        
    def _crear_archivo(self, p_archivo): 
        p_archivo.drawString(100, 750, 'Datos del programa')

    def escribir_archivo(self, p_nom_archivo, p_ps, p_epoca, p_lista_inteligencia, p_inteligencia_prom, p_desviacion_estandar):
        archivo = canvas.Canvas(p_nom_archivo)
        self._crear_archivo(archivo)  
        self.crear_histograma(p_lista_inteligencia)
        
        archivo.drawString(100, 720, "Fecha y hora actuales:")
        archivo.drawString(100, 700, str(self.obtener_fecha_hora()))
        
        y_position = 660
        
        parametros = Parametros_de_Simulacion()
        texto = str(parametros.dic_parametros)
        archivo.drawString(100, 680, "Parametros de la simulacion:")
        archivo.drawString(100, y_position, texto)
        
        archivo.setFont("Helvetica", 12)
        archivo.drawString(100, y_position -20, "Época:")
        archivo.drawString(100, y_position - 40, str(p_epoca))
        
        archivo.drawString(100, y_position - 60, "Inteligencia:")
        archivo.drawString(100, y_position - 80, str(p_lista_inteligencia))
        
        archivo.drawString(100, y_position - 100, "Inteligencia promedio:")
        archivo.drawString(100, y_position - 120, str(p_inteligencia_prom))  
        
        archivo.drawString(100, y_position - 100, "Desviacion estandar:")
        archivo.drawString(100, y_position - 120, str(p_desviacion_estandar))  
        archivo.showPage()
        
        archivo.drawString(100, 425, "Histograma con datos de la inteligencia de los microorganismos:")
        archivo.drawImage('grafico.png', 100, 400, width=400, height=300) 
        archivo.showPage()  
        
        archivo.save()  
        
        
if __name__ == '__main__':
    pdf = Archivo_PDF()
    ps = Parametros_de_Simulacion()
    lista_intel = [0, 5, 4, 2, 0, 0, 0]
    pdf.escribir_archivo('archi_prueba.pdf', 'Datos del programa', ps, '10', lista_intel, 20)