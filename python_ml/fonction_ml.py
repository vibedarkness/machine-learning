"""
abs(): return la valeur absolu du nombre
bin(): permet de convertir un entier en nombre binaire
hex(): pour exadecimal
open():  permet de creer certains fichier et de les ouvrirs

"""

#round permet d'arondir une decimal

#x=3.15478
#print(round(x))

#max et min retourne l'element maximum et minimum dans une liste

#liste=[54,87,96,1,5]
#print(max(liste))
#print(min(liste))

#sum additionne les elements d'une liste

#liste=[54,87,96,1,5]
#print(sum(liste))

#str permet de changer un entier en chaine de caractere et int inversememnt

#x=10
#x1=str(x)
#print(type(x1))

#tuple permet de convertir une liste en tuple et list pour l'inverse 
#liste=[54,87,96,1,5]
#print(tuple(liste))

#f=open("fichier.txt","w")
with open("fichier.txt","w") as f:
    for i in range(20):
        f.write(f"{i}={i**2}\n")

