def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # Itera sobre cada transação na lista
    for transacao in transacoes:
        # Verifica se o valor absoluto da transação é maior que o limite
        if abs(transacao) > limite:
            # Adiciona a transação à lista filtrada
            transacoes_filtradas.append(transacao)

    # Retorna a lista de transações filtradas
    return transacoes_filtradas


# Recebe a entrada do usuário
entrada = input("Informe as transações e o limite (exemplo: [100, -50, 300, -150], 100): ")

# Processa as entradas
entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "")  # Remove os colchetes e espaços extras
limite = float(limite.strip())  # Converte o limite para float

# Converte as transações em uma lista de inteiros ou floats
transacoes = [float(valor) for valor in entrada_transacoes.split(",")]

# Filtra as transações que ultrapassam o limite
resultado = filtrar_transacoes(transacoes, limite)

# Exibe o resultado
print(f"Transações: {resultado}")
[200, -50, 400], 150