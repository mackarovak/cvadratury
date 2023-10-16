import numpy as np

# Определение интеграллая функции K(x, t)
def K(x, t):
    return np.exp(-x*t)

# Определение кусочно-линейной функции-базиса
def basis(x, i):
    if i == 0:
        return (1 - x)
    elif i == 1:
        return x
    else:
        return 0

# Начальное и конечное значения интервала интегрирования
a, b = 0, 1

# Различные значения числа частичных отрезков
Ns = [5, 10, 20, 50]

for N in Ns:
    # Создание матрицы системы
    A = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            integrand = lambda x: K(x, np.linspace(a, b, N)[j]) * basis(x, i) * (b-a)/N
            A[i][j] = np.trapz(integrand(np.linspace(a, b, N)), np.linspace(a, b, N))

    # Создание вектора правой части системы
    b = np.ones(N)

    # Решение системы линейных алгебраических уравнений
    c = np.linalg.solve(A, b)

    # Вычисление приближенного решения интегрального уравнения
    x = np.linspace(a, b, N)
    result = np.trapz(K(x.reshape(-1, 1), np.linspace(a, b, N)) @ c, x)

    print("Число частичных отрезков:", N)
    print("Значение интеграла:", result)
    print()
