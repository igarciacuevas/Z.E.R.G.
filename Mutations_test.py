# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 16:29:43 2018

@author: igarc

Tests para los opeardores de mutacion
"""


"""
Seleccionar dos puntos aleatorios de la ruta e invertir todos sus elementos
https://www.youtube.com/watch?v=WSx_l1Km72U
"""
def Inversion_test(ruta,pos1,pos2):
    # Posiciones de inversion
#    pos1 = random.randint(0,len(ruta)-1)
#    pos2 = random.randint(0,len(ruta)-1)
    
    # Invertimos
    ruta[pos1:pos2+1] = ruta[pos1:pos2+1][::-1]
    
    return ruta

"""
Intercambiamos dos posiciones de sitio
"""
def RandomSwap_test(ruta, poslimit, pos1I, pos1D, tamaño):
    
    # Limite en el borde - devolver ruta original
    if poslimit == 0 or poslimit==(len(ruta)-1):
        return ruta
        
    # Limites
    if (pos1I+tamaño) > poslimit:
        pos1I = poslimit - tamaño
        print(pos1I)
    
    # Limites
    if (pos1D+tamaño) > (len(ruta)-1):
        pos1D = (len(ruta)-1) - tamaño
        print(pos1D)
        
    # Intercambio
    for i in range(tamaño):
        print(ruta)
        ruta[pos1I+i] , ruta[pos1D+i] = ruta[pos1D+i] , ruta[pos1I+i]
            
    return ruta

#ruta = [1,2,3,4,5,6,7,8]
#ruta2 = Inversion_test(ruta,4,7)
#print("La respuesta deberia ser:")
#print("[1, 2, 3, 4, 8, 7, 6, 5]")
#print(ruta2)
    
#ruta = [1,2,3,4,5,6,7,8]
#ruta2 = RandomSwap_test(ruta,0,0,7,8)
#print("La respuesta deberia ser:")
#print("[1, 2, 3, 4, 5, 6, 7, 8]")
#print(ruta2)
#    
#ruta = [1,2,3,4,5,6,7,8]
#ruta2 = RandomSwap_test(ruta,7,0,7,8)
#print("La respuesta deberia ser:")
#print("[1, 2, 3, 4, 5, 6, 7, 8]")
#print(ruta2)

#ruta = [1,2,3,4,5,6,7,8]
#ruta2 = RandomSwap_test(ruta,3,3,5,2)
#print("La respuesta deberia ser:")
#print("[1, 6, 7, 4, 5, 2, 3, 8]")
#print(ruta2)
