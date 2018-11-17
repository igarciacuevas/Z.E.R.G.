# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 12:56:55 2018

@author: igarc

Script principal del algoritmo.
Desde aqui se creara el enjambre de particulas y se llamara al resto de funciones 
para la evolucion en la busqueda de la solucion optima
"""

import numpy
import random
import FuncionesInicializar
import GenParticula
import Evolucion
import datetime
import funcionesLog
import os

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#             DATOS INICIALES
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

archivodatos = "berlin52.txt"
#archivodatos = "autonomicas"

# Variables auxiliares
tamaño=100 # Tamaño del enjambre
itermax=600 # Numero de iteraciones maximas para la busqueda
numvecinos=4 # Numero de vecinos para cada particula
operador_cross=1 # 1=Order1 // 2=Cycle // 3=PMX
operador_mut=1 # 0=No mutacion // 1=Inversion // 2=SingleSwap

# Variables vacias iniciales
enjambre = [] # Lista de todas las particulas
distanciasrutas = [] # Lista de las distancias para cada particula
indices = list(range(tamaño - 1)) # Indices del 0 al tamaño del enjambre (-1)

# Logfile para la ejecucion
nombrelogfile = os.path.splitext(archivodatos)[0]+datetime.datetime.now().strftime('_%H_%M_%S_%d_%m_%Y.log')
logbook = open(nombrelogfile, "a")
funcionesLog.iniciar(logbook,operador_cross,operador_mut,tamaño,itermax)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#             DATOS DEL PROBLEMA
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Lectura de datos
# Citys
#   "Lat" - Latitud de cada ciudad
#   "Long" - Longitud de cada ciudad
#   "Nombres" - Nombres de cada punto. Pueden ser nombres propios o numeros simplemente
Citys = FuncionesInicializar.leerdatos(archivodatos)
#Calculo de distancias
Distancias = FuncionesInicializar.calculardistancias(Citys["Lat"],Citys["Long"])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#             CREACION DEL ENJAMBRE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Vamos a generar todas las particulas iniciales
for i in range(tamaño):
  # Vecinos para cada particula con los que realizará crossovers
  indicesvecinos = random.sample(indices, numvecinos) 
  # Generamos particulas iniciales
  particula = GenParticula.crear_particula(indicesvecinos,Distancias) 
  # Guardamos la distancia de la ruta de cada particula
  distanciasrutas.append(particula.distanciaruta) 
  # Añadimos la particula al enjambre
  enjambre.append(particula) 

# Sacamos el indice del enjambre correspondiente a la particula 
# con menor distancia de ruta del enjambre inicial
indicemejorparticula_ini = numpy.argmin(distanciasrutas)
logbook.write("Mejor distancia inicial: " + str(enjambre[indicemejorparticula_ini].distanciaruta))
logbook.write("\n")
logbook.write("\n")
logbook.write("\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#             EVOLUCION DEL ENJAMBRE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Empezamos el bucle de evolucion que nos dara la solucion al finalizar
for i in range(itermax):
    print("Iteracion " + str(i))
    # Iteramos a lo largo del enjambre
    for j in range(len(indices)):
        print(j)
        # Sacamos la particula
        particulaoriginal = enjambre[j]
        # Caculamos la nueva ruta resultado de curzar y mutar
        nuevaruta = Evolucion.gennuevaruta(enjambre,particulaoriginal,operador_cross,operador_mut)
        # Si la nueva particula es mejor que la original, la reemplazará
        # En caso contrario la particula original se mantendrá
        nuevaparticula = GenParticula.GenParticula(nuevaruta, Distancias, particulaoriginal.vecinos)
        
        if nuevaparticula.distanciaruta < particulaoriginal.distanciaruta:
            enjambre[j] = nuevaparticula
            distanciasrutas[j] = nuevaparticula.distanciaruta
                
    # Sacamos la mejor distancia de la iteracion
    idxbest = numpy.argmin(distanciasrutas)
    logbook.write(str(i) + "--" + str(enjambre[idxbest].distanciaruta))
    logbook.write("\n")
        

resultado = enjambre[idxbest]

# Resultado final
logbook.write("\n")
logbook.write("El mejor resultado final es:")
logbook.write("\n")
logbook.write("\n")
logbook.write("Distancia:  " + str(resultado.distanciaruta))
logbook.write("\n")
logbook.write("\n")
logbook.write("La ruta a seguir es:")
logbook.write("\n")
contadorbreakline = 0
for i in range(len(resultado.ruta)-1):
    logbook.write(Citys["Nombres"][resultado.ruta[i]] + "==>")
    contadorbreakline+=1
    # Cada 8 ciudades apuntadas, pasamos a nueva linea
    if contadorbreakline == 8:
        logbook.write("\n")
        contadorbreakline = 0
    
logbook.write(Citys["Nombres"][resultado.ruta[-1]]+"==>"+Citys["Nombres"][resultado.ruta[0]])
logbook.write("\n")
logbook.write("\n")
logbook.write("------FINAL DEL EXPERIMENTO------")
logbook.close()
    