# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:33:02 2018

@author: igarc

Operadores de crossover y mutaciones extraidos de:
http://www.rubicite.com/Tutorials/GeneticAlgorithms.aspx

3 de cada operador han sido seleccionados
3 (crossover) x 3 (mutaciones-2 op + nomut) = 9 configuraciones
"""

def cruzarymutar(particula,vecino,opcross=1,opmut=0):
    # Por defecto se realizará un crossover Order1 y no mutacion
    if opcross == 1: # Order1
        nuevaparticula = Order1(particula,vecino)
    elif opcross == 2: # Cycle
        nuevaparticula = Cycle(particula,vecino)
    elif opcross == 3: # Edge recombination
        nuevaparticula = EdgeRecom(particula,vecino)
    else: # Si no es numero de operador valido, se realizar un Order1
        nuevaparticula = Order1(particula,vecino)
        
    # Mutaciones. Por defecto no se realizará la operacion de mutacion
    if opmut == 1: # Inversion
        nuevaparticula = Inversion(particula,vecino)
    elif opmut == 2: # SingleSwap
        nuevaparticula = SingleSwap(particula,vecino)
    
    return nuevaparticula

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Operadores Crossover
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     
def Order1(particula,vecino):
    
    return nuevaparticula

def Cycle(particula,vecino):
    
    return nuevaparticula
 
def EdgeRecom(particula,vecino):
    
    return nuevaparticula
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           Operadores Mutacion
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
def Inversion(particula,vecino):
    
    return nuevaparticula

def SingleSwap(particula,vecino):
    
    return nuevaparticula

