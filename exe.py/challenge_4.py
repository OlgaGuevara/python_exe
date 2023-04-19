#suma todos los números enteros pares desde 0 a 100. 
s= sum(list(range(0,101,2)))
print(s)

#solución 2

num=0
suma=0
while num <= 100:
    if(num % 2 == 0): 
        suma += num
    num+=1 
    print(num, suma)  
