import matplotlib.pyplot as plt
from Bio import SeqIO
from collections import Counter
import numpy as np

# Пътища (променете ги, ако е необходимо)
path_genome = "C:/Users/asus/Downloads/sequence.fasta"
path_genes = "C:/Users/asus/Downloads/covid_genes.fasta"

# 1. Данни за целия геном
genome_record = SeqIO.read(path_genome, "fasta")
c_gen = Counter(genome_record.seq)
len_gen = len(genome_record.seq)

# 2. Данни за отделните гени (S, E, M, N)
gene_counts = {}
for rec in SeqIO.parse(path_genes, "fasta"):
    gene_counts[rec.id] = Counter(rec.seq)

labels = ['A', 'T', 'C', 'G']
genes_order = ["Spike_S", "Envelope_E", "Membrane_M", "Nucleocapsid_N"]

# --- НОВИ, КОНТРАСТНИ ЦВЕТОВЕ ---
# Spike(S): Gold, Envelope(E): DeepPink, Membrane(M): LimeGreen, Nucleocapsid(N): DarkViolet
gene_colors = ['#FFD700', '#FF1493', '#32CD32', '#9400D3']

# Подготовка на данните за графиката
vals_gen = [c_gen[b] for b in labels]

# Визуализация
x = np.arange(len(labels))
width = 0.4

fig, ax = plt.subplots(figsize=(12, 7))

# Стълб 1: Пълен геном
rects1 = ax.bar(x - width / 2, vals_gen, width, label=f'Пълен Геном ({len_gen} bp)', color='skyblue', alpha=0.7)

# Стълб 2: Наслоени гени (Stacked Bar) с нови цветове
bottoms = np.zeros(len(labels))  # Начална точка (основа) за наслояването

for i, gene_name in enumerate(genes_order):
    if gene_name in gene_counts:
        # Вземаме броя бази за текущия ген
        current_gene_vals = [gene_counts[gene_name][b] for b in labels]

        # Рисуваме сегмента върху "bottoms" с новия цвят
        ax.bar(x + width / 2, current_gene_vals, width,
               bottom=bottoms, label=gene_name, color=gene_colors[i])

        # Обновяваме основата за следващия ген
        bottoms = np.add(bottoms, current_gene_vals)

# Настройки на графиката
ax.set_ylabel('Брой нуклеотиди')
ax.set_title('Анализ на COVID-19: Пълен геном vs Структурни гени (S, E, M, N)')
ax.set_xticks(x)
ax.set_xticklabels(['Аденин (A)', 'Тимин (T)', 'Цитозин (C)', 'Гуанин (G)'])
ax.legend()

# Етикети само за общия геном (за яснота)
ax.bar_label(rects1, padding=3)

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Извеждане на индивидуално GC съдържание за всеки ген (за статистиката)
print("\n--- GC съдържание по гени ---")
for g_name, counts in gene_counts.items():
    g_len = sum(counts.values())
    gc = (counts['G'] + counts['C']) / g_len * 100
    print(f"Ген {g_name}: {gc:.2f}%")