from methods.interpolacao import lagrange, newton, gregory_newton
from methods.splines import spline_linear, spline_cubica_natural
from methods.ajustesCurvas import ajuste_linear_mmq, prever_reta
from methods.integracao import (
    simpson_38,
    trapezios_repetida,
    simpson_13,
    quadratura_gauss
)


def executar_projeto():
    print("PROJETO DE CÁLCULO NUMÉRICO")
    print("-" * 50)

    x1 = [1.0, 2.0, 3.0, 4.0, 5.0]
    y1 = [1.2, 1.9, 3.2, 5.5, 8.2]
    valor1 = 3.5

    print("\n1. Interpolação - Lagrange e Newton")
    print("Lagrange:", lagrange(x1, y1, valor1))
    print("Newton:", newton(x1, y1, valor1))

    x2 = [10, 20, 30, 40]
    y2 = [45.0, 52.0, 60.0, 71.0]
    valor2 = 25

    print("\n2. Interpolação - Gregory-Newton")
    print("Gregory-Newton:", gregory_newton(x2, y2, valor2))

    x3 = [0.0, 1.0, 2.0, 3.0]
    y3 = [2.5, 4.5, 3.0, 6.0]
    valor3 = 1.5

    print("\n3. Splines")
    print("Spline Linear:", spline_linear(x3, y3, valor3))
    print("Spline Cúbica Natural:", spline_cubica_natural(x3, y3, valor3))

    x4 = [8, 9, 10, 11, 12]
    y4 = [2.1, 2.8, 3.1, 4.0, 4.8]
    valor4 = 13

    a, b = ajuste_linear_mmq(x4, y4)
    previsao = prever_reta(a, b, valor4)

    print("\n4. Ajuste Linear por MMQ")
    print(f"Reta: P1(x) = {a:.4f}x + ({b:.4f})")
    print("Previsão para x = 13:", previsao)

    x5 = [0, 2, 4, 6]
    y5 = [10, 15, 12, 8]

    print("\n5. Integração - Simpson 3/8")
    print("Total transferido:", simpson_38(x5, y5), "MB")

    x6 = [0.0, 0.5, 1.0, 1.5, 2.0]
    y6 = [0, 40, 65, 80, 90]

    print("\n6. Integração - Trapézios e Simpson 1/3")
    print("Trapézios:", trapezios_repetida(x6, y6), "km")
    print("Simpson 1/3:", simpson_13(x6, y6), "km")

    def f(x):
        return 5 * x ** 3 + x ** 2 - 12 * x + 4

    print("\n7. Quadratura de Gauss")
    print("Gauss n = 2:", quadratura_gauss(f, -1, 1, 2))


if __name__ == "__main__":
    executar_projeto()