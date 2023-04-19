print('Hola')     
n1= float(input("ingrese número 1 \n"))
n2 = float(input("ingrese número 2 \n"))
    
opcion= input("""Indique la operacion a realizar? 
    [1]sumar
    [2]restar
    [3]multiplicar
    [4]dividir
    """)

if opcion == "1": 
    print(f"resultado de la suma de {n1} y {n2} es {n1+n2}")
elif opcion =="2": 
    print(f"resultado es {n1-n2}")
elif opcion =="3": 
    print(f"resultado es {n1*n2}")
elif opcion =="4": 
    print(f"resultado es {n1/n2}")
else: 
    print("ingrese una opcion valida")
    
    
      