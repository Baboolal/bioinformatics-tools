# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:37:27 2020

@author: Baboolal

Family | Species list generator
"""

# function to remove trailing new lines
def remove_trailing_newlines(data):
    while data[-1] == "\n":
        data = data[:-1]
    return data

# read text files
species_file = open(r"species_lineage.txt", "r")
species_data = species_file.read()
species_data = remove_trailing_newlines(species_data)
nodes_file = open(r"nodes.dmp", "r")
lineage_file = open(r"fullnamelineage.dmp", "r", encoding="utf8")

# just get family
family_taxids = []
for line in nodes_file:
    #print(line.strip().split("\t")[4]) # debug
    if line.strip().split("\t")[4] == "family":
        #print(line.strip().split("\t")[0]) # debug
        family_taxids.append(line.strip().split("\t")[0])
        
# dict: taxid and name
full_taxids_dict = {}
for line in lineage_file:
    #print(line) # debug
    full_taxids_dict[line.strip().split("\t")[0]] = line.strip().split("\t")[2]
        
# species' families
species_name = []
species_family_taxids = []
for entry in species_data.split("\n"):
    #print(entry) # debug
    ok = 0
    species_name.append(entry.split("\t")[0])
    for taxid in entry.split("\t")[1].split(" "):
        if taxid in family_taxids:
            species_family_taxids.append(taxid)
            ok = 1
            break
    if ok == 0:
        species_family_taxids.append(-1)
            
# family taxid to family name
species_family_name = []
for taxid in species_family_taxids:
    try:
        species_family_name.append(full_taxids_dict[str(taxid)])
    except KeyError:
        species_family_name.append("no rank")
        
# write out family species file
family_species_file = open(r"family_species.txt", "w")
counter = 0
for name in species_family_name:
    family_species_file.write(name)
    family_species_file.write("\t")
    family_species_file.write(species_name[counter])
    family_species_file.write("\n")
    counter += 1
        
# close files
species_file.close()
nodes_file.close()
lineage_file.close()
family_species_file.close()