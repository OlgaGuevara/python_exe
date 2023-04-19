#generar otra lista con los elementos que se repitan en ellas. 
lista1 = ["a", "g", "a", "n", "a", "r", "b", "a", "b", "y"]
lista2 = ["s", "o", "m", "o", "s", "u", "n", "g", "r", "a", "n", "e", "q", "u", "i", "p", "o"]
lista3=[]

for l in lista1: 
    if l in lista2 and l not in lista3: 
        lista3.append(l)
print(lista3)
