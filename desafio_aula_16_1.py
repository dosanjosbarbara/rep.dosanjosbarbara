# Dados iniciais da imagem
vendas_brutas = [
    (101, "Monitor", 5, 1200.0),
    (102, "Mouse", 50, 80.0),
    (103, "Teclado", 8, 150.0),
    (104, "Case", 3, 50.0)
]

# 1. Filtrar estoque baixo (ex: menor que 6)
estoque_baixo = [p for p in vendas_brutas if p[2] < 6]
print(f"Estoque baixo: {estoque_baixo}")

# 2. Calcular valor total do inventário
total_inventario = sum(p[2] * p[3] for p in vendas_brutas)
print(f"Total: R$ {total_inventario:.2f}")

# 3. Gerar lista com reajuste de 10%
vendas_reajustadas = []
for p in vendas_brutas:
    novo_item = (p[0], p[1], p[2], p[3] * 1.10)
    vendas_reajustadas.append(novo_item)
print(f"Reajustadas: {vendas_reajustadas}")