# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:12:33 2018

@author: igarc
"""

import math
import random
from Inicializar import *
import GenParticula


#Lectura de datos
Citys=leerdatos("berlin52.txt")
#Calculo de distancias
Distancias=CalcularDistancias(Citys["Lat"],Citys["Long"])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                   ENJAMBRE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Variables iniciales y auxiliares
tamaño=500
numvecinos=4
itermax=600
enjambre = []
indices = list(range(tamaño - 1))

# Vamos a generar todas las particulas iniciales
for i in range(len(tamaño)):
  indicesvecinos = random.sample(indices, numvecinos) # Vecinos para cada particula con los que realizará crossovers
  particula = GenParticula(


