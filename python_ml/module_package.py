import statistics as sts
import random as rd
import glob as gb
#mean permet de calculer la moyenne
liste=[54,87,96,1,5]
#print(sts.mean(liste))
#print(sts.variance(liste))
#choice permet de choisir un nombre aleatoire dans une liste
#print(rd.choice(liste))

#affiche des nombres float entre 0 et 1
#print(rd.random())
#affiche un nombre aleatoirement dans un intervalle
#print(rd.randint(1, 9))
#print(rd.randrange(100))

# affiche une liste avec le nombre de donnes definit en dernier argument dans l'intervalle du premier argument
#print(rd.sample(range(100), 10))


# shuffle permet de melanger aleatoirement les dones d'une liste ou autre structure de donnes
#print(rd.shuffle(liste))

#glob permet d'afficher tout les nom des fichiers qui sont dans notre repertoire de travail
#print(gb.glob("*"))
#tres util
"""
filenames=gb.glob("*")
d={}
for file in filenames:
    with open(file,"r") as f:
        d[file]=f.read().splitlines()
        
print(d)
"""