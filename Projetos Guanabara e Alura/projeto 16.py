spar = sterceira = maior = 0
matriz = [  [ 0, 0, 0,] , [0, 0, 0,] , [0, 0, 0,]] 
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f" Digite um Valor para [{l}] [{c}]: "))
for l in range (0,3):
    for c in range (0,3):
        print(f" [{matriz[l][c]:^5}]" ,  end ="")
    print()
    if matriz[l][c] %2 == 0 :
        spar += matriz[l][c] 
print(f"A soma dos números pares digitados são: {spar} ")
sterceira = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f"A soma dos valores da terceira coluna são: {sterceira} ")
for c in range(0,3):
    if c == 0:
        maior += matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f"O maior número da segunda linha é: {maior} ")
