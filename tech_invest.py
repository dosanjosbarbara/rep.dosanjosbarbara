
# entrada de dados
nome = input("Digite seu nome: ")
renda = float(input("Digite sua renda mensal: "))
gastos = float(input("Digite seus gastos mensais: "))
coragem = int(input("Nivel de coragem (1 a 10): "))

# calculo da sobra
sobra = renda - gastos

# calculo da reserva de emergencia (6 meses)
reserva = gastos * 6

print("Relatorio de:", nome)

# verificando se esta no vermelho
if renda < gastos:
    print("Situacao: NEGATIVA")
    print("Voce esta gastando mais do que ganha.")
else:
    print("Situacao: POSITIVA")
    print("Voce ganha mais do que gasta.")
    print("Sobra mensal calculada:", renda - gastos)  # refaz a conta

    # verificando reserva
    if sobra >= reserva:
        print("Voce ja teria uma reserva de 6 meses.")
    else:
        print("Sua reserva ideal deveria ser:", reserva)
        print("Atualmente sua sobra e:", sobra)
        print("Voce ainda nao atingiu a reserva ideal.")

print("Definindo perfil de investidor...")

# definicao do perfil (feito de forma simples)
if coragem >= 1 and coragem <= 3:
    perfil = "Conservador"
    investimento = "Tesouro Direto"
elif coragem >= 4 and coragem <= 7:
    perfil = "Moderado"
    investimento = "Fundos Imobiliarios"
elif coragem >= 8 and coragem <= 10:
    perfil = "Agressivo"
    investimento = "Acoes de Tecnologia"
else:
    perfil = "Indefinido"
    investimento = "Nenhum"

print("Perfil:", perfil)
print("Investimento recomendado:", investimento)

anos = int(input("Quantos anos deseja investir? "))

total = 0
ano = 1

print("Simulacao de crescimento:")

# simulacao simples
while ano <= anos:
    total = total + ((renda - gastos) * 12)
    print("Ano atual:", ano)
    print("Valor acumulado ate agora:", total)
    print("")
    ano = ano + 1

print("Fim da simulacao.")
print("Obrigado por usar o TechInvest!")