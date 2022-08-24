from abc import abstractmethod

class Conta:
    def __init__(self, agencia, numeroDaConta, saldo):
        self._agencia: agencia
        self._numeroDaConta: numeroDaConta
        self._saldo: saldo
    
    @property
    def agencia(self):
        return self._agencia
    @property
    def numeroDaConta(self):
        return self._numeroDaconta
    @property
    def saldo(self):
        return self._saldo
    
    @abstractmethod
    def sacar(self, valorRetirado: int or float):
        self._saldo -= valorRetirado
    

class ContaCorrente(Conta):
    def __init__(self, agencia, numeroDaConta, saldo):
        super().__init__(agencia, numeroDaConta, saldo)
        
    def deposito(self, valorAdicionado: int or float):  
        self.saldo += valorAdicionado

    def sacar(self, valorRetirado: int or float):
        self.saldo -= valorRetirado

class ContaPoupanca(Conta):
    def __init__(self, agencia, numeroDaConta, saldo):
        super().__init__(agencia, numeroDaConta, saldo)
        
    def deposito(self, valorAdicionado: int or float):
        self.saldo += valorAdicionado
        
    def sacar(self, valorRetirado: int or float):
        if not self.saldo - valorRetirado < 0:
            self.saldo -= valorRetirado
        raise Exception('Saldo de conta poupança não pode ser negativo!')