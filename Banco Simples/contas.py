import abc

# Classe principal ou super()


class Conta(abc.ABC):
    # Seta a tipagem dos parâmetros que devem ser recebidos
    # Não vai precisar enviar o saldo obrigatoriamente
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')
        return self.saldo

    def detalhes(self, msg: str = '') -> None:
        print(f'O seu saldo {self.saldo:.2f} {msg}.')
        print('--')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo


class ContaCorrente(Conta):
    # Limite é um atributo adicional de Conta Corrente
    def __init__(self, agencia: int, conta: int,
                 saldo: float = 0, limite: float = 0
                 ):  # Cria o novo argumento na subclasse __init__

        # Passando os parâmetros para a classe principal
        super().__init__(agencia, conta, saldo)
        self.limite = limite  # Pegando somente o parâmetro 'limite'

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite  # Para implementar o limite da conta
        # corrente
        # Permite que o saque vá até o limite máximo
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        def __repr__(self) -> str:
            class_name = type(self).__name__
            attrs = f'({self.agencia!r}, {self.conta!r}, '\
                f'{self.saldo!r}, {self.limite!r})'
            return f'{class_name}{attrs}'

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo


# Para fins de teste de código
# Nada abaixo é executado quando
# for importado no main
if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print('##')

    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(1)
    print('##')
