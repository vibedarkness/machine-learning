"""
Note1: on ne peut avoir 2 meme cle dans une dictionnaire
Not2: on peut utiliser les dictionnaires pour stocker les parametres de reseaux de neuronnes
Note3: Dans une dictionnaire il n'ya pas d'odre
"""
#exemple pour le reseaux neuronne
import numpy as np

parametres={
    "w1":np.random.randn(10,100),
    "b1":np.random.randn(10,1),
    "w2":np.random.randn(10,10),
    "b2":np.random.randn(10,1),
    
    }

traduction={
    "chien":"dog",
    "souris":"mouse",
    "chat":"cat",
    "oiseau":"bird"
    
    }

inventaire={
    "banane":4587,
    "pomme":2478,
    "poire":12587,
    "cerise":582
    
    }
"""
association={
    "dict1":traduction,
    "dict2":inventaire
    
    }
"""
#--------------------------------------------------------------
#afficher les valeurs qui se trouve dans le dictionnaire
#print(inventaire.values())

#ajouter un ligne dans le dictionnaire
#inventaire["patates"]=1287
#print(inventaire)

#la methode get permet de verifier si une cle exixte dans le dcitionnaire et affiche sa valeur, sinon il affiche none
#print(inventaire.get('banane'))

#fromkeys permet de creer un dictionnaires a travers travers des cles qui lui seront attribué
#liste1=('paris','londres','marseille')
#print(inventaire.fromkeys(liste1,"omzo"))

#pop permet de supprimer une association dans une dictionnaire
#inventaire.pop("banane")
#print(inventaire)
#-------------------------------------------------------------

#utilisation de la boucle for dans les dictionnaires
#items permet d'afficher la cle et la valeur
print("cle : valeur")
for key,value in inventaire.items():
    print(f"{key}:{value}")

