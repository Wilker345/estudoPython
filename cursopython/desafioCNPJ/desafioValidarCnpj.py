# CNPJ teste: 04.252.011/0001-10
# valores fixos para cálculos: 543298765432 / 6543...2987...2
# fórmula para gerar os dois ultimos valores: 11 - (x % 11)
# se for maior que 9, insere 0

##
# Passos:
# 1. recebe o cnpj e desmonta ele para ficar só números
# 2. armazena em um array de ints
# 3. verifica a quantidade de valores para escolher qual array será utilizado no cálculo
# 3. utiliza a função map para multiplicar cada valor do array com os respectivos valores do array
#    de cálculo e obter o valor pro dígito adicional
# 4. verifica a quantidade de valores para escolher qual array será utilizado no cálculo
# 5. passo 3 novamente
# 6. compara o cnpj obtido com o inserido e realiza a validação
##

##
# Pedidos do curso sobre métodos para a resolução :
# Criar um módulo que contém funções
##
from CnpjDefs import filtro, valid_cnpj, turn_string, check

cnpj = '04.252.011/0001-10'
test_cnpj = filtro(cnpj)

while len(test_cnpj) < 14:
    valid_cnpj(test_cnpj)

resultado = check(input=cnpj, result=turn_string(test_cnpj))
print(resultado)