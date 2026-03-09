def pipeline_auditoria(lista_bruta):
    vendas_validadas = []
    relatorio_erros = []

    for venda in lista_bruta:
        id_prod, nome, qtd, preco = venda  # Isso "desempacota" a tupla

        # Regra 1: Preço negativo
        if preco < 0:
            relatorio_erros.append(f"ID {id_prod}: Valor Negativo (R$ {preco})")

        # Regra 2: Valor Atípico (acima de 10k)
        elif preco > 10000:
            relatorio_erros.append(f"ID {id_prod}: Valor Atípico (R$ {preco})")

        # Se passar nas duas, a venda é boa!
        else:
            vendas_validadas.append(venda)

    return vendas_validadas, relatorio_erros


# Chamando a função para ver o resultado:
limpos, erros = pipeline_auditoria(vendas)

print("--- Vendas Validadas ---")
print(limpos)

print("\n--- Relatório de Erros ---")
for e in erros:
    print(e)