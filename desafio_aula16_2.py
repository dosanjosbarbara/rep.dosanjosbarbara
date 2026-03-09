# dados do exercicio
vendas_brutas = [
    (101, "Monitor", 5, 1200.0),
    (102, "Mouse", 50, 80.0),
    (103, "Teclado", 8, 150.0),
    (104, "Case", 3, 50.0)
]

# identifica estoque baixo
estoque_baixo = []
for p in vendas_brutas:
    if p[2] < 6:
        estoque_baixo.append(p)

#valor total do inventario
total_inventario = 0
for p in vendas_brutas:
    subtotal = p[2] * p[3]
    total_inventario += subtotal #valor acumulativo

#reajuste de 10%
vendas_reajustadas = []
for p in vendas_brutas:
    # Arredondando para 2 casas decimais aqui:
    preco_novo = round(p[3] * 1.10, 2)

    novo_item = (p[0], p[1], p[2], preco_novo)
    vendas_reajustadas.append(novo_item)

print(f"Reajustadas: {vendas_reajustadas}")