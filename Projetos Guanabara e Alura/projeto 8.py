verificador = str(input("Digite um link a ser verificado: "))
print(f"O link digitado foi: {verificador}")
if verificador.startswith("https://") and verificador.endswith(".com"):
    print("O link é seguro.")
else:
    print("O link não é seguro.")       
print("Verificação concluída.")