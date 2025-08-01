dados = list()
pessoas = list()
maior_peso = 0
menor_peso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])  
    dados.clear()  

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print(f"Foram cadastradas {len(pessoas)} pessoas.")
if len(pessoas) > 0:
    maior_peso = menor_peso = pessoas[0][1]
    for p in pessoas:
        if p[1] > maior_peso:
            maior_peso = p[1]
        if p[1] < menor_peso:
            menor_peso = p[1]

    print(f'O maior peso foi de {maior_peso}kg. Peso de ', end='')
    for p in pessoas:
        if p[1] == maior_peso:
            print(f'[{p[0]}] ', end='')

    print(f'O menor peso foi de {menor_peso}kg. Peso de ', end='')
    for p in pessoas:
        if p[1] == menor_peso:
            print(f'[{p[0]}] ', end='')