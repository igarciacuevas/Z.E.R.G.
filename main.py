# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:12:33 2018

@author: igarc
"""

import math

def leerdatos(nombre):
    # Lista de ciudades
    Ciudades = {}
    
    # provincias españolas
    if (nombre == "provincias"):
        archivo = open("Provincias.txt", "r")
        Ciudades = LeerLineas(archivo,"tabulador")
    # capitales del mundo
    elif (nombre == "mundo"):
        archivo = open("CapitalesMundiales.txt", "r")
        Ciudades = LeerLineas(archivo,"tabulador")
    # capitales europeas
    elif (nombre == "europa"):
        archivo = open("CapitalesEuropa.txt", "r")
        Ciudades = LeerLineas(archivo,"tabulador")
    # capitales asia
    elif (nombre == "asia"):
        archivo = open("CapitalesAsia.txt", "r")
        Ciudades = LeerLineas(archivo,"tabulador")
    # capitales america
    elif (nombre == "america"):
        archivo = open("CapitalesAmerica.txt", "r")
        Ciudades = LeerLineas(archivo,"tabulador")
    # capitales oceania
    elif (nombre == "oceania"):
        archivo = open("CapitalesOceania.txt", "r")
        Ciudades = LeerLineas(archivo,"tabulador")
    # Benchmark problem data: archivos de texto separado por espacios
    else:
        archivo = open(nombre, "r")
        Ciudades = LeerLineas(archivo,"espacio")
        
    # Cerrar archivo y devolver diccionario
    archivo.close()
    return Ciudades
     
def LeerLineas(archivo,separador):
    # Inicializar listas
    Nombres = [] 
    Latitud = []
    Longitud = []
    # Archivos propios
    if separador == "tabulador":
        for linea in archivo:
            datoslinea = linea.split("\t")
            Nombres.append(str(datoslinea[0]))
            Latitud.append(float(datoslinea[1]))
            Longitud.append(float(datoslinea[2]))
    # Benchmark problems - Archivos de texto con espacios
    else:
        for linea in archivo:
            datoslinea = linea.split()
            Nombres.append(str(datoslinea[0]))
            Latitud.append(float(datoslinea[1]))
            Longitud.append(float(datoslinea[2]))
        
    # Juntamos todo en un diccionario y devolvemos
    Ciudades = {'Nombres':Nombres,'Lat':Latitud,'Long':Longitud}
    return Ciudades


def CalcularDistancias(Latitudes,Longitudes):
    # Inicializar Listas y puntos auxiliares
    Distancias = []
    Punto1 = []
    Punto2 = []
    
    # Iteramos doblemente para enfrentar todas las ciudades entre sí
    for i in range(len(Latitudes)):
        Punto1 = [Latitudes[i],Longitudes[i]]
        # Variable auxiliar temporal
        DistTemp = []
        for j in range(len(Longitudes)):
            Punto2 = [Latitudes[j],Longitudes[j]]
            DistTemp.append(math.sqrt((Punto1[0]-Punto2[0])*(Punto1[0]-Punto2[0])+(Punto1[1] - Punto2[1])*(Punto1[1] - Punto2[1])))
            
        # Guardamos las distancias de todas las ciudades vs la ciudad "i"
        Distancias.append(DistTemp)
    return Distancias  

