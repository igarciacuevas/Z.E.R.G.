# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:12:33 2018

@author: igarc
"""

import math
import numpy
import random
from FuncionesInicializar import leerdatos, calculardistancias
import GenParticula

#Lectura de datos
Citys = leerdatos("berlin52.txt")
#Calculo de distancias
Distancias = calculardistancias(Citys["Lat"],Citys["Long"])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#             CREACION DEL ENJAMBRE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Variables iniciales y auxiliares
tamaño=500
numvecinos=4
enjambre = []
distanciasrutas = []
indices = list(range(tamaño - 1))

# Vamos a generar todas las particulas iniciales
for i in range(len(tamaño)):
  indicesvecinos = random.sample(indices, numvecinos) # Vecinos para cada particula con los que realizará crossovers
  particula = GenParticula.crear_particula(indicesvecinos,Distancias) # Generamos particulas iniciales
  distanciasrutas.append(particula.distanciaruta) # Guardamos la distancia de la ruta de cada particula
  enjambre.append(particula) # Añadimos la particula al enjambre

# Sacamos el indice la particula con menor distancia de ruta
indicemejorparticula = numpy.argmin(distanciasrutas)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#             EVOLUCION DEL ENJAMBRE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
itermax=600
operador_cross=1 #Seleccionar el operador de crossover
operador_mut=1 #Seleccionar el operador de mutacion

# Empezamos el bucle de evolucion que nos dara la solucion al finalizar
for i in range(itermax):
    nuevagen = [] # Lista vacia donde guardar las nuevas particulas
    for particula in enjambre:
        nuevaparticula = gennuevaparticula(enjambre,particula,operador_cross,operador_mut)
    



