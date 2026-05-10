from Bio import SeqIO
import matplotlib.pyplot as plt

def analyze_covid_genetics(file_path):
    # 1. Зареждане на последователността
    try:
        record = SeqIO.read(file_path, "fasta")
        sequence = record.seq
        print(f"Анализ на: {record.description}")
        print(f"Обща дължина: {len(sequence)} нуклеотида")
    except FileNotFoundError:
        print("Грешка: Файлът 'sequence.fasta' не е намерен!")
        return

    # 2. Преброяване на нуклеотидите
    counts = {
        'Аденин (A)': sequence.count("A"),
        'Цитозин (C)': sequence.count("C"),
        'Гуанин (G)': sequence.count("G"),
        'Тимин (T)': sequence.count("T")
    }

    labels = list(counts.keys())
    values = list(counts.values())
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

    # 3. Създаване на графиките
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Кръгова диаграма (Pie Chart)
    ax1.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
    ax1.set_title("Процентно разпределение на нуклеотидите")

    # Стълбовидна диаграма (Bar Chart)
    ax2.bar(labels, values, color=colors)
    ax2.set_ylabel('Брой нуклеотиди')
    ax2.set_title('Количество на нуклеотидите в генома')

    plt.tight_layout()
    plt.show()

# Стартиране на анализа
analyze_covid_genetics("C:/Users/asus/Downloads/sequence.fasta")