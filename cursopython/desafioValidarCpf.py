#Com o conteúdo visto até então, não é possível evitar cpfs como "11...111", pois não 
#não lecionado como interromper o programa 

cpf = ''
multiplier = 10
cluster = 0
testCpf = ''

while len(cpf) != 11:
    cpf = input('Insira o CPF a ser validado: ')
    if len(cpf) == 11 and cpf.isnumeric:
        continue      
    else:
        print('Inválido. Por favor, insira uma sequência de 11 dígitos.')
        
for n in range(0, 9, 1):
    testCpf += cpf[n]
    cluster = cluster + (int(cpf[n]) * multiplier)
    multiplier = multiplier - 1

if 11 - (cluster % 11) > 9:
    testCpf += (str(0))
elif 11 - (cluster % 11) <= 9:
    testCpf += (str(11 - (cluster % 11))) 

multiplier = 11
cluster = 0

for n in range(0, 10, 1):
    cluster = cluster + (int(testCpf[n]) * multiplier)
    multiplier = multiplier - 1
    
if 11 - (cluster % 11) > 9:
    testCpf += (str(0))
elif 11 - (cluster % 11) <= 9:
    testCpf += (str(11 - (cluster % 11)))

if cpf != testCpf:
    # Em um contexto real, definitivamente não seria posto na tela um possível CPF válido, mas inseri por questões de aprendizado.
    print(f'CPF Inválido!\nCPF válido obtido com os valores inseridos: {testCpf}, CPF inserido: {cpf}')
elif cpf == testCpf:
    print('CPF válido!')