import re

def filtro(cnpj):
    res = re.sub(r'[^0-9]', '', cnpj)
    list_cnpj = []
    for x in res:
        if len(list_cnpj) < 12:
            list_cnpj.append(int(x))
        elif len(list_cnpj) >= 12:
            continue
    return list_cnpj

def valid_cnpj(cnpj):
    if len(cnpj) == 12:
        cnpj.append(gen_n(calcN1(cnpj)))
    elif len(cnpj) == 13:
        cnpj.append(gen_n(calcN2(cnpj)))
    elif len(cnpj) == 14:
        return cnpj
        
def calcN1(array_cnpj):
    array_cript = [5,4,3,2,9,8,7,6,5,4,3,2]
    y = 0
    for x in range(12):
        y = y + array_cnpj[x] * array_cript[x]
    return y
    
def calcN2(array_cnpj):
    array_cript = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    y = 0
    for x in range(13):
        y = y+ array_cnpj[x] * array_cript[x]
    return y

def gen_n(x):
    if 11 - (x % 11) <= 9:
        return 11 - (x % 11)
    elif 11 - (x % 11) > 9:
        return 0
    
def turn_string(cnpj):
    string = ''
    for x in range(14):
        string = string + (str(cnpj[x]))
    return string

def check(input, result):
    input = re.sub(r'[^0-9]', '', input)
    if input == result:
        print(f'{input} = {result}')
        return ('CNPJ válido.')
    elif input != result:
        print(f'{input} != {result}')
        return ('CNPJ inválido.')