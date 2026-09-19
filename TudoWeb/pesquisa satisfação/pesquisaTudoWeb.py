excelente = 0
bom = 0
ruim = 0

#Mensagem inicial
print("Essa é uma pesquisa de opinião feita pela empresa TudoWeb para medir o grau de satisfação de nossos clientes. Por favor responda:")

#Pesquisa
for i in range(50):
    nome = input("Informe seu nome:")
    idade = float (input("Informe sua idade:"))

    print("Opinião: Excelente - Bom - Ruim")
    avaliacao = input("De qual forma você avalia nossa empresa?:")

#Cálculo de satisfação
    if avaliacao == "Excelente":
        excelente = excelente + 1
    elif avaliacao == "Ruim":
        ruim = ruim + 1

#Resultado da pesquisa
    print("\n --- Grau de satisfação no atendimento --- ")
    print(f" Excelente: {excelente}")
    print(f" Ruim: {ruim}")
    print("\n --Agradecemos a colaboração!-- ")
