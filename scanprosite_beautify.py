# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:53:54 2020

@author: Tan Kwan Ann

Beautifies ScanProsite output to a format better suited for Excel

Instructions:
1. Search from ScanProsite, choose output format as Table
2. Copy paste the table and save it as a text file
3. Use this program

This program helps to format the data nicely so you can copy to Excel.
It also searches online for species names.
It removes dots from the sequences.

Notes: Stable as at 12 Oct 2020
implement numpy 2D array on 2 Mar 2021
"""

import urllib3
import numpy as np

# function to remove trailing new lines
def remove_trailing_newlines(data):
    while data[-1] == "\n":
        data = data[:-1]
    return data

# get lineage, version 1.1 hotfix
def lineage(species_name):
    # version 1 (5 Jan 2021)
    lineage_file = open("fullnamelineage.dmp", "r", encoding="utf-8")
    line_no = 0
    for line in lineage_file:
        #print("line {} in".format(line_no))
        line_no += 1
        if line.split("|")[1].strip() == species_name:
            print(line + "line number {}".format(line_no))
            break
    lineage_file.close()
    return [i.strip() for i in line.split("|")[-2].strip()[:-1].split(";")]

# determine taxonomic clade, version 1 (12 Jan 2021)
def taxoner(name):
    lineage_file = open("fullnamelineage.dmp", "r", encoding="utf-8")
    for line in lineage_file:
        if line.split("|")[1].strip() == name: # rmb to change back
            print(line)
            taxid = int(line.split("|")[0].strip())
            break
    lineage_file.close()
    
    nodes_file = open("nodes.dmp", "r", encoding="utf-8")
    for node_line in nodes_file:
        if int(node_line.split("|")[0].strip()) == taxid:
            print(node_line) # test
            taxon_clade = node_line.split("|")[2].strip()
            break
    nodes_file.close()
    return taxon_clade

# input species, get SFO, version 1 (12 Jan 2021)
def sfo(species_name):
    family_name = ""
    order_name = ""
    lineage_list = lineage(species_name)
    for index in lineage_list[::-1]:
        if taxoner(index) == "family":
            family_name = index
        elif taxoner(index) == "order":
            order_name = index
            
        if (bool(species_name) and bool(family_name) and bool(order_name)) == True:
            break
    return species_name, family_name, order_name

# some urllib3 configs
retries = urllib3.Retry(total=50)
http = urllib3.PoolManager(retries=retries)

# read from file
# this is the table format from scanprosite saved as text file
crazyass_file = open(r"crazyass1.txt", "r")
crazyass_data = crazyass_file.read()
crazyass_data = remove_trailing_newlines(crazyass_data)

# this part is the beautification process
# remove double newlines, extract impt data and write to new file
crazyass_data_wo_2newlines = crazyass_data.replace("\n\n", "\n")
#testfile = open(r"testfile.txt", "w") # debug
#testfile.write(crazyass_data_wo_2newlines) # debug
#testfile.close() # debug
beautiful_file = open(r"scanprosite_beautiful.txt", "w")
for row in crazyass_data_wo_2newlines.split("\n"):
    #print(row) # debug
    peptide_info = row.split(" ")[0]
    #print(peptide_info) # debug
    accession_number = peptide_info.split("|")[1]
    peptide_name = peptide_info.split("|")[-1]
    #print(accession_number, end="\t") # debug
    
    # look online for species names
    uniprot_fasta_url = "https://www.uniprot.org/uniprot/" + accession_number + ".fasta"
    fasta_file = http.request("GET", uniprot_fasta_url)
    fasta_file_decoded = fasta_file.data.decode('utf-8')
    header = fasta_file_decoded.split("\n")[0]
    #print(header) # debug
    recording = False
    species_name = ""
    for word in header.split(" "):
        #print(word, end=" ") # debug
        if word[0:3] == "OS=":
            recording = True
        if word[0:3] == "OX=":
            recording = False
        
        #print(recording) # debug
        if recording:
            species_name = species_name + word + " "
    species_name = species_name[3:-1]
    #print(species_name) # debug
    
    # family name, order name
    sfodatabase = np.array([]) # testing
    dummy, family_name, order_name = sfo(species_name)
        
    # look online for full sequence
    full_sequence = ""
    for line in fasta_file_decoded[:-1].split("\n"): # [:-1] removes "\n" at the end
        #print(line, end=" ") # debug
        if (line[0] != ">"):
            full_sequence = full_sequence + line
            #print("added") # debug
    #print(full_sequence) # debug
    
    # debug printing
    print(peptide_name, species_name, family_name, order_name,\
          row.split(" ")[-1].replace(".", "").replace("-", ""), "with full sequence")
    
    beautiful_file.write(peptide_name)
    beautiful_file.write("\t")
    beautiful_file.write(species_name)
    beautiful_file.write("\t")
    beautiful_file.write(family_name)
    beautiful_file.write("\t")
    beautiful_file.write(order_name)
    beautiful_file.write("\t")
    beautiful_file.write(row.split(" ")[-1].replace(".", "").replace("-", ""))
    beautiful_file.write("\t")
    beautiful_file.write(full_sequence)
    beautiful_file.write("\n")

# close files
crazyass_file.close()
beautiful_file.close()