import numpy as np
A= np.array(([2,4,9],[1,6,3],[5,7,8]))

#afficher la premiere ligne et la premiere colonne
#print(A[0,0])

#afficher la premiere ligne et la deuxieme colonne
#print(A[0,1])

#afficher les elements de la premiere colonnne avec le slicing
#print(A[:,0])

#afficher les elements de la premiere ligne avec le slicing
#print(A[0,:]) ou print(A[0])

#creer un tableau apartir d'un tableau

#B= A[0:2,0:2]
#print(A)
#print(B)
"""
C= A[0:,1:]
print(A)
print(C)

#remplacer les elements au milieu diu tableau avec des 1
B= np.zeros((4,4))
B[1:3,1:3]=1
print(B)
"""
B= np.random.randint(0,10, [5,5])
print(B<5)