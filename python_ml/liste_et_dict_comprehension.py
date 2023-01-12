# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 21:40:47 2022

@author: HP
"""

"""
Note1:par exemple la boucle au dessus permet d'inserer le carre des nombres allant de 0 a 10 dans une liste'
Note2: la liste prend moins de temps pour s'executer danns la machine que la methode classic
Note: les listes comprehension peuvent servir a creer des nested list(des listes dans une liste)
"""
#import time
#start=time.time()
#methode classic
"""
liste=[]
for i in range(10):
    liste.append(i**2)
end=time.time()
print(end-start)
print(liste)
"""


"""
# Avec liste comprehension
start=time.time()
liste2=[i**2 for i in range(10)]
#end=time.time()
#print(end-start)
print(liste2)
"""
#----------------------------------------------------------------------------
"""
Dict comprehension
Note1:
"""
#ceci creer un dictionnaire en en prennant comme cle des nombres ordonné et comme valeur les elements de la liste
prenoms=["awa","binta","marie","aîcha"]
#dictio={k:v for k,v in enumerate(prenoms)}
#print(dictio)
age=[20,47,12,89]

dico={prenoms:age for prenoms,age in zip(prenoms,age) if age>50}
print(dico)
