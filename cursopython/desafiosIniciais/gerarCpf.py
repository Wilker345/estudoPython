from random import randint

cpf = str(randint(100000000, 999999999))
multiplier = 10
cluster = 0
testCpf = ''
        
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

print(f'randint: {cpf} CPF:{testCpf}')