lista = list()
while True:
    produto = str(input("Digite o nome do produto: ")).strip().lower()
    lista.append(produto)
    print(f"Produto adicionado: {produto}")
    opcao = str(input("Deseja adicionar mais produtos? [S/N] ")).strip().upper()
    if opcao == 'S':
        continue
    elif opcao == 'N'or opcao != "S":
        print("Obrigado por usar o sistema!")
        break   
print(f"Produtos adicionados: {lista}")