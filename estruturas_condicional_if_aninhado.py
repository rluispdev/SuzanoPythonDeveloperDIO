
conta_normal = False
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))
cheque_especial = 1000.0
conta_universitaria = False

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial) :
     print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente!")

elif conta_universitaria:
    if saldo >= saque:
     print("Saque realizado com sucesso!")
    else:
     print("Saldo insuficiente da conta Universitaria!")
 
else: 
    print("O tipo de conta informado não é válido!")
