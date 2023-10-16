import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

# определяем веса
weights = np.array([0.0, 0.0])
# определяем пороговое значение
bias = 0.0
# устанавливаем коэффициент обучения
learning_rate = 0.1

# определяем функцию активации (ступенчатая функция)
def activation_function(z):
    if z >= 0:
        return 1
    else:
        return 0

# обучаем персептрон
for epoch in range(10):
    for i in range(len(X)):
        # вычисляем взвешенную сумму
        weighted_sum = np.dot(X[i], weights) + bias
        # применяем функцию активации
        result = activation_function(weighted_sum)
        # вычисляем ошибку
        error = y[i] - result
        # обновляем веса и пороговое значение
        weights = weights + learning_rate * error * X[i]
        bias = bias + learning_rate * error

# проверяем работу персептрона на новых данных
new_data = np.array([-2,2])
weighted_sum = np.dot(new_data, weights) + bias
result = activation_function(weighted_sum)
print(result) 
