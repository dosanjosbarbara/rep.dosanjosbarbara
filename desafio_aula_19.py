conquistas = 0
explorando = True

def passo3():
    decisao = input("Desejam 'escalar' ou 'contornar'? ")

    if decisao == "escalar":
        passo4()
    else:
        passo5()

def passo4():
    sucesso = input("A escalada deu certo? (sim/nao): ")

    if sucesso == "sim":
        print("Escalada concluída.")
    else:
        print("A escalada falhou.")

def passo5():
    print("Vocês contornaram a montanha.")

def passo7():
    global conquistas
    print("Coletando dados...")
    conquistas = conquistas + 1
    print("Conquistas:", conquistas)

print("Você chegou em Alphara-7 para explorar")

while explorando:

    encontrado = input("\nEncontraram obstáculo? (sim/nao): ")

    if encontrado == "sim":
        passo3()
    else:
        print("Caminho livre.")

    cientifico = input("Encontraram minerais ou vida? (sim/nao): ")

    if cientifico == "sim":
        passo7()

        continuar = input("Desejam 'continuar' ou 'retornar'? ")

        if continuar == "retornar":
            explorando = False
    else:
        print("Nada encontrado.")

print("Expedição finalizada!")
print("Total de conquistas:", conquistas)