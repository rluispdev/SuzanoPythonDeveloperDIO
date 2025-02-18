
class ContaBancaria:  # A definição da classe está corretamente posicionada sem espaços extras.

    def __init__(self, saldo: float = 500.0):  # O método está corretamente indentado dentro da classe.
        self.saldo = saldo  # Define o saldo como um atributo do objeto. A indentação de um nível (4 espaços) está correta.

    def sacar(self, valor: float) -> None:  # O método está corretamente alinhado dentro da classe.
        if self.saldo >= valor:  # O bloco if está corretamente indentado dentro do método.
            self.saldo -= valor  # O corpo do if está corretamente indentado (4 espaços a mais que o if).
            print(f"Você sacou R$ {valor:.2f}. Seu saldo atual é de R$ {self.saldo:.2f}.")  # A indentação está correta.
        else:  # O else está corretamente alinhado ao if.
            print("Saldo insuficiente.")  # O bloco do else está corretamente indentado.

# Criando um objeto da classe
conta = ContaBancaria()  # A instância da classe está corretamente posicionada sem necessidade de indentação.

# Chamando o método corretamente
conta.sacar(300)  # O método está sendo chamado corretamente sem necessidade de indentação.