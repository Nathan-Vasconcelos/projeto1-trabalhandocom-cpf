#osb passou pelo validadorcpf e pelo cadastro de usuário do pdv
#gera números que possam ser um cpf de rj
from random import randint

cpf = []
for c in range(0, 8):
    cpf.append(randint(0, 9))
cpf.append(7)
print(f'CPF: {cpf}')

# PRIMEIRO DÍGITO VERIFICADOR
produto = []
d = 0
for c in range(10, 1, -1):
    produto.append(c * cpf[d])
    d += 1
soma = sum(produto)
print(f'{produto}')
print(soma)
if soma % 11 >= 2:
    pd = 11 - soma % 11
else:
    pd = 0
cpf.append(pd)
print(f'CPF: {cpf}')
#SEGUNDO DÍGITO VVERIFICADOR
n = 0
p = []
for x in range(11, 1, -1):
    p.append(x * cpf[n])
    n += 1
s = sum(p)
#soma = sum(produto)
print(p)
print(s)
if s % 11 >= 2:
    sd = 11 - s % 11
else:
    sd = 0
cpf.append(sd)
for n in cpf:
    print(f'{n}', end='')
