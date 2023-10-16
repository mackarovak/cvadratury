import numpy as np
import matplotlib.pyplot as plt

# Определение функции правых частей системы ОДУ
def f(t, y):
    return np.array([y[1], -y[0]])

# Начальные условия
t0, y0 = 0, np.array([0, 1])

# Конечный момент времени
tf = 10

# Шаг по времени
h = 0.01

# Создание массива временных точек
t = np.arange(t0, tf, h)

# Создание массива решений системы ОДУ
y = np.zeros((len(t), len(y0)))
y[0] = y0

# Явный метод Рунге-Кутта 4 порядка
for i in range(len(t)-1):
    k1 = f(t[i], y[i])
    k2 = f(t[i] + h/2, y[i] + h/2 * k1)
    k3 = f(t[i] + h/2, y[i] + h/2 * k2)
    k4 = f(t[i] + h, y[i] + h * k3)
    y[i+1] = y[i] + h/6 * (k1 + 2*k2 + 2*k3 + k4)

# Визуализация решения
plt.plot(t, y[:, 0], label='y(t)')
plt.plot(t, y[:, 1], label='y\'(t)')
plt.legend()
plt.xlabel('t')
plt.show()
