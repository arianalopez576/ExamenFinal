# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 17:58:24 2022

@author: Ivana
"""

from modulos.control_del_mundo import Mundo
from datos.parametros_de_simulacion import Parametros_de_Simulacion
import random
p_s = Parametros_de_Simulacion()
mundo = Mundo(p_s)

#PRUEBA 1 (MOVIMIENTO)
print("Prueba movimiento: ")
indice_random = random.randint(0,20) #AGREGAR LARGO DE LA LISTA MO
mo = mundo.retornar_MO(indice_random)
print("Microorganismo N°" + str(indice_random))
print("\n")

for i in range(10):
    print("Epoca N°" + str(i+1) + ":")
    print("Antes de una iteracion del metodo vivir: ")
    print("Fila: " + str(mo.get_fila()))
    print("Columna: " + str(mo.get_columna()))

    mundo.vivir()

    print("Despues de una iteracion del metodo vivir: ")
    print("Fila: " + str(mo.get_fila()))
    print("Columna: " + str(mo.get_columna()))
    print("\n")

#####################################################################
"""
#PRUEBA ENERGIA

print("Prueba energia: ")
indice_random = random.randint(0,20)
mo = mundo.retornar_MO(indice_random)
print("Microorganismo N°" + str(indice_random))
print("\n")

for i in range(50):
    print("Epoca N°" + str(i+1) + ":")
    print("Antes de una iteracion del metodo vivir: ")
    print("Energia Microorganismo: " + str(mo.retornar_nivel_energia()))
  

    mundo.vivir()

    print("Despues de una iteracion del metodo vivir: ")
    print("Energia Microorganismo: " + str(mo.retornar_nivel_energia()))
    print("\n")

#########################################################################

#PRUEBA INTELIGENCIA PROMEDIO

for i in range(10):
    print("Epoca N°" + str(i))
    print("Antes:")
    print(mundo.retornar_inteligencia_promedio())
    for i in range(100):
        mundo.vivir()
    print("Despues:")
    print(mundo.retornar_inteligencia_promedio())
    print("\n")

"""
mundo.vivir()