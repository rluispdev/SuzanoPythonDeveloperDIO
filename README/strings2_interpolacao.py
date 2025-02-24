nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"

print( "Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))



#Chave

print( "Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.". format(nome, idade, profissao, linguagem))
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format (linguagem, profissao, idade, nome) )


#Nomeando as chaves

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format (nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))




#f-strings
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

#Formatar strings com f-strings
PI = 3.14159265359
print(f"O valor de PI é {PI:.2f}")
print(f"O valor de PI é {PI:.5f}")
print(f"O valor de PI é {PI:10.2f}")