# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 11:33:02 2018

@author: igarc

Operadores de crossover extraidos de:
http://www.rubicite.com/Tutorials/GeneticAlgorithms.aspx

3 doperadores de crossover han sido seleccionados:
    Order1
    PMX
    Cycle
"""

import random

"""
Order1 operator
http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/Order1CrossoverOperator.aspx
https://www.youtube.com/watch?v=HATPHZ6P7c4
"""  
def Order1(ruta1,ruta2):
    # posiciones de intercambio
    posorigen = random.randint(0,len(ruta1)-1)
    posfinal = random.randint(0,len(ruta1)-1)
    
    # si la posicion final es antes que la del origen, la instercambiamos
    if posfinal < posorigen: 
        posorigen, posfinal = posfinal, posorigen
    elif posorigen == posfinal:
        # Devolvemos la original
        return ruta1
        
    # Creamos la ruta
    nuevaruta = [0] * len(ruta1)
    flags = [False] * len(ruta1)
    cacho = ruta1[posorigen:posfinal+1] #+1 indice rangos listas
    
    # Insertamos el cacho de la ruta1 en la nueva ruta
    nuevaruta[posorigen:posfinal+1] = cacho
    
    # Elementos de ruta2 que no son parte de lo insertado de la ruta1
    # son insertados a partir de la derecha de lo insertado de la ruta1
    for elemento in cacho:
        if elemento in ruta2:
            # Elementos de la ruta2 ya guardados
            flags[ruta2.index(elemento)] = True
    
    
    # Posicion donde empezar a insertar los elementos restantes
    pos_insert = posfinal+1
    
    # Overflow
    if pos_insert >= len(nuevaruta):
            pos_insert = 0
    
    # ahora insertamos desde la derecha del cacho los elementos de ruta 2,
    # que aun no han sido insertados
    for i in range(posfinal+1,len(ruta2)):
        # Si el elemento no esta incluido
        if not flags[i]:
            nuevaruta[pos_insert] = ruta2[i]
            pos_insert+=1
            flags[i] = True
        
        # Overflow
        if pos_insert >= len(nuevaruta):
            pos_insert = 0
        
    # Metemos el resto de elementos
    for i in range(posfinal+1):
        # Si el elemento no esta incluido
        if not flags[i]:
            nuevaruta[pos_insert] = ruta2[i]
            pos_insert+=1
            flags[i] = True
        
        # Overflow
        if pos_insert >= len(nuevaruta):
            pos_insert = 0
    
    return nuevaruta

"""
Cycle operator
http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/CycleCrossoverOperator.aspx
https://www.youtube.com/watch?v=DJ-yBmEEkgA
Esta operacion puede devolver 2 partículas descendientes pero solo elegiremos una
"""
def Cycle(ruta1,ruta2):
    # Generamos variables iniciales
    flags = [False] * len(ruta1)
    nuevaruta = [0] * len(ruta1)
    origen = 0
    indice = 0
    contador = 0
    switch = random.choice([True,False]) #Aleatorio el origen del primer ciclo
    
    # Bucle hasta terminar
    while contador < len(ruta1):
        # No volvemos a añadir misma posicion
        flags [indice] = True
        # Añadimos elementos de la ruta 1
        if switch:
            # Añadimos
            nuevaruta[indice] = ruta1[indice]
            # Sumamos contador
            contador+=1
            # Nuevo indice
            indice = ruta2.index(ruta1[indice])
            # Si hemos completado un ciclo, alternamos
            if indice == origen:
                indice = 0
                # Encontramos el nuevo origen
                while flags[indice] and contador < len(ruta1):
                    indice += 1
                # Nuevo origen
                origen = indice
                switch = not switch #Alternamos
        # Añadimos elementos de la ruta 2
        else:
            # Añadimos
            nuevaruta[indice] = ruta2[indice]
            # Sumamos contador
            contador+=1
            # Nuevo indice
            indice = ruta1.index(ruta2[indice])
            # Si hemos completado un ciclo, alternamos
            if indice == origen:
                indice = 0
                # Encontramos el nuevo origen
                while flags[indice] and contador < len(ruta1):
                    indice += 1
                # Nuevo origen
                origen = indice
                switch = not switch #Alternamos
        
    return nuevaruta
 
"""
Partially mapped crossover
http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/PMXCrossoverOperator.aspx
https://www.youtube.com/watch?v=ZtaHg1C25Kk
"""
def PMX(ruta1,ruta2):
    # Posiciones de la insercion original
    posorigen = random.randint(0,len(ruta1)-1)
    posfinal = random.randint(0,len(ruta1)-1)
    
    # si la posicion final es antes que la del origen, la instercambiamos
    if posfinal < posorigen: 
        posorigen, posfinal = posfinal, posorigen
    elif posorigen == posfinal:
        # Devolvemos la original
        return ruta1
    
    posfinal+=1 #Indices de listas funcionan raro ;-)
    
    # Inicializamos y realizamos la primera copia
    nuevaruta = [0] * len(ruta1)
    flags = [False] * len(nuevaruta)
    cacho1 = ruta1[posorigen:posfinal]
    nuevaruta[posorigen:posfinal] = cacho1
    
    # Posiciones que ya estan llenas
    for i in range(posorigen,posfinal):
        flags[i] = True
    
    # Del mismo tramo de la ruta 2, vemos que elementos no han sido copiados aun
    flagslocales = [False] * len(cacho1)
    cacho2 = ruta2[posorigen:posfinal]
    
    for i in range(len(cacho2)):
        origen = cacho1[i]
        # Si este elemento del cacho 2 no esta entre los elementos de lo copiado del cacho 1
        # y encontrarles su posicion de destino
        if cacho2[i] not in cacho1:
            # No seguimos hasta encontrar la posicion de destino en la nueva ruta
            while not flagslocales[i]:
                # Donde esta colocado el elemento cuya posicion es la misma que
                # la del elemento del cacho2, dentro del cacho1
                indice = ruta2.index(origen)
                # si esta fuera del rango que han dado lugar a los cachos:
                if indice not in range(posorigen,posfinal):
                    # copiamos el elemento del cacho2 en dicha posicion de la neuva ruta
                    nuevaruta[indice] = cacho2[i]
                    # No volvemos a repetir este elemento
                    flagslocales[i] = True
                    # Esta posicion ya esta llena en la ruta a devolver
                    flags[indice] = True
                # Continuar iterando
                else:
                    origen = ruta1[indice]
        # elemento ya copiado en el cacho
        else:
            # No volvemos a repetir este elemento
            flagslocales[i] = True
            
    # Rellenamos el resto de posiciones vacias
    for i in range(len(flags)):
        # Si no esta relleno aún
        if not flags[i]:
            nuevaruta[i] = ruta2[i]
    
    return nuevaruta
    

    
    
    
    
