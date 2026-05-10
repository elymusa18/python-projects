import pandas as pd

# 1. Зареждаме файла, като прескачаме първия ред (където са само имената на градовете)
# Така ще използваме втория ред (Date, Temp. Avg...) като основни заглавия
df = pd.read_csv("C:/Users/asus/Downloads/exam_scores.csv", skiprows=1)

# 2. Премахваме колоните, които са изцяло празни (NaN)
df = df.dropna(axis=1, how='all')

# 3. Тъй като заглавията "Date", "Temp. Avg." и т.н. се повтарят,
# Pandas автоматично ги е кръстил "Date.1", "Date.2".
# Нека ги преименуваме ръчно, за да ни е лесно:

columns_mapping = {
    'Date': 'LA_Date', 'Temp. Avg.': 'LA_Temp', 'Week Count': 'LA_Week_Count', 'Week#': 'LA_Week_No', 'Avg': 'LA_Avg',
    'Date.1': 'CHI_Date', 'Temp. Avg..1': 'CHI_Temp', 'Week Count.1': 'CHI_Week_Count', 'Week#.1': 'CHI_Week_No', 'Avg.1': 'CHI_Avg',
    'Date.2': 'DC_Date', 'Temp. Avg..2': 'DC_Temp', 'Week Count.2': 'DC_Week_Count', 'Week#.2': 'DC_Week_No', 'Avg.2': 'DC_Avg'
}

df = df.rename(columns=columns_mapping)

# Показваме само колоните с температурите за проверка
print("--- Изчистена таблица (първи 5 реда) ---")
print(df[['LA_Date', 'LA_Temp', 'CHI_Temp', 'DC_Temp']].head())





