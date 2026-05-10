import matplotlib.pyplot as plt
import pandas as pd

# 1. Данни (Вариационен ред)
data = [7, 11, 14, 15, 15, 17, 18, 20, 21, 30]
n = len(data)

# 2. Създаване на честотна таблица (точно по формулите ти)
df = pd.Series(data).value_counts().sort_index().reset_index()
df.columns = ['x_i', 'm_i']  # x_i е стажът, m_i е честотата
df['v_i'] = df['m_i'] / n    # Относителна честота
df['gamma_i'] = df['v_i'].cumsum()  # Кумулативна честота

print("Честотна таблица:")
print(df)

# 3. Визуализация на Хистограма
plt.figure(figsize=(10, 6))
plt.bar(df['x_i'].astype(str), df['m_i'], color='teal', edgecolor='black')

plt.title('Разпределение на честотите ($m_i$)', fontsize=14)
plt.xlabel('Трудов стаж ($x_i$)', fontsize=12)
plt.ylabel('Брой работници ($m_i$)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()