# Simples, Composto, Encadeado

n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

# Calcular a média aritmétrica das notas
media = (n1 + n2) / 2

if (media >= 7):
    print("Resultado: Aprovado!")
    print("Parabéns!")
elif (media >= 5):
    print("O aluno está em recuperação.")
else:
    print('Aluno reprovado...')

print('Sua média é {}'.format(media))
