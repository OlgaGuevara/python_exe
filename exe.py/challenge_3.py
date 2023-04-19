#pide un número impar. Si ingresa un número par se reinicia el proceso

while(True):
    numero=int(input("ingrese número impar"))
    if(numero % 2 != 0): 
        print(f"su número es {numero}")
        break
    else: 
        print("Vuelve a intentar")    
