
classeur1={
    "negatif":[],
    "positif":[],
    
    }

def trier(classeur,nombre):
    if nombre > 0:
        classeur["positif"].append(nombre)
        
    else:
        classeur["negatif"].append(nombre)
        

trier(classeur1, -12)

print(classeur1)
        