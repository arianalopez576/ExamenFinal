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

    def escribir_archivo(self, p_nom_archivo, p_parametros, p_datos):
        archivo = canvas.Canvas(p_nom_archivo)
        #p_datos es una lista que contiene 
            # [0] epoca
            # [1] lista inteligencia
            # [2] inteligencia promedio
            # [3] desviacion estandar 
        self._crear_archivo(archivo)  
        self.crear_histograma(p_datos[1])
        
        archivo.drawString(100, 720, "Fecha y hora actuales:")
        archivo.drawString(100, 700, str(self.obtener_fecha_hora()))
        
        y_position = 660
        
        texto = str(p_parametros.dic_parametros)
        archivo.drawString(100, 680, "Parametros de la simulacion:")
        archivo.drawString(100, y_position, texto)
        
        archivo.setFont("Helvetica", 12)
        archivo.drawString(100, y_position -20, "Época:")
        archivo.drawString(100, y_position - 40, str(p_datos[0]))
        
        archivo.drawString(100, y_position - 60, "Inteligencia:")
        archivo.drawString(100, y_position - 80, str(p_datos[1]))
        
        archivo.drawString(100, y_position - 100, "Inteligencia promedio:")
        archivo.drawString(100, y_position - 120, str(p_datos[2]))  
        
        archivo.drawString(100, y_position - 140, "Desviacion estandar:")
        archivo.drawString(100, y_position - 160, str(p_datos[3]))  
        archivo.showPage()
        
        archivo.drawString(100, 720, "Histograma con datos de la inteligencia de los microorganismos:")
        archivo.drawImage('grafico.png', 100, 400, width=400, height=300) 
        archivo.showPage()  
        
        archivo.save()  
        
        
if __name__ == '__main__':
    pdf = Archivo_PDF()
    ps = Parametros_de_Simulacion()
    p_datos = [10, [5,3,2,1,1], 2.5, 0.9]
    pdf.escribir_archivo('archi_prueba.pdf', ps, p_datos)