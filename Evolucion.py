# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 13:19:27 2018

@author: igarc

Funciones de alto nivel para cruzar y mutar las rutas y finalmente generar nuevas particulas
3 (crossover) x 3 (mutaciones-2 op + nomutacion) = 9 configuraciones
"""

import Crossovers
import Mutations
import random
    
def gen_nueva_ruta(enjambre,particula,operador_cross,operador_mut):
    # Sacamos los indices de los vecinos
    indicesvecinos = particula.vecinos
    # Seleccionamos el mejor de los vecinos, el cual sera utilizado para el crossover
    mejorvecino = None # = None para la primera iteracion
    for idx in indicesvecinos:
        temp_particula = enjambre[idx]
        if (mejorvecino == None or temp_particula.distanciaruta < mejorvecino.distanciaruta):
            mejorvecino = temp_particula
        
    # Una vez seleccionado el mejor vecino, realizamos el crossover y mutacion
    # para obtener nueva ruta
    nuevaruta = cruzar_y_mutar(particula.ruta,mejorvecino.ruta,operador_cross,operador_mut)
    
    return nuevaruta


def cruzar_y_mutar(rutaparticula,rutavecino,opcross,opmut):
    # Por defecto se realizará un crossover Order1 y no mutacion
    if opcross == 1: # Order1
        nuevaruta = Crossovers.Order1(rutaparticula,rutavecino)
    elif opcross == 2: # Cycle
        nuevaruta = Crossovers.Cycle(rutaparticula,rutavecino)
    elif opcross == 3: # Partially mapped crossover
        nuevaruta = Crossovers.PMX(rutaparticula,rutavecino)
    else: # Si no es numero de operador valido, se realizar un Order1
        nuevaruta = Crossovers.Order1(rutaparticula,rutavecino)
        
        
    # Mutaciones. Por defecto no se realizará la operacion de mutacion
    # Hay un 10% de probabilidades de realizar una mutacion
    if random.randint(0,100) < 15:
        if opmut == 1: # Inversion
            nuevaruta = Mutations.Inversion(nuevaruta)
        elif opmut == 2: # SingleSwap
            nuevaruta = Mutations.RandomSwap(nuevaruta)
    
    return nuevaruta