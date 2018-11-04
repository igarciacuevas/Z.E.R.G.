# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:24:52 2018

@author: igarc
"""

import random

class GenParticula:
    
    def __init__(self, ruta, distancias, vecinos):
        self.ruta = ruta # Orden de ciudades de la ruta
        self.vecinos = vecinos # Numero de vecinos con los que realizar crossover
        self.__distancias = distancias # Distancias entre ciudades
        self.distanciaruta = 0.0 # Distancia de la ruta creada
        self.__calculardistanciaruta() # Calculo de la distancia de la ruta creada
        
    # Calcular la distancia de la ruta creada
    def __calculardistanciaruta(self):
        # Iteramos a lo largo de la ruta
        for idx in range(len(self.ruta) - 1):
            iorigen = self.ruta[idx] # Indice ciudad origen
            idestino = self.ruta[idx + 1] # Indice ciudad destino
            # Acumulacion de distancias
            self.distanciaruta += self.__distancias[iorigen][idestino] 
        # Añadimos la ultima distancia desde el punto final al punto inicial de la ruta
        self.distanciaruta += self.__distancias[self.ruta[len(self.ruta) - 1]][self.ruta[0]]
        return self.distanciaruta
    
# Llamada a esta clase
# Generamos ruta aleatoria para la primera vez
def random_particle(vecinos, distancias):
    # Generamos la lista de indices de las ciudades
    ruta = list(range(len(distancias)))
    # Reordenamos la lista aleatoriamente
    random.shuffle(ruta)
    # Devolvemos una partícula/solucion
    return GenParticula(ruta, distancias, vecinos)



