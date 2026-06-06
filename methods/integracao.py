def simpson_38(x, y):
    h = x[1] - x[0]

    if len(x) != 4 or len(y) != 4:
        raise ValueError("A Regra 3/8 simples exige exatamente 4 pontos.")

    return (3 * h / 8) * (y[0] + 3 * y[1] + 3 * y[2] + y[3])


def trapezios_repetida(x, y):
    h = x[1] - x[0]
    n = len(x)

    soma = y[0] / 2 + y[n - 1] / 2

    for i in range(1, n - 1):
        soma += y[i]

    return h * soma


def simpson_13(x, y):
    n = len(x) - 1

    if n % 2 != 0:
        raise ValueError("A Regra 1/3 de Simpson exige número par de subintervalos.")

    h = x[1] - x[0]

    soma = y[0] + y[-1]

    for i in range(1, n):
        if i % 2 == 0:
            soma += 2 * y[i]
        else:
            soma += 4 * y[i]

    return (h / 3) * soma


def quadratura_gauss(funcao, a, b, n_pontos):
    if n_pontos == 2:
        raiz = 1 / (3 ** 0.5)
        pontos = [-raiz, raiz]
        pesos = [1, 1]

    elif n_pontos == 3:
        raiz = (3 / 5) ** 0.5
        pontos = [-raiz, 0, raiz]
        pesos = [5 / 9, 8 / 9, 5 / 9]

    else:
        raise ValueError("Este projeto aceita apenas n_pontos = 2 ou n_pontos = 3.")

    soma = 0

    for i in range(n_pontos):
        t = pontos[i]
        x_transformado = ((b - a) / 2) * t + ((a + b) / 2)

        soma += pesos[i] * funcao(x_transformado)

    return ((b - a) / 2) * soma