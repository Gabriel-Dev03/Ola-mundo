nome = str(input("Digite seu nome: "))
documento = input("Digite o seu documento e o codigo de verificação dele: ")
print(f"Ola {nome}, o documento digitado foi: {documento}")
if "1087568" in documento:
    print("O documento é válido.")
else:
    print("O documento não é válido.")      
print("Verificação concluída.")