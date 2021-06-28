# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 15:28:59 2020

@author: Baboolal

Example:
A0A270R5T5	Panicum hallii	Poaceae	Poales	CGQHAGGMLCPHNLCCSRSGLCGLGADYCGAGCQSGACCPSLRC
to
>A0A270R5T5|Panicum hallii|Poaceae|Poales
CGQHAGGMLCPHNLCCSRSGLCGLGADYCGAGCQSGACCPSLRC
"""

# read text file
peptide_file = open(r"cbfullseqs.txt", "r")
#peptide_data = peptide_file.read()
#peptide_data = remove_trailing_newlines(peptide_data)

# write text file
fasta_file = open(r"cbfullseqs_fasta.fa", "w")
for row in peptide_file:
    print(row) # debug
    fasta_file.write(">" + row.split("\t")[0] + "|") # ID
    fasta_file.write(row.split("\t")[1] + "|") # species
    fasta_file.write(row.split("\t")[2] + "|") # family
    fasta_file.write(row.split("\t")[3] + "\n") # order
    
    fasta_file.write(row.split("\t")[-1])

# close both files
peptide_file.close()
fasta_file.close()
