"""
corrcoef permet de connaitre les correlations entres differentes ligne et les differentes colonnes
unique permet de connaitre le nombre fois q'un element apparait dans un tableau numpy
nan:not a number
nanmean permet de calculer la moyenne d'un tableau en ignorant les valeurs nan
de base il faut ajouter un nan devant les fonctions np
isnan().sum() permet de compter le nombre de fois que nous avons un nan
isnan(A).sum()/A.size definit le pourcetange qu'occupe les nan dans le tableau
"""
import numpy as np

#A=np.random.randint(0,10,[8,10])
B=np.random.randn(5,5)


#print(A.argmin(axis=0))
#print(A.argsort(axis=0))
#print(np.exp(A))
#print(A.mean())

#print(np.corrcoef(A))
#print(A[1,2])
#print(A[6,9])




#ceci permet de trier les elements du tableau en fonction du nombre de fois qu'ils apparaissent
#print(val[counts.argsort()])
"""
val, counts= np.unique(A, return_counts=True)
print(val, counts)
for i,j in zip(val[counts.argsort()], counts[counts.argsort()]):
    
    print(f"la valeur {i} apparait {j} fois dans le tableau ")
"""

B[3,4]=np.nan
B[4,2]=np.nan
B[2,2]=np.nan
print(np.isnan(B).sum()/B.size)
B[np.isnan(B)]= 2
print(B.mean())
