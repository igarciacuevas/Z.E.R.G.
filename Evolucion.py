# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 13:19:27 2018

@author: igarc
"""

import Crossovers
    
def gennuevaparticula(enjambre,particula,operador_cross,operador_mut):
    # Sacamos los indices de los vecinos
    indicesvecinos = particula.vecinos
    # Seleccionamos el mejor de los vecinos, el cual sera utilizado para el crossover
    mejorvecino = None # = None para la primera iteracion
    for idx in indicesvecinos:
        temp_particula = enjambre[idx]
        if (mejorvecino == None or temp_particula.distanciaruta < mejorvecino.distanciaruta):
            mejorvecino = temp_particula
        
    # Una vez seleccionado el mejor vecino, realizamos el crossover
    nuevaparticula = Crossovers.cruzarymutar(particula,mejorvecino,operador_cross,operador_mut)
    
    return nuevaparticula
