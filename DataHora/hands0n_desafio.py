import datetime

# Variáveis globais
LIMITE_TRANSACOES = 10
saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
transacoes_hoje = 0  # Contador para transações do dia
data_atual = datetime.datetime.now().date()  # Armazenar a data de hoje

def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    return menu

def verificar_reset_data():
    global data_atual, transacoes_hoje
    if datetime.datetime.now().date() != data_atual:
        data_atual = datetime.datetime.now().date()  # Atualiza a data
        transacoes_hoje = 0  # Reseta o contador de transações

def depositar(valor):
    global saldo, extrato, transacoes_hoje

    verificar_reset_data()

    if transacoes_hoje >= LIMITE_TRANSACOES:
        print("Limite de transações diárias atingido!")
        return

    if valor > 0:
        saldo += valor
        extrato += f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Depósito: R$ {valor:.2f}\n"
        transacoes_hoje += 1
        print("Depósito efetuado com sucesso!")
    else:
        print("Valor do depósito deve ser maior que zero.")

def sacar(valor):
    global saldo, extrato, numero_saques, transacoes_hoje

    verificar_reset_data()

    if transacoes_hoje >= LIMITE_TRANSACOES:
        print("Limite de transações diárias atingido!")
        return

    if valor > 0:
        if valor <= 500:  # Limite de R$500 por saque
            if saldo >= valor:
                saldo -= valor
                numero_saques += 1
                extrato += f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Saque: R$ {valor:.2f}\n"
                transacoes_hoje += 1
                print("Saque efetuado com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor do saque acima do limite permitido (R$500).")
    else:
        print("Valor do saque deve ser maior que zero.")

def exibir_extrato():
    global saldo, extrato

    print("\n========= EXTRATO ==========")
    if extrato:
        print(extrato)
    else:
        print("Nenhuma movimentação realizada.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("============================")

def main():
    global saldo, extrato, numero_saques, transacoes_hoje
    while True:
        opcao = input(exibir_menu()).lower()

        if opcao == "d":
            valor = float(input("Digite o valor a depositar: "))
            depositar(valor)

        elif opcao == "s":
            valor = float(input("Digite o valor a sacar: "))
            sacar(valor)

        elif opcao == "e":
            exibir_extrato()

        elif opcao == "q":
            print("Obrigado por utilizar o nosso sistema bancário!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()