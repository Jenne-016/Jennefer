n0= int(input("Digite um número: "))
n1= int(input("Digite outro número: "))
n2= int(input("Digite outro número: "))
n3= int(input("Digite outro número: "))
n4= int(input("Digite outro número: "))
pares=0
impares=0
if n0%2==0:
    pares+=1
else:
    impares+=1
if n1%2==0:
    pares+=1
else:
    impares+=1
if n2%2==0:
    pares+=1
else:
    impares+=1
if n3%2==0:
    pares+=1
else:
    impares+=1
if n4%2==0:
    pares+=1
else:
    impares+=1
print(f"{pares}valores pares")
print(f"{impares}valores impares")
