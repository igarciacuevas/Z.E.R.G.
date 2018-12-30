# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import math

def cambiar_latitud(dato):
    if dato[-1]=='N':
        return float(1.0*float(dato[:-1]))
    else:
        return float(-1.0*float(dato[:-1]))
    
def cambiar_longitud(dato):
    if "\n" in dato:
        if dato[-3]=='E':
            return float(1.0*float(dato[:-2]))
        else:
            return float(-1.0*float(dato[:-2]))
    else: #Ultima linea
        if dato[-1]=='E':
            return float(1.0*float(dato[:-1]))
        else:
            return float(-1.0*float(dato[:-1]))


def leer_datos(nombre):
    # Lista de ciudades
    Ciudades = {}
    
    # Capitales autonomicas
    if (nombre == "autonomicas"):
        archivo = open("./data/CapitalesAutonomicas.txt", "r")
        Ciudades = leer_lineas(archivo,"tabulador")
    # capitales del mundo
    elif (nombre == "mundiales"):
        archivo = open("./data/CapitalesMundiales.txt", "r")
        Ciudades = leer_lineas(archivo,"tabulador")
    elif (nombre == "autonomicas_vecinos.txt"):
        archivo = open("./data/autonomicas_vecinos.txt", "r")
        Ciudades = leer_lineas(archivo,"tabulador")
    elif (nombre == "mundiales_vecinos.txt"):
        archivo = open("./data/mundiales_vecinos.txt", "r")
        Ciudades = leer_lineas(archivo,"tabulador")
    # capitales europeas
#    elif (nombre == "europa"):
#        archivo = open("./data/CapitalesEuropa.txt", "r")
#        Ciudades = leer_lineas(archivo,"tabulador")
    # capitales asia
#    elif (nombre == "asia"):
#        archivo = open("./data/CapitalesAsia.txt", "r")
#        Ciudades = leer_lineas(archivo,"tabulador")
    # capitales america
#    elif (nombre == "america"):
#        archivo = open("./data/CapitalesAmerica.txt", "r")
#        Ciudades = leer_lineas(archivo,"tabulador")
    # capitales oceania
#    elif (nombre == "oceania"):
#        archivo = open("./data/CapitalesOceania.txt", "r")
#        Ciudades = leer_lineas(archivo,"tabulador")
    # Benchmark problem data: archivos de texto separado por espacios
    else:
        archivo = open("./data/"+nombre, "r")
        Ciudades = leer_lineas(archivo,"espacio")
        
    # Cerrar archivo y devolver diccionario
    archivo.close()
    return Ciudades
     
def leer_lineas(archivo,separador):
    # Inicializar listas
    Nombres = [] 
    Latitud = []
    Longitud = []
    
    # Archivos propios
    if separador == "tabulador":
        for linea in archivo:
            datoslinea = linea.split("\t")
            Nombres.append(str(datoslinea[0]))
            if "Mundiales" in archivo.name or "mundiales" in archivo.name: # N S W E
                Latitud.append(cambiar_latitud(datoslinea[1]))
                Longitud.append(cambiar_longitud(datoslinea[2]))
            else:
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


def calcular_distancias(Latitudes,Longitudes):
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
