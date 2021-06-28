# retrieve full sequence of protein
# input: fasta file of short sequences
# output1: tab-delimited file of: id <tab> short seq <tab> full seq
# output2: fasta file of the full sequences

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# read in the full sequences file into a dict (memory efficient)
full_record_dict = SeqIO.index("HC-1A-Trinity_aa_frame3.fa", "fasta")

# prep tab-delimited txt file to write
output_file = open("HC_cyclo_frame3_table.txt", "w")
fasta_file_write_entries = []

# real deal
for record in SeqIO.parse("HC_cyclo_frame3.fa", "fasta"):
    print(record.id, record.seq, full_record_dict[record.id.split("/")[0]].seq)
    output_file.write(str(record.id) + "\t" + str(record.seq) \
        + "\t" + str(full_record_dict[record.id.split("/")[0]].seq) + "\n")
    fasta_entry = SeqRecord(
        full_record_dict[record.id.split("/")[0]].seq,
        id = full_record_dict[record.id.split("/")[0]].id
    )
    fasta_file_write_entries.append(fasta_entry)

output_file.close()
SeqIO.write(fasta_file_write_entries, "HC_cyclo_frame3_full.fa", "fasta")