#fibonnaci

def fibonaci(n):
    a=0
    b=1
    liste_vide=[a]
    while b<n:
       #print(a)
        a,b=b, a+b
        liste_vide.append(a)
    return liste_vide

print(fibonaci(1000))
