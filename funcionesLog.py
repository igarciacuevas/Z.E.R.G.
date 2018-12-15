# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 17:58:15 2018

@author: igarc

Funcion para incializar el log file, escribiendo las condiciones del experimento
"""


def iniciar(archivo,cross,mut,tamano,iteraciones,numciudades):
    archivo.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    archivo.write("\n")
    archivo.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    archivo.write("\n")
    archivo.write("\t" + "CONDICIONES DEL EXPERIMENTO:")
    archivo.write("\n")
    archivo.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    archivo.write("\n")
    archivo.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    archivo.write("\n")
    
    archivo.write("El problema consta de " + str(numciudades) + " ciudades.")
    archivo.write("\n")
    archivo.write("El enjambre tiene " + str(tamano) + " particulas.")
    archivo.write("\n")
    archivo.write("La busqueda tendrá como máximo " + str(iteraciones) + " iteraciones.")
    archivo.write("\n")
    
    if cross == 2: #Cycle
        archivo.write("El operador de crossover es Cycle.")
        archivo.write("\n")
    elif cross == 3: #PMX
        archivo.write("El operador de crossover es PMX.")
        archivo.write("\n")
    else: #Order1
        archivo.write("El operador de crossover es Oder1.")
        archivo.write("\n")
    
    if mut == 1: #Inversion
        archivo.write("El operador de mutacion es Inversion.")
        archivo.write("\n")
    elif cross == 2: #Swap
        archivo.write("El operador de crossover es SingleSwap.")
        archivo.write("\n")
    else: #Nothing
        archivo.write("No hay operador de mutacion.")
        archivo.write("\n")
    
    archivo.write("\n")
    
    archivo.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    archivo.write("\n")
    archivo.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    archivo.write("\n")
    archivo.write("\t" + "MEJOR DISTANCIA PARA CADA ITERACION:")
    archivo.write("\n")
    archivo.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    archivo.write("\n")
    archivo.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    archivo.write("\n")
    
    archivo.write("\n")
    archivo.write("\n")
    
    return
    
    