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

record.id \t species \t fullseq \n
'''

import requests as r
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from io import StringIO

# open input and output FASTA files
output_file = open("all_seq_with_full_seq_tdt.txt", "w")

# real deal
for record in SeqIO.parse("all_seq.fasta", "fasta"):
    print(record.id, end="\t") # debug
    if record.id.startswith("gnl"): # access onekp full sequence
        print("its gnl") # debug
        protein_id = record.id.split("|")[-1]
        print(protein_id) # debug
        species_name = record.description.split(" ")[-1].replace("_", " ")
        onekp_iterator = SeqIO.parse("every_onekp\\" + \
            protein_id.split("_")[0] + "-translated-protein.fa", "fasta")
        for entry in onekp_iterator:
            if protein_id.split("_")[-1] in entry.id:
                print(entry.id) # debug
                #print(record.id, species_name, str(entry.seq))
                output_file.write(record.id + "\t" + species_name + "\t" + str(entry.seq) + "\n")
    elif record.id.startswith("sp"): # access uniprot full sequence (if any)
        print("its sp") # debug
        species_name = record.description.split("[")[-1][:-1]
        protein_id = record.id.split("|")[1]
        print(protein_id) # debug
        cID = protein_id.split(".")[0]
        baseUrl="http://www.uniprot.org/uniprot/"
        currentUrl=baseUrl+cID+".fasta"
        response = r.post(currentUrl)
        cData=''.join(response.text)
        Seq=StringIO(cData)
        pSeq=list(SeqIO.parse(Seq,'fasta'))
        output_file.write(record.id + "\t" + species_name + "\t" + str(pSeq[-1].seq) + "\n")
    

# close files
output_file.close()