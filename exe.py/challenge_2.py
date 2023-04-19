#Devuelve una lista donde el número de carácteres sea => a 2 
# y que su primer y último caracter sean iguales.

lista= ["ana", "lia", "lucas", "osito", "este", "avila"]
lista2=[]
suma =0
for i in lista: 
    if (len(i)>=2 and (i[0]== i[-1])):
        suma += 1
        lista2.append(i)
        print(suma, lista2)
    
        