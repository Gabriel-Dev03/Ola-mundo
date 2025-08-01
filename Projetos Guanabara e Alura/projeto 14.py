num = list()
pares = list()
impares = list()
for n in range(0,7):
    num.append(int(input(f"Digite um número: ")))   
for i in num:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f"Os números pares são: {pares} ")    
print(f"Os números ímpares são: {impares} ")

