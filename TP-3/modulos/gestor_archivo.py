from abc import ABC, abstractmethod
import time
from datetime import date
    
class Archivo_Informe(ABC):
    def __init__(self):
        self._datos = None

    def obtener_fecha_hora(self):
        t = time.localtime()
        horario = time.strftime("%H:%M:%S", t) #convierte la hora 't' a HH:MM:SS
        horario_actual = str(horario).replace(':', '-')
        fecha_actual = date.today()
        fecha_hora = str(fecha_actual) + ',' + horario_actual
        return str(fecha_hora)
    
    @abstractmethod
    def escribir_archivo(self):
        pass
