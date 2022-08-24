"""
Criar um sistema bancário que tem clientes, contas e um banco. A ideia é que o cliente tenha uma
conta (poupança ou corrente) e que possa sacar/depositar nessa conta. Contas corrente tem um limite
extra. Banco tem clientes e contas.

Pessoa: nome e idade (getters)
Cliente: tem conta, agregação de ContaCorrente ou ContaPoupanca
CC e CP herdam de conta
CC deve ter limite extra (ir abaixo de 0 no saldo após sacar)
Contas têm agência, número da conta e saldo
Contas devem ter método para depósito
Conta (super classe) deve ter método para sacar abstrato
Classe Banco tem que agregar classes de clientes e de contas
Banco autentica o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só sera possível sacar se passar na autenticação do banco (descrita acima)
"""
