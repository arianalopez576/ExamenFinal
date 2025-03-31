import matplotlib.pyplot as plt
import matplotlib.animation as animation

from modulos.control_del_mundo import Mundo
from datos.parametros_de_simulacion import Parametros_de_Simulacion

import numpy as np

ps = Parametros_de_Simulacion()

class Animador:
    
    def __init__(self, p_func_ani, p_interval=50):
        
        self._fig = None
        self._ax = None
        self._scatter = None
        self._animation = None
        self._func_ani = p_func_ani
        self._interval = p_interval
        
        self._fig = plt.figure(figsize=(6, 4), facecolor="white", dpi=100)
        self._ax = self._fig.add_axes([0, 0, 1, 1], frameon=False)
        self._scatter = self._ax.scatter([], [], s=50, linewidth=0.5, edgecolors=[], facecolors=[]) 
       
        #limites de los ejes
        self._ax.set_xlim(0, 100)
        self._ax.set_xticks([])
        self._ax.set_ylim(0, 100)
        self._ax.set_yticks([])
        
    def animar(self):   
        self._animation = animation.FuncAnimation(self._fig, self._func_ani, fargs=(self._scatter,), interval = self._interval)
        plt.show(block = False) 
        
    def pausar(self):
        if self._animation is not None:
            self._animation.pause()
        else:
            print("Error, la animacion no comenzo")
        
    def continuar(self):
        if self._animation is not None:
            self._animation.resume()
        else:
            print('Error, la animacion no comenzo')