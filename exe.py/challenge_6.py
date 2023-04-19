#realiza programa que pida al usuario un número de 0 al 9. 
# verifique y anuncie si es correcto. 

lista=[0, 1, 3, 5, 6, 8]
 
while(True):
    num = int(input("Adivina un número entre el 0 al 9 \n"))
    if num >= 0 and num <=9: 
        break
if num in lista: 
            print(f"¡Acertaste! el {num} se encuentra en la lista")
else: 
        print(f"el número {num} no se encuentra en la lista. ¡Bye!")     