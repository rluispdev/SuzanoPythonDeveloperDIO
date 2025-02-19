texto = input("Digite um texto: ")

VOGAIS = "AEIOU"

#Exemplo usando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra)
    else:
        print("*")

#Exemplo com func built-in range
for numero in range(0, 51, 5):
            print(numero, end=" ")
