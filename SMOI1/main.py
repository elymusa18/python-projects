import pandas as pd
import matplotlib.pyplot as plt

# 1. Зареждане и почистване (както преди)
df = pd.read_csv('C:/Users/asus/Downloads/SMOI2.csv', skiprows=1)
la_temp = df.iloc[:, 1].dropna()
chi_temp = df.iloc[:, 7].dropna()
dc_temp = df.iloc[:, 13].dropna()

# 2. Създаване на фигура с две подграфики
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# --- ХИСТОГРАМА ---
ax1.hist(la_temp, bins=20, alpha=0.5, label='Лос Анджелис', color='orange', edgecolor='white')
ax1.hist(chi_temp, bins=20, alpha=0.5, label='Чикаго', color='blue', edgecolor='white')
ax1.hist(dc_temp, bins=20, alpha=0.5, label='Вашингтон', color='green', edgecolor='white')

ax1.set_title('Разпределение на температурите (Хистограма)')
ax1.set_xlabel('Температура (°F)')
ax1.set_ylabel('Брой дни')
ax1.legend()
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# --- BOXPLOT ---
# Събираме данните в списък за boxplot
data_to_plot = [la_temp, chi_temp, dc_temp]
ax2.boxplot(data_to_plot, patch_artist=True, labels=['LA', 'Chicago', 'DC'],
            medianprops={'color': 'black', 'linewidth': 2},
            boxprops={'facecolor': 'lightblue', 'edgecolor': 'blue', 'alpha': 0.7})

ax2.set_title('Статистически диапазон (Boxplot)')
ax2.set_ylabel('Температура (°F)')
ax2.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()