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


n1 = str(input("A porta está aberta? (sim/não) ")).strip().lower()
n2 = str(input("A janela está aberta? (sim/não) ")).strip().lower()
alarme = (n1 != n2)


# Se a porta estiver aberta e a janela fechada
if n1 == "sim" and n2 == "não":
    print("Feche a porta")
# Se a janela estiver aberta e a porta fechada
elif n2 == "sim" and n1 == "não":
    print("Feche a janela")
# Se ambos estiverem abertos
elif n1 == "sim" and n2 == "sim":
    print("O alarme foi disparado!")
# Se ambos estiverem fechados
else:
    print("O alarme está estável!")

# porta_aberta = input("A porta está aberta? (sim/não) ").strip().lower() == "sim"
# janela_aberta = input("A janela está aberta? (sim/não) ").strip().lower() == "sim"

# # Se a porta estiver aberta e a janela fechada
# if porta_aberta and not janela_aberta:
#     print("Feche a porta")
# # Se a janela estiver aberta e a porta fechada
# elif janela_aberta and not porta_aberta:
#     print("Feche a janela")
# # Se ambos estiverem abertos
# elif porta_aberta and janela_aberta:
#     print("O alarme foi disparado!")
# # Se ambos estiverem fechados
# else:
#     print("O alarme está estável!")


# if (alarme == True):
#     print("O alarme foi disparado.")
# elif n1 == "sim" and n2 == "não":
#     print('Feche a porta', '\n')
# elif n2 == "sim" and n1 == "não":
#     print('Feche a janela')
# else:
#     print("O alarme está estável!")


# tem_dinheiro = False
# tem_dinheiro = not tem_dinheiro
# msg = 'Tem dinheiro? ' + str(tem_dinheiro)
# print(msg)