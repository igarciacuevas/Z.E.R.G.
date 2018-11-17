# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 16:29:43 2018

@author: igarc

Tests para los opeardores de mutacion
"""


"""
Seleccionar dos puntos aleatorios de la ruta e invertir todos sus elementos
https://www.youtube.com/watch?v=WSx_l1Km72U
"""
def Inversion_test(ruta,pos1,pos2):
    # Posiciones de inversion
#    pos1 = random.randint(0,len(ruta)-1)
#    pos2 = random.randint(0,len(ruta)-1)
    
    # Invertimos
    ruta[pos1:pos2] = ruta[pos1:pos2][::-1]
    
    return ruta

"""
Intercambiamos dos posiciones de sitio
"""
def SingleSwap_tes(ruta,pos1,pos2):
    # Posiciones de intercambio
#    pos1 = random.randint(0,len(ruta)-1)
#    pos2 = random.randint(0,len(ruta)-1)
    
    # Intercambiamos
    ruta[pos1],ruta[pos2] = ruta[pos2],ruta[pos1]
    
    return ruta




