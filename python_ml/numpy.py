import numpy as np

"""
note: reshape tres important piur les calcules matriciels

"""


#a=np.array(range(100))

#print(a)

#retourne la dimmension de notre tableau
#print(a.ndim)

#retourne la forme de notre tableau
#print(a.shape)

#retourne le nombre d'elemnt dans notre tableau
#print(a.size)

#fourni des nombres aleatoires pour un tableau en definissant les dimmesions
#a=np.random.randn(3,4)
#print(a)

# linspace permet d'afficher un quantite de nombre definit en dernier argument dans une intervalle de valeur(souvent des nombres float)
#a=np.linspace(0,10,20)
#print(a)

#contrairement au linspace ici le dernier argument represente le pas
#a=np.arange(0,10,2)
#print(a)

#hstack et vstack permet de melanger deux tableau horizontalement ou verticalement(utile pour faire des regressions), concatenate aussi fait la meme chose que les deux


a=np.zeros((3,2))
b=np.ones((3,2))
c=np.hstack((a,b))


#reshape permet de dimension notre une tableau a notre propre vision
"""
d=c.reshape((3,4))
print(d)

e=np.array([1,2,3])
"""
#ceci permet d'ajouter un 1 pour les tableaus a une dimmension pour ne pas avoir de probleme avec les algorithmes
#e=e.reshape((e.shape[0],1))
#print(e.shape)
#squeeze permet d'enlever le 1 du shape e.squeeze()

#permet de transformer un tableau a ndimension en une dimmension
print(c.ravel())






