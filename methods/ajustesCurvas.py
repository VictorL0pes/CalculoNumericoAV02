def ajuste_linear_mmq(x, y):
    n = len(x)

    soma_x = sum(x)
    soma_y = sum(y)
    soma_x2 = sum(valor ** 2 for valor in x)
    soma_xy = sum(x[i] * y[i] for i in range(n))

    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)
    b = (soma_y - a * soma_x) / n

    return a, b


def prever_reta(a, b, valor):
    return a * valor + b