import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1. Зареждане на данните
df = pd.read_csv('C:/Users/asus/Downloads/temperatures.csv')

# Превръщаме таблицата в един списък (изключваме първата колона "Ден/Година")
# Премахваме '*' от 2026 и превръщаме всичко в числа
temp_data = df.iloc[:, 1:].values.flatten()
temp_data = pd.to_numeric(temp_data, errors='coerce')
temp_data = temp_data[~np.isnan(temp_data)]  # Премахваме празните стойности

# 2. Напасване на разпределенията
# Нормално разпределение
mu, std = stats.norm.fit(temp_data)

# Триъгълно разпределение
left, mode_param, width = stats.triang.fit(temp_data)

# Разпределение на Гъмбел (Extreme Value Analysis)
loc_g, scale_g = stats.gumbel_r.fit(temp_data)

# 3. Визуализация
plt.figure(figsize=(12, 7))
x = np.linspace(min(temp_data), max(temp_data), 100)

# Хистограма на реалните данни
plt.hist(temp_data, bins=30, density=True, alpha=0.5, color='gray', label='Данни (Януари)')

# Плотиране на кривите
plt.plot(x, stats.norm.pdf(x, mu, std), 'r-', lw=2, label=f'Нормално (μ={mu:.2f})')
plt.plot(x, stats.triang.pdf(x, left, mode_param, width), 'g-', lw=2, label='Триъгълно')
plt.plot(x, stats.gumbel_r.pdf(x, loc_g, scale_g), 'b-', lw=2, label='Гъмбел (Екстремни стойности)')

plt.title('Анализ на разпределението на температурите в Пловдив (1976-2026)')
plt.xlabel('Температура (°C)')
plt.ylabel('Плътност')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Печат на параметрите
print(f"Средна темп. (Нормално): {mu:.2f}°C")
print(f"Локация (Гъмбел): {loc_g:.2f}")