import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from methods.interpolacao import lagrange, newton, gregory_newton
from methods.splines import spline_linear, spline_cubica_natural
from methods.ajustesCurvas import ajuste_linear_mmq, prever_reta
from methods.integracao import (
    simpson_38,
    trapezios_repetida,
    simpson_13,
    quadratura_gauss
)


def aproximadamente_igual(valor, esperado, tolerancia=0.0001):
    return abs(valor - esperado) <= tolerancia


def testar_lagrange_e_newton():
    x = [1.0, 2.0, 3.0, 4.0, 5.0]
    y = [1.2, 1.9, 3.2, 5.5, 8.2]

    resultado_lagrange = lagrange(x, y, 3.5)
    resultado_newton = newton(x, y, 3.5)

    print("Lagrange:", resultado_lagrange)
    print("Newton:", resultado_newton)

    assert aproximadamente_igual(resultado_lagrange, 4.2390625)
    assert aproximadamente_igual(resultado_newton, 4.2390625)


def testar_gregory_newton():
    x = [10, 20, 30, 40]
    y = [45.0, 52.0, 60.0, 71.0]

    resultado = gregory_newton(x, y, 25)

    print("Gregory-Newton:", resultado)

    assert aproximadamente_igual(resultado, 55.75)


def testar_splines():
    x = [0.0, 1.0, 2.0, 3.0]
    y = [2.5, 4.5, 3.0, 6.0]

    resultado_linear = spline_linear(x, y, 1.5)
    resultado_cubica = spline_cubica_natural(x, y, 1.5)

    print("Spline Linear:", resultado_linear)
    print("Spline Cúbica Natural:", resultado_cubica)

    assert aproximadamente_igual(resultado_linear, 3.75)
    assert aproximadamente_igual(resultado_cubica, 3.675)


def testar_mmq():
    x = [8, 9, 10, 11, 12]
    y = [2.1, 2.8, 3.1, 4.0, 4.8]

    a, b = ajuste_linear_mmq(x, y)
    previsao = prever_reta(a, b, 13)

    print("Coeficiente a:", a)
    print("Coeficiente b:", b)
    print("Previsão para 13h:", previsao)

    assert aproximadamente_igual(a, 0.66)
    assert aproximadamente_igual(b, -3.24)
    assert aproximadamente_igual(previsao, 5.34)


def testar_integracao():
    x1 = [0, 2, 4, 6]
    y1 = [10, 15, 12, 8]

    resultado_38 = simpson_38(x1, y1)

    print("Simpson 3/8:", resultado_38)

    assert aproximadamente_igual(resultado_38, 74.25)

    x2 = [0.0, 0.5, 1.0, 1.5, 2.0]
    y2 = [0, 40, 65, 80, 90]

    resultado_trapezios = trapezios_repetida(x2, y2)
    resultado_simpson = simpson_13(x2, y2)

    print("Trapézios:", resultado_trapezios)
    print("Simpson 1/3:", resultado_simpson)

    assert aproximadamente_igual(resultado_trapezios, 115.0)
    assert aproximadamente_igual(resultado_simpson, 116.6666666667)


def testar_gauss():
    def f(x):
        return 5 * x ** 3 + x ** 2 - 12 * x + 4

    resultado = quadratura_gauss(f, -1, 1, 2)

    print("Quadratura de Gauss:", resultado)

    assert aproximadamente_igual(resultado, 8.6666666667)


if __name__ == "__main__":
    testar_lagrange_e_newton()
    testar_gregory_newton()
    testar_splines()
    testar_mmq()
    testar_integracao()
    testar_gauss()

    print("\nTodos os testes passaram com sucesso!")