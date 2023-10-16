import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# загружаем данные из файла
data = pd.read_csv('data.csv')

# создаем модель линейной регрессии
model = smf.ols('y ~ x', data=data)

# выводим результаты регрессии, включая оценки коэффициентов
results = model.fit()
print(results.summary())

# строим линию регрессии

fig, ax = plt.subplots()
ax.scatter(data['x'], data['y'])

# добавляем линию регрессии
ax.plot(data['x'], results.predict(), color='red')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Regression line')
plt.show()

# выводим результаты регрессии, включая тест на значимость коэффициентов
print(results.summary())

# тестируем значимость коэффициента beta1
print("p-value for beta1:", results.t_test("x=0").pvalue)

# выводим R^2
print("R-squared:", results.rsquared)
