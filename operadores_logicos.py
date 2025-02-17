 
#And = para ser True tudo que ser True
#OR = para ser True basta um ser True

print (True and True)
print (True and False)
print (False and True)
print (False and False)
print (True or True)
print (True or False)
print (False or True)
print (False or False)
print (not True)
print (not False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

cliente = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print("Pode sacar?", cliente)
 
#Variaveis
conta_normal_com_saldo_suficiente =  (saldo >= saque and saque <= limite)

conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print("Pode sacar?", exp)