
def calcular_saldo(transacoes):
    saldo = 0

    # Itera sobre cada transação na lista
    for transacao in transacoes:
        # Adiciona o valor da transação ao saldo
        saldo += transacao

    # Retorna o saldo formatado em moeda brasileira com duas casas decimais
    return f"Saldo: R$ {saldo:,.2f}".replace(".", "X").replace(".", ".").replace("X", ".")

# Recebe a entrada do usuário
entrada_usuario = input()

# Remove os colchetes e espaços extras
entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

# Converte a entrada em uma lista de floats
transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# Calcula o saldo com base nas transações informadas
resultado = calcular_saldo(transacoes)

# Exibe o resultado formatado
print(resultado)

 