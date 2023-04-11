nome = 'Vinicius Congeski'
altura = 1.84
peso = 120
imc = peso / altura ** 2

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Vinicius Congeski tem 1.84 de altura,
# pesa 120 quilos e seu IMC é
# 35.44