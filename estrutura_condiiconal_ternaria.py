
saldo = 2000.0
saque = 2000.0

status = "Realizando saque" if saldo >= saque else "Saldo insuficiente"
print(status)