# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:52:43 2018

@author: igarc
"""

import main
import Graficar

# Input de datos
#archivos = ["autonomicas", "mundiales","berlin52.txt","ch130.txt","ch150.txt","PoblacionesSpa.txt"]
archivos = ["ch150.txt"]
archivodatos = archivos[0]

figura = Graficar.crear_figura()

# Tamnos de enjambres
tamanos = [40,100,250,500]
#tamano = 200

# Numero maximo de iteraciones
iteraciones = [100,200,500,1000]
#itermax = 1000

# Numero de vecinos entre particulas
numerodevecinos = [3,5,10] # Numero de vecinos para cada particula
#numvecinos = 3

# Operadores de crossover
# 1=Order1 // 2=Cycle // 3=PMX
operadores_c = [1,2,3]
#operador_cross = 1

# Operadores de mutacion
operadores_m = [0,1,2]
#operador_mut = 1 # 0=No mutacion // 1=Inversion // 2=RandomSwap

#ZERG(archivodatos,tamano,itermax,numvecinos,operador_cross,operador_mut)


for archivodatos in archivos:
	for tamano in tamanos:
		for itermax in iteraciones:
			for numvecinos in numerodevecinos:
				for operador_cross in operadores_c:
					for operador_mut in operadores_m:
						for i in range(0,10):
							main.ZERG(figura,archivodatos,tamano,itermax,numvecinos,operador_cross,operador_mut)
