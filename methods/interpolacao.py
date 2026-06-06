def lagrange(x, y, valor):
    n = len(x)
    resultado = 0

    for i in range(n):
        termo = y[i]

        for j in range(n):
            if i != j:
                termo *= (valor - x[j]) / (x[i] - x[j])

        resultado += termo

    return resultado


def coeficientes_newton(x, y):
    n = len(x)
    coef = y.copy()

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])

    return coef


def newton(x, y, valor):
    coef = coeficientes_newton(x, y)
    n = len(coef)

    resultado = coef[n - 1]

    for i in range(n - 2, -1, -1):
        resultado = resultado * (valor - x[i]) + coef[i]

    return resultado


def tabela_diferencas_finitas(y):
    tabela = [y.copy()]

    while len(tabela[-1]) > 1:
        linha_anterior = tabela[-1]
        nova_linha = []

        for i in range(len(linha_anterior) - 1):
            nova_linha.append(linha_anterior[i + 1] - linha_anterior[i])

        tabela.append(nova_linha)

    return tabela


def gregory_newton(x, y, valor):
    h = x[1] - x[0]
    p = (valor - x[0]) / h

    tabela = tabela_diferencas_finitas(y)

    resultado = tabela[0][0]
    produto_p = 1
    fatorial = 1

    for ordem in range(1, len(tabela)):
        produto_p *= p - (ordem - 1)
        fatorial *= ordem

        resultado += (produto_p / fatorial) * tabela[ordem][0]

    return resultado