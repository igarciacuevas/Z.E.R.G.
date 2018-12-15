# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:23:13 2018

@author: igarc

Funcion para dibujar la ruta
"""

import networkx
import matplotlib.pyplot as plt

def crear_figura():
    plt.ion() # Activar interactividad
    return plt.figure()

def crear_lista_segmentos(ruta):
    # generar lista
    segmentos = []
    for j in range(len(ruta)-1):
        segmentos.append((ruta[j],ruta[j+1]))
    # Ultimo segmento
    segmentos.append((ruta[-1],ruta[0]))
    
    return segmentos

def crear_etiquetas(nombres):
    labels={}
    for i in range(len(nombres)):
        labels[i] = nombres[i]
    return labels

def anadir_ruta(grafo0,segmentos):
    grafo = networkx.classes.function.create_empty_copy(grafo0)
    grafo.add_edges_from(segmentos)
    return grafo

def crear_grafo(latitudes,longitudes):
    # Init
    grafo = networkx.Graph()
    # Anadimos nodos con sus posiciones
    for i in range(len(latitudes)):
        grafo.add_node(i,pos=(longitudes[i],latitudes[i]))
    
    return grafo

def dibujar(figura,grafo):  
    # Limpiamos
    figura.clear()
    # Anadimos
    posiciones = networkx.get_node_attributes(grafo,'pos') 
    # Dibujar/Actualizar el grafo
    networkx.draw(grafo,pos = posiciones, with_labels=True)
    # Mostramos
    plt.pause(0.001)
    plt.show()
    return

def guardar_figura(figura,configuracion,archivodatos,nombrelogfile):  
    # Limpiamos
    plt.savefig("./logs/"+archivodatos+"/"+configuracion+nombrelogfile+".png")
    return

#def dibujar(figura,grafo,etiquetas):  
#    figura.clear()
#    posiciones = networkx.get_node_attributes(grafo,'pos')  
#    # Dibujar/Actualizar el grafo
#    networkx.draw(grafo,pos = posiciones, with_labels=True)
#    networkx.draw_networkx_labels(grafo, pos=posiciones,labels=etiquetas)
#    # Mostramos
#    plt.pause(0.00001)
#    plt.show()
#    return
