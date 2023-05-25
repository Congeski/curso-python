"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = '1000'
string2 = 'vinicius'
# outra_variavel = f'{string[:3]}ABC{string[4:]}'    0 até o 3, e 4 até o final, irá incrementar ABC no meio
# print(string)
# print(outra_variavel)
print(string.zfill(10))  # Passa uma largura dentro do método, irá preencher a string com 0 a esquerda, até dar o valor passado no método.
print(string2.capitalize())  # Retorna o primeiro caractere Maiúsculo, método utilizado para strings
