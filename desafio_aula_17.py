# os dados serão armazenados na lista (relatorio_venda)
relatorio_vendas = []

#input de dados
# ciclo de coleta while
while True:

#apenas input pois deve considerar como nome
    nome_filial = input('Insira o nome da filial ou zero para encerrar ')
# definindo o break como "0" para entender como texto e não como numero, pois tratasse de input apenas
    if nome_filial == "0":
        break

# float(input('') para valores (dinheiro) pois aceita casas decimais
    valor_vendido = float(input('Insira o valor vendido ou digite zero para encerrar '))
# define um valor para encerrar
    if valor_vendido == 0:
        break #encerra a captação dos dados

#guarda os valores inseridos em relatorio_vendas dentro da indentação do while para inserir na lista
    relatorio_vendas.append((nome_filial, valor_vendido))

#retorna os resultados inseridos no while
#print(relatorio_vendas)

def limpar_vendas(relatorio_vendas):
    relatorio_validado = [] #será armanezado aqui as vendas que atendem os requisitos de >0 <10000
    for nome_filial, valor_vendido in relatorio_vendas:
        if valor_vendido > 0 and valor_vendido < 10000:
            relatorio_validado.append((nome_filial, valor_vendido))

    return relatorio_validado #devolve os valores validados

resultado_validado_final = limpar_vendas(relatorio_vendas) #recebe os valores de relatorio_validado da função e armazena em resultado_validado_final

print('relatorio bruto ')
print(relatorio_vendas)
print('relatorio validado ')
print(resultado_validado_final)

# função de analise de dados
def analise(relatorio_validado):
    #caso a lista esteja vazia, retornará (0, 0)
    if len(relatorio_validado) == 0:
        return (0, 0)

    total = 0
    for nome_filial, valor_vendido in relatorio_validado:
        total += valor_vendido

    quantidade = len (relatorio_validado)
    media = total / quantidade

    return(total, media)

faturamento_total, media_faturamento = analise(resultado_validado_final)

print('resultado da analise dos dados inseridos')
print(f"Faturamento Total: R$ {faturamento_total:.2f}")
print(f"Média das Vendas: R$ {media_faturamento:.2f}")

# classificação de performance
def definir_status(media):
    if media > 5000:
        return "Alta Performance"
    elif 2000 <= media <= 5000:
        return "Performance Estável"
    else:
        return "Performance Crítica"

#relatorio de saida
status_performance = definir_status(media_faturamento)

# 5. Relatório de Saída (Exibição)
print("\n" + "="*40)
print(f"{'RELATÓRIO DE VENDAS DA FILIAL':^40}")
print("="*40)

# Exibe o status e os valores financeiros
print(f"Status de Performance: {status_performance}")
print(f"Faturamento Total:     R$ {faturamento_total:.2f}")
print(f"Média das Vendas:      R$ {media_faturamento:.2f}")
print("-"*40)

# Listagem numerada das vendas válidas
print("Listagem de Vendas Válidas:")
if not resultado_validado_final:
    print("Nenhuma venda válida registrada.")
else:
    # O enumerate() cria o índice (i) começando em 1
    for i, (filial, valor) in enumerate(resultado_validado_final, start=1):
        print(f"{i}. Filial: {filial} | Valor: R$ {valor:.2f}")

print("="*40)