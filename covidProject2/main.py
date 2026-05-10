from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

input_file = "C:/Users/asus/Downloads/sequence.fasta"
genome_record = SeqIO.read(input_file, "fasta")
genome_seq = genome_record.seq

# 2. Официални координати на 4-те гена (базирани на NC_045512.2)
# Внимание: Индексите в Python започват от 0, затова вадим 1 от началото
genes_coords = {
    "Spike_S": (21562, 25384),
    "Envelope_E": (26244, 26472),
    "Membrane_M": (26522, 27191),
    "Nucleocapsid_N": (28273, 29533)
}

# 3. Извличане и запазване
gene_records = []
for name, (start, end) in genes_coords.items():
    gene_seq = genome_seq[start:end]
    # Създаваме нов запис за всеки ген
    record = SeqRecord(gene_seq, id=name, description=f"SARS-CoV-2 {name} gene")
    gene_records.append(record)

# 4. Записване във втория файл
output_file = "C:/Users/asus/Downloads/covid_genes.fasta"
SeqIO.write(gene_records, output_file, "fasta")

print(f"Готово! Вторият файл е създаден тук: {output_file}")
