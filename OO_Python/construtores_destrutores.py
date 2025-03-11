class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Construindo um cachorro")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado


    def latir(self):
        print("Au au")

    
    def __del__(self):
        print("Removendo um cachorro")


c= Cachorro("Rex", "Marrom")
c.latir()


