opcao = 1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \nDigite a opção desejada: "))
    if opcao == 1:
        print("Sacar")
    elif opcao == 2:
        print("Extrato")
    elif opcao == 0:
        print("Sair")
    else:
        print("Opção inválida!")

        