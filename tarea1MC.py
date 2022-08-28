# ADALBERTO EMMANUEL ROJAS
# TAREA 1 MATEMATICAS COMPUTACIONALES
# APROXIMACION A PI CON EL METODO MONTECARLO

# Importamos libreria random
import random as rand
import numpy as np


# NUMERO DE PUNTOS
radio = 1
#puntos = 100
#puntos = 1000
#puntos = 10000
puntos = 1000000

# METODO APLICADO
pc = 0  # puntosdentro del circulo
i = 0
while i<puntos:
    x = rand.random()*(2*radio)-1
    y = rand.random()*(2*radio)-1
    
# calcular distancia del punto
    d = np.sqrt(x**2+y**2)
    if d <= radio:
        pc = pc+1
    i=i+1
        
valorpi= 4*pc/i       
# RESULTADOS
#print(x, y)
#print(pc, puntos)
print('Valor aproximado de pi con 10 000 000 puntos:',valorpi)