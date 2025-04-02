# num = 1

# while (num <= 10):
#     print(num)
#     num += 1
# print('laço encerrados!')

num = None

while True:
    print('Digite seu nome, ou x para finalizar:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem-vindo, {nome}')
print('Até logo!')


# Laço de repetição