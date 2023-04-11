"""
Fatiamento de strings
 012345678
 Olá Mundo
-987654321
Fatiamento [i:f:p] [::] p -> quantidade de caracteres que irá pular
Obs.: a função len retorna a qtd de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[-1:-10:-1])  # odnum álO
print(variavel[0:9:2])  # Oámno
print(variavel[0:len(variavel):1])  # Olá mundo
print(len(variavel[4:9]))  # 5
