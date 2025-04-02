from abc import ABC, abstractmethod
import time
from datetime import date
import matplotlib.pyplot as plt
    
class Archivo_Informe(ABC):
    ''' datos que se deben escribir en el informe
    Título.
    - Fecha y hora actuales.
    - Un breve texto descriptivo de lo que contiene el informe (en uno o dos renglones).
    - Los valores de los parámetros de la simulación
    - Número de iteraciones de la simulación
    - Estadística de la inteligencia de los MO: histograma, promedio y desviación
    poblacional.
    '''
    def __init__(self):
        self._datos = None
        self._epoca = None
        self._inteligencia_MOs = None

    def obtener_fecha_hora(self):
        t = time.localtime()
        horario = time.strftime("%H:%M:%S", t) #convierte la hora 't' a HH:MM:SS
        horario_actual = str(horario).replace(':', '-')
        fecha_actual = date.today()
        fecha_hora = str(fecha_actual) + ',' + horario_actual
        return str(fecha_hora)
    
    def crear_histograma(self, p_datos):
        plt.figure()
        plt.hist(p_datos)
        # plt.show()
        plt.savefig("grafico.png")
    
    @abstractmethod
    def escribir_archivo(self):
        pass
