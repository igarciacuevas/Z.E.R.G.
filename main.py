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
import time
import Graficar


def ZERG(figura,archivodatos,tamano,itermax,numvecinos,operador_cross,operador_mut):
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #             DATOS INICIALES
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    # Variables vacias iniciales
    enjambre = [] # Lista de todas las particulas
    distanciasrutas = [] # Lista de las distancias para cada particula
    indices = list(range(tamano)) # Indices del 0 al tamano del enjambre 
    
    # Logfile para la ejecucion
    nombrelogfile = os.path.splitext(archivodatos)[0]+datetime.datetime.now().strftime('_%H_%M_%S_%d_%m_%Y.log')
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #             DATOS DEL PROBLEMA
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    if operador_cross==1:
        if operador_mut==0:
            configuracion="/Config1/"
        elif operador_mut==1:
            configuracion="/Config2/"
        elif operador_mut==2:
            configuracion="/Config3/"
    elif operador_cross==2:
        if operador_mut==0:
            configuracion="/Config4/"
        elif operador_mut==1:
            configuracion="/Config5/"
        elif operador_mut==2:
            configuracion="/Config6/"
    elif operador_cross==3:
        if operador_mut==0:
            configuracion="/Config7/"
        elif operador_mut==1:
            configuracion="/Config8/"
        elif operador_mut==2:
            configuracion="/Config9/"
    else:
        if operador_mut==0:
            configuracion="/Config1/"
        elif operador_mut==1:
            configuracion="/Config2/"
        elif operador_mut==2:
            configuracion="/Config3/"
            
    #Lectura de datos
    # Citys
    #   "Lat" - Latitud de cada ciudad
    #   "Long" - Longitud de cada ciudad
    #   "Nombres" - Nombres de cada punto. Pueden ser nombres propios o numeros simplemente
    
    Citys = FuncionesInicializar.leer_datos(archivodatos)
    
    #Calculo de distancias
    Distancias = FuncionesInicializar.calcular_distancias(Citys["Lat"],Citys["Long"])
    
    with open("./logs/"+os.path.splitext(archivodatos)[0]+configuracion+nombrelogfile, "a") as logbook:
        
        funcionesLog.iniciar(logbook,operador_cross,operador_mut,tamano,itermax,len(Citys["Lat"]))
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #             CREACION DEL ENJAMBRE
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        # Vamos a generar todas las particulas iniciales
        for i in range(tamano):
          # Vecinos para cada particula con los que realizará crossovers
          indicesvecinos = random.sample(indices, numvecinos) 
          # Generamos particulas iniciales
          particula = GenParticula.crear_particula(indicesvecinos,Distancias) 
          # Guardamos la distancia de la ruta de cada particula
          distanciasrutas.append(particula.distanciaruta) 
          # Anadimos la particula al enjambre
          enjambre.append(particula) 
        
        # Sacamos el indice del enjambre correspondiente a la particula 
        # con menor distancia de ruta del enjambre inicial
        indicemejorparticula_ini = numpy.argmin(distanciasrutas)
        logbook.write("Mejor distancia inicial: " + str(enjambre[indicemejorparticula_ini].distanciaruta))
        logbook.write("\n")
        logbook.write("\n")
        logbook.write("\n")
        
        # Graficamos la ruta inicial
        # etiquetas = Graficar.crear_etiquetas(Citys["Nombres"])
        #figura = Graficar.crear_figura()
        #figura.clear()
        grafo_0 = Graficar.crear_grafo(Citys["Lat"],Citys["Long"])
        
        # Anadimos la ruta
        segmentos = Graficar.crear_lista_segmentos(enjambre[indicemejorparticula_ini].ruta)
        grafo = Graficar.anadir_ruta(grafo_0,segmentos)
        Graficar.dibujar(figura, grafo_0)
        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #             EVOLUCION DEL ENJAMBRE
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        contadorestancamiento = 0
        idxbestold = -1
        
        tiempoini = time.time()
        
        # Empezamos el bucle de evolucion que nos dara la solucion al finalizar
        for i in range(itermax):
            print("Iteracion " + str(i))
            # Iteramos a lo largo del enjambre
            for j in range(len(indices)):
#                print(j)
                # Sacamos la particula
                particulaoriginal = enjambre[j]
                # Caculamos la nueva ruta resultado de curzar y mutar
                nuevaruta = Evolucion.gen_nueva_ruta(enjambre,particulaoriginal,operador_cross,operador_mut)
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
            
            # Si recibimos misma ruta optima durante más de el 15% de iteraciones - BREAK
            if idxbest == idxbestold:
                contadorestancamiento+=1
                if contadorestancamiento >= round((0.15*itermax)):
                    print("Busqueda estancada.")
                    logbook.write("FINAL DE BUSQUEDA POR ESTANCAMIENTO")
                    logbook.write("\n")
                    break
            else:
                segmentos = Graficar.crear_lista_segmentos(enjambre[idxbest].ruta)
                grafo = Graficar.anadir_ruta(grafo_0,segmentos)
                Graficar.dibujar(figura,grafo)
                contadorestancamiento = 0
                idxbestold = idxbest
                
        tiempofin = time.time()
        
        # Calculamos el tiempo de ejecucion redondeando a milisegundos
        tiempocalculo = round(tiempofin - tiempoini,3)
        logbook.write("\n")
        logbook.write("El tiempo de búsuqeda ha sido de " + str(tiempocalculo) + " segundos.")
        logbook.write("\n")
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
        logbook.write("NumVecinos:  " + str(numvecinos))
        logbook.write("\n")
        logbook.write("\n")
        logbook.write("Indices de ruta:  " + str(resultado.ruta))
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
        
        Graficar.guardar_figura(figura,configuracion,os.path.splitext(archivodatos)[0],os.path.splitext(nombrelogfile)[0])
            
        return


# Variables auxiliares
# Input de datos
#archivos = ["autonomicas", "mundiales","berlin52.txt","ch130.txt","ch150.txt","PoblacionesSpa.txt"]
#archivodatos = "mundiales"
#
## Tamnos de enjambres
#tamanos = [40,100,250,500]
#tamano = 200
#
## Numero maximo de iteraciones
#iteraciones = [500,2000,5000]
#itermax = 1000
#
## Numero de vecinos entre particulas
#numerodevecinos = [3,5,10,15] # Numero de vecinos para cada particula
#numvecinos = 3
#
## Operadores de crossover
## 1=Order1 // 2=Cycle // 3=PMX
#operadores_c = [1,2,3]
#operador_cross = 1
#
## Operadores de mutacion
#operadores_m = [0,1,2]
#operador_mut = 0 # 0=No mutacion // 1=Inversion // 2=RandomSwap
#
##ZERG(archivodatos,tamano,itermax,numvecinos,operador_cross,operador_mut)
#
#for archivodatos in archivos:
#    for tamano in tamanos:
#        for itermax in iteraciones:
#            for numvecinos in numerodevecinos:
#                for operador_cross in operadores_c:
#                    for operador_mut in operadores_m:
#                        ZERG(archivodatos,tamano,itermax,numvecinos,operador_cross,operador_mut)

#ZERG(archivodatos,tamano,itermax,numvecinos,operador_cross,operador_mut)
#ZERG(archivodatos,tamano,itermax,numvecinos,operador_cross,operador_mut)
