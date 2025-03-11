
#Representacao de uma bicicleta em uma bicicletaria

class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):

        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    
    #metdotos
    def bizinar(self):
        print("Plin plin plin")
    
    def parar(self):
        print("PaBicicleta parada!")
    
    def correr(self):
        print("Vrummmm")
     
     #sobrescrevendo o metodo __str__
    # def __str__(self):
    #     return f'Bicicleta {self.cor} {self.modelo} {self.ano} {self.valor}'
    
    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta('vermelha', 'Caloi', 2020, 1000)

print(b1.cor)
print(b1.modelo)
print(b1.ano)   
print(b1.valor)

b1.bizinar
b1.correr()
b1.parar()

print(b1)

