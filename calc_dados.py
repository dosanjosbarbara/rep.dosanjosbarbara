def validar_vetores(v1, v2):
    if len(v1) != len(v2):
        raise ArithmeticError("Os vetores devem ter o mesmo tamanho!")
    return True


if __name__ == "__main__":
    obs = [1.2, 2.5, 3.8]
    pred = [1.0, 2.7, 4.0]

    print("Sistema iniciado com sucesso.")

def mae(v1, v2):
    validar_vetores(v1, v2)
    return sum(abs(a - b) for a, b in zip(v1, v2)) / len(v1)


def mse(v1, v2):
    validar_vetores(v1, v2)
    return sum((a - b) ** 2 for a, b in zip(v1, v2)) / len(v1)

