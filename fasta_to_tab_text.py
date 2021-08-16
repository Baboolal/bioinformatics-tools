# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:39:04 2020
last modified: 16 Aug 2021

@author: Baboolal

FASTA to Tab-delimited text (Generic)
"""

# function to remove trailing new lines
def remove_trailing_newlines(data):
    while data[-1] == "\n":
        data = data[:-1]
    return data

# read text file
big_fasta_file = open(r"all_seq_filtered_M.fasta", "r")
big_fasta_data = big_fasta_file.read()
big_fasta_data = remove_trailing_newlines(big_fasta_data)

# split that damn file
# seq_flag indicates whether the program is currently inside the sequence portion
protein_info_lines = [] # init
protein_sequence = [] # init
protein_line = "" # init
seq_flag = False # init

for line in big_fasta_data.split("\n"):
    #print(line) # debug
    if line[0] == ">":
        if seq_flag:
            protein_sequence.append(protein_line)
            protein_line = "" # clear it for next entry
            seq_flag = False
        print(line[1:]) # debug
        protein_info_lines.append(line[1:])
    else:
        seq_flag = True
        print(line) # debug
        protein_line = protein_line + line
protein_sequence.append(protein_line) # settle the last entry

# write file
tab_text_file = open(r"all_seq_filtered_M_tdt.txt", "w")
counter = 0
for entry in protein_info_lines:
    if entry.split("|")[0] == "sp":
        print("sp")
        species_name = entry.split("[")[-1][:-1]
    elif entry.split("|")[0] == "gnl":
        print("gnl")
        species_name = entry.split(" ")[-1].replace("_", " ")

    tab_text_file.write(entry)
    tab_text_file.write("\t")
    tab_text_file.write(species_name)
    tab_text_file.write("\t")
    tab_text_file.write(protein_sequence[counter])
    tab_text_file.write("\n")
    counter += 1

# close files
big_fasta_file.close()
tab_text_file.close()