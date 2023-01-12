#f= lambda x: x**2
#print(f(9))

liste= [1,32,45,2,2,87,9,47,2,56,12]
liste_chaine=["souley","ndiogou","mamadou","aliou","ibou","babou"]
liste_combine=[liste,liste_chaine]
liste_vide=[]
prenom="thiombane"

#affiche les elements de la liste par pas de 2
#print(liste[1:-2:2])

#affiche tous les element de la liste a l'envers
#print(liste[::-1])

#inverse une chaine de caractere 
#print(prenom[::-1])

#----------------------------------------------------------------------

#les differentes methodes qu.on peut utiliser sur une liste

#append permet d'ajouter un elements dans la liste tout a la fin
#liste_chaine.append("abdoulaye")
#print(liste_chaine)

#insert permet d'inserer un element dans une liste en definissant sa position
#liste_chaine.insert(2, "mouhamed")
#print(liste_chaine)

#extend permet d'ajouter une liste dans une liste à la fin
#liste_chaine2=["khadim","thierno","mayoro"]
#liste_chaine.extend(liste_chaine2)
#print(liste_chaine)

#len affiche la taille d'une liste
#print(len(liste_chaine))

#sort permet de trier une liste par ordre alphabet ou inverse et meme du plus grand au plus petit
#liste_chaine.sort(reverse=True)
#print(liste_chaine)
#liste.sort()
#print(liste)

#count permet d'afficher le nombre de fois qu'un element est present dans la liste
#print(liste.count(2))

#clear permet d'effacer tout le contenu d'une liste
#pop et remove nous permet d'enlever certains element dans la liste

#manipuler les listes avec les structures de controle if else for while etc...
"""
if "souley" in liste_chaine:
    liste_chaine.append("abou day")
    print(liste_chaine)
    
else:
    liste_chaine.remove("souley")
    print(liste_chaine)
"""
#afficher les lements avec les index et les valeurs
#for index,valeur in enumerate(liste_chaine):
#    print(index,valeur)

#zip permet d'afficher deux listes avec leur valeur avec la boucle for

#for a, b in zip(liste_chaine,liste[::2]):
#    print(a,b)


