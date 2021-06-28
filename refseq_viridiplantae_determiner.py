# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:40:30 2020

@author: Baboolal

RefSeq viridiplantae determiner arranger
"""

# function to remove trailing new lines
def remove_trailing_newlines(data):
    while data[-1] == "\n":
        data = data[:-1]
    return data

# read lineage file (large) and refseq file (large)
lineage_file = open(r"fullnamelineage.dmp", "r", encoding="utf8")
refseq_file = open(r"refseq.txt", "r")
lineage_data = lineage_file.read()
lineage_data = remove_trailing_newlines(lineage_data)
refseq_data = refseq_file.read()
refseq_data = remove_trailing_newlines(refseq_data)

# lineage data things
lineage_dict = {}
for line in lineage_data.split("\n"):
    cleaned_line = line.replace("\t", "")[:-2]
    # take only viridiplantae
    if "Viridiplantae" in cleaned_line.split("|")[-1]:
        #print(cleaned_line.split("|")[-1]) # debug
        lineage_dict[cleaned_line.split("|")[1]] = cleaned_line.split("|")[-1]
        
# output to file: species, viridiplantae or not
refseq_file_out = open(r"refseq_species_viridiplantae.txt", "w")
for line in refseq_data.split("\n")[1:]:
    # informational
    info_line = line.split("\t")[1]
    peptide_name = line.split("\t")[0]
    species_name = info_line.split("[")[-1][:-2]
    
    # sequence
    full_sequence = line.split("\t")[3]
    targets = line.split("\t")[-1]
    
    # process
    for seq in targets.split(","):
        print(peptide_name, species_name, seq, full_sequence, end=" ") # debug
        if species_name in lineage_dict:
            print("ViridiplantBAE") # debug
            refseq_file_out.write(peptide_name)
            refseq_file_out.write("\t")
            refseq_file_out.write(species_name)
            refseq_file_out.write("\t")
            refseq_file_out.write(seq)
            refseq_file_out.write("\t")
            refseq_file_out.write(full_sequence)
            refseq_file_out.write("\t")
            refseq_file_out.write("Viridiplantae")
            refseq_file_out.write("\n")
        else:
            print("ViridiplantNAYYYY (not written)") # debug
            
    
# close all files
lineage_file.close()
refseq_file.close()
refseq_file_out.close()