# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:12:33 2018

@author: igarc
"""

import math
from Inicializar import *


#Lectura de datos
Citys=leerdatos("berlin52.txt")
#Calculo de distancias
Distancias=CalcularDistancias(Citys["Lat"],Citys["Long"])


