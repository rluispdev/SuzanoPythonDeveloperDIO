nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"

print( "Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

print("Nome:{} Idade:{}".format(nome, idade))
print("Nome:{0} Idade:{1}".format(nome, idade))
print("Nome:{1} Idade:{0}".format(idade, nome))
print("Nome:{n} Idade:{i}".format(n=nome, i=idade))


