#pregunta al usuario cuantos numeros quiere introducir, 
# lee los numeros y obtiene la media.

num=int(input("¿cuántos números desea ingresar? \n \t"))
sum=0

for e in range(num): 
    sum += float(input("introduce un número \n \t"))
print(f"se ha introducido {num} numeros que en total suman {sum} y la media es {sum/num}")
    