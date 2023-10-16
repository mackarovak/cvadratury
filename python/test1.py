import numpy as np

# Определение функции f(x)
def f(x):
    return x**2 - 10 * np.sin(x)

# Определение производной функции f(x)
def df(x):
    return 2*x - 10 * np.cos(x)

# Начальное приближение
x0 = 4

# Точность
eps = 1e-6

# Итерации метода Ньютона
k = 0
x = x0
while abs(f(x)) > eps:
    x = x - f(x) / df(x)
    k += 1

print("Минимум функции:", x)
print("Количество итераций:", k)
