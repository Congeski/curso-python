# Operadores in e not in - entre e não está entre
# Strings são iteráveis
#  0 1 2 3 4 5 6 7
#  V i n i c i u s
# -8-7-6-5-4-3-2-1
# nome = 'Vinícius'
# print(nome[2])
# print(nome[-4])
# print('ius' in nome)
# print('0' in nome)
# print('ius' not in nome)
# print('0' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')