#clase 10 del 26/03/2026 
import numpy as np
# Crear matriz
Matriz_Cero = np.zeros((3,4),dtype= int)
print (Matriz_Cero)
# Crear matriz de ceros de tipo entero 3*4  exepto la primera fila que sera 1
Matriz_Cero[0]=1
print (Matriz_Cero)
#Crear matriz de ceros de tipo entero 3*4 excepto la ultma fila que sera de rango entre 5 y 8
Matriz_Cero[2]= np.arange(5,9)
print (Matriz_Cero)

#