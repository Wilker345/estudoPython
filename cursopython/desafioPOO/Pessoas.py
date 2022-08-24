from .Contas import ContaPoupanca, ContaCorrente 

class Pessoa():
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        return self._idade
        
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta: ContaPoupanca or ContaCorrente):
        super().__init__(nome, idade)
        self._conta = conta
        
    @property
    def conta(self):
        return self._conta
