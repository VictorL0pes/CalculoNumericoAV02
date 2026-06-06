def spline_linear(x, y, valor):
    n = len(x)

    for i in range(n - 1):
        if x[i] <= valor <= x[i + 1]:
            return y[i] + ((y[i + 1] - y[i]) / (x[i + 1] - x[i])) * (valor - x[i])

    raise ValueError("O valor está fora do intervalo dos dados.")


def resolver_sistema_gauss(A, b):
    n = len(A)

    matriz = []
    for i in range(n):
        matriz.append(A[i].copy() + [b[i]])

    for coluna in range(n):
        pivo = coluna

        for linha in range(coluna + 1, n):
            if abs(matriz[linha][coluna]) > abs(matriz[pivo][coluna]):
                pivo = linha

        matriz[coluna], matriz[pivo] = matriz[pivo], matriz[coluna]

        if matriz[coluna][coluna] == 0:
            raise ValueError("Sistema sem solução única.")

        divisor = matriz[coluna][coluna]

        for j in range(coluna, n + 1):
            matriz[coluna][j] /= divisor

        for linha in range(n):
            if linha != coluna:
                fator = matriz[linha][coluna]

                for j in range(coluna, n + 1):
                    matriz[linha][j] -= fator * matriz[coluna][j]

    solucao = []

    for i in range(n):
        solucao.append(matriz[i][n])

    return solucao


def spline_cubica_natural(x, y, valor):
    n = len(x) - 1
    h = []

    for i in range(n):
        h.append(x[i + 1] - x[i])

    A = []
    b = []

    for i in range(n + 1):
        A.append([0] * (n + 1))
        b.append(0)

    A[0][0] = 1
    A[n][n] = 1

    for i in range(1, n):
        A[i][i - 1] = h[i - 1]
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]

        b[i] = 3 * (
            (y[i + 1] - y[i]) / h[i]
            - (y[i] - y[i - 1]) / h[i - 1]
        )

    c = resolver_sistema_gauss(A, b)

    a = y.copy()
    b_coef = []
    d = []

    for i in range(n):
        b_i = ((y[i + 1] - y[i]) / h[i]) - (h[i] * (2 * c[i] + c[i + 1]) / 3)
        d_i = (c[i + 1] - c[i]) / (3 * h[i])

        b_coef.append(b_i)
        d.append(d_i)

    for i in range(n):
        if x[i] <= valor <= x[i + 1]:
            dx = valor - x[i]
            return a[i] + b_coef[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3

    raise ValueError("O valor está fora do intervalo dos dados.")