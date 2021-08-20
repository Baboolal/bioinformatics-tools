# get full sequence but onekp
'''
Created on 19 Aug 2021

input:
>gnl|onekp|RMVB_scaffold_2006997 Avena_fatua
CPGNQCCSKWGYCGLGGDYCGAGCQSGPCTRAKLNENVVPGNACSSSSPCPSNQCCSKWGYCGLGGDYCGSGCQSGPCTG
AMLNEDGVPNACSSSSPCPGNQCCSKWGYCGLGGDY
>sp|P15312.1| RecName: Full=Root-specific lectin; Flags: Precursor [Hordeum vulgare]
MKMMSTRALALGAAAVLAFAAATAHAQRCGEQGSNMECPNNLCCSQYGYCGMGGDYCGKGCQNGACYTSKRCGTQAGGKT
CPNNHCCSQWGYCGFGAEYCGAGCQGGPCRADIKCGSQAGGKLCPNNLCCSQWGYCGLGSEFCGEGCQGGACSTDKPCGK
AAGGKVCTNNYCCSKWGSCGIGPGYCGAGCQSGGCDGVFAEAIAANSTLVAE

output (header species full_seq)
gnl|onekp|RMVB_scaffold_2006997 Avena fatua MMMCPGNQC....CGYTC
gnl|onekp|RMVB_scaffold_2006997 Avena fatua MMMCPGNQC....CGYTC
'''

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# open input and output FASTA files
output_file = open("all_seq_with_full_seq_tdt.txt", "w")

# real deal
for record in SeqIO.parse("all_seq.fasta", "fasta"):
    print(record.id, end="\t") # debug
    if record.id.startswith("gnl"): # access onekp full sequence
        print("its gnl") # debug
        protein_id = record.id.split("|")[-1]
        print(protein_id) # debug
        onekp_iterator = SeqIO.parse("every_onekp\\" + \
            protein_id.split("_")[0] + "-translated-protein.fa", "fasta")
        for entry in onekp_iterator:
            if protein_id.split("_")[-1] in entry.id:
                print(entry.id) # debug
    elif record.id.startswith("sp"): # access uniprot full sequence (if any)
        print("its sp") # debug
        protein_id = record.id.split("|")[1]
        print(protein_id) # debug

# close files
output_file.close()