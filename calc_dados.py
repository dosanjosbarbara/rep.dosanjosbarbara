def validar_vetores(v1, v2):
    if len(v1) != len(v2):
        raise ArithmeticError("Os vetores devem ter o mesmo tamanho!")
    return True


if __name__ == "__main__":
    obs = [1.2, 2.5, 3.8]
    pred = [1.0, 2.7, 4.0]

    print("Sistema iniciado com sucesso.")

def euclidiana(v1, v2):
    validar_vetores(v1, v2)
    soma_quadrados = sum((a - b) ** 2 for a, b in zip(v1, v2))
    return soma_quadrados ** 0.5


def produto_escalar(v1, v2):
    validar_vetores(v1, v2)
    return sum(a * b for a, b in zip(v1, v2))

