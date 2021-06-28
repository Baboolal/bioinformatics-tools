# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:17:43 2020
version 2 update 12 Jan 2021

@author: Baboolal

Input file:
Draba sachalinensis
Maesa lanceolata
Leucodon brachypus
Selaginella kraussiana
Meliosma cuneifolia

Output file:
Draba sachalinensis	Brassicaceae	Brassicales
Maesa lanceolata	Primulaceae	Ericales
Leucodon brachypus	Leucodontaceae	Hypnales
Selaginella kraussiana	Selaginellaceae	Selaginellales
Meliosma cuneifolia	Sabiaceae	Proteales
"""

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

# main program below this line
# read text files
species_file = open(r"ncb_species.txt", "r")
        
# write the damned file
species_family_order_file = open(r"species_family_order.txt", "w")
for name in species_file:
    #print(name.strip()) # test
    species, family, order = sfo(name.strip())
    print("Output:", species, family, order)
    species_family_order_file.write(species + "\t" + family + "\t" + order + "\n")
    
# close files
species_file.close()
species_family_order_file.close()