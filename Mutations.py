# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 16:29:43 2018

@author: igarc

Operadores de mutaciones extraidos de:
http://www.rubicite.com/Tutorials/GeneticAlgorithms.aspx

2 doperadores de mutacion han sido seleccionados:
    Inversion
    SingleSwap
"""

import random

"""
Seleccionar dos puntos aleatorios de la ruta e invertir todos sus elementos
https://www.youtube.com/watch?v=WSx_l1Km72U
"""
def Inversion(ruta):
    # Posiciones de inversion
    pos1 = random.randint(0,len(ruta)-1)
    pos2 = random.randint(0,len(ruta)-1)
    
    # Invertimos
    ruta[pos1:pos2] = ruta[pos1:pos2][::-1]
    
    return ruta

"""
Intercambiamos dos posiciones de sitio
"""
def SingleSwap(ruta):
    # Posiciones de intercambio
    pos1 = random.randint(0,len(ruta)-1)
    pos2 = random.randint(0,len(ruta)-1)
    
    # Intercambiamos
    ruta[pos1],ruta[pos2] = ruta[pos2],ruta[pos1]
    
    return ruta