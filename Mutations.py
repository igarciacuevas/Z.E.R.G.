# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 16:29:43 2018

@author: igarc

Operadores de mutaciones extraidos de:
http://www.rubicite.com/Tutorials/GeneticAlgorithms.aspx

2 doperadores de mutacion han sido seleccionados:
    Inversion
    RandomSwap
"""

import random

"""
Seleccionar dos puntos aleatorios de la ruta e invertir todos sus elementos
https://www.youtube.com/watch?v=WSx_l1Km72U
"""
def Inversion(ruta):
    # Posiciones de inversion
    posorigen = random.randint(0,len(ruta)-1)
    posfinal = random.randint(0,len(ruta)-1)
    
    # si la posicion final es antes que la del origen, la instercambiamos
    if posfinal < posorigen: 
        posorigen, posfinal = posfinal, posorigen
    elif posorigen == posfinal:
        # Devolvemos la original
        return ruta
    
    # Invertimos
    ruta[posorigen:posfinal+1] = ruta[posorigen:posfinal+1][::-1] #List indexes are weird
    
    return ruta

"""
Intercambiamos posiciones de sitio
"""
def RandomSwap(ruta):
    # Posicion limite
    poslimit = random.randint(0,len(ruta)-1)
    
    # Limite en el borde - devolver ruta original
    if poslimit == 0 or poslimit==(len(ruta)-1):
        return ruta
    
    # Tamano maximo de rango
    if poslimit > (len(ruta)-1-poslimit):
        maxrango = (len(ruta)-1-poslimit)
    else:
        maxrango = poslimit
    
    # Posiciones izquieda
    pos1I = random.randint(0,poslimit)
    tamano = random.randint(0,maxrango)
    
    # Limites
    if (pos1I+tamano) > poslimit:
        pos1I = poslimit-tamano
        
    # Posiciones derecha
    pos1D = random.randint(poslimit+1,len(ruta)-1)
    
    # Limites
    if (pos1D+tamano) > (len(ruta)-1):
        pos1D = (len(ruta)-1)-tamano
        
    # Intercambio
    for i in range(tamano):
        ruta[pos1I+i] , ruta[pos1D+i] = ruta[pos1D+i] , ruta[pos1I+i]
    
    return ruta