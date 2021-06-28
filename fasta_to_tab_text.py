# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:39:04 2020

@author: Baboolal

FASTA to Tab-delimited text (Generic)
"""

# function to remove trailing new lines
def remove_trailing_newlines(data):
    while data[-1] == "\n":
        data = data[:-1]
    return data

# read text file
big_fasta_file = open(r"violas_cyclotided.txt", "r")
big_fasta_data = big_fasta_file.read()
big_fasta_data = remove_trailing_newlines(big_fasta_data)

# split that damn file
protein_info_lines = []
protein_sequence = []
for line in big_fasta_data.split("\n"):
    #print(line) # debug
    if line[0] == ">":
        print(line[1:]) # debug
        protein_info_lines.append(line[1:])
    else:
        print(line) # debug
        protein_sequence.append(line)

# write file
tab_text_file = open(r"violas_cyclotided_output.txt", "w")
counter = 0
for entry in protein_info_lines:
    tab_text_file.write(entry)
    tab_text_file.write("\t")
    tab_text_file.write(protein_sequence[counter])
    tab_text_file.write("\n")
    counter += 1

# close files
big_fasta_file.close()
tab_text_file.close()