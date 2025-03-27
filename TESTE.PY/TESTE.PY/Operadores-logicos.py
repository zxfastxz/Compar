# Booleano('Operador logico'), (True e False)
# And, Or e Not

# idade = 15
# altura = 1.81

# resultado = (idade >= 18) and (altura >= 1.79)
# msg = 'Pode participar do torneio ? ' + str(resultado)

# print(msg)

# Progama de disparo de alarme
n1 = 1
n2 = 2
alarme = str

n1 = str(input("A porta está aberta? "))
n2 = str(input("A janela está aberta? "))
alarme = (n1 != n2)


if (alarme == True):
    print("O alarme foi disparado.")
# elif (n1 != n2):
#     (n1 == print('Feche a porta'))
# elif (n2 != n1):
#     (n1 == print('Feche a janela'))
else:
    print("O alarme está estável!")


# tem_dinheiro = False
# tem_dinheiro = not tem_dinheiro
# msg = 'Tem dinheiro? ' + str(tem_dinheiro)
# print(msg)