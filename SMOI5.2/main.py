import matplotlib.pyplot as plt
import numpy as np

# Данни от условието
data = [7, 14, 11, 17, 17, 21, 15, 15, 18, 11, 15, 16, 20, 14, 25, 25, 35, 27, 24, 24,
        31, 28, 33, 25, 28, 33, 24, 7, 13, 21, 16, 22, 23, 28, 23, 27, 27, 31, 34, 34,
        37, 41, 20, 41, 13, 20, 20, 25, 30, 22, 22, 34, 31, 34, 24, 29, 34, 36, 8, 37]

# Параметри на интервалите
n = 60
k = 6
h = 6
start = 7
bins = [start + i*h for i in range(k + 1)] # [7, 13, 19, 25, 31, 37, 43]

# Изчисляване на честотите
counts, bin_edges = np.histogram(data, bins=bins)

# Намиране на средите на интервалите за полигона (x_i*)
bin_centers = bin_edges[:-1] + h/2

# Визуализация
plt.figure(figsize=(10, 6))

# 1. Хистограма
plt.hist(data, bins=bins, color='lightgray', edgecolor='black', alpha=0.7, label='Хистограма ($m_i$)')

# 2. Полигон (линия свързваща средите)
plt.plot(bin_centers, counts, color='red', marker='o', linestyle='-', linewidth=2, label='Полигон')

# Настройки на графиката
plt.title('Групиран статистически ред: Хистограма и Полигон', fontsize=14)
plt.xlabel('Трудов стаж (интервали)', fontsize=12)
plt.ylabel('Честота ($m_i$)', fontsize=12)
plt.xticks(bins) # Показва границите на интервалите върху оста X
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.show()