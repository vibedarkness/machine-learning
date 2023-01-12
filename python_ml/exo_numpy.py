import numpy as np
"""from scipy import misc
import matplotlib.pyplot as plt
face=misc.face()

plt.imshow(face)

plt.show()
print(face.shape)
"""
"""
description de l'exo
ecrire une fonction qui retourne une matrice de dimension m*n+1
et a droite de la derniere colonne il sera rempli de 1
"""

def initialisation(m,n):
    
    X=np.random.randn(m,n)
    X=np.concatenate((X, np.ones((X.shape[0],1))), axis=1)
    
    return X


A= initialisation(3,4)

print(A)


