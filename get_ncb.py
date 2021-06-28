# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:46:24 2020

@author: Baboolal

Remove CB from CRP. To get NCBs

ZYCD_scaffold_2042828	MPQVTSDENDDTCGVCGDGGELICCDHCPSTYHLRCLLLEEVPEGEWY
ZYCD_scaffold_2042914	ELLATLERHRSICTICADVPEEAVISCCGHVFCRQCISEKLATSDDTE
ZYCD_scaffold_2042914	ELLATLERHRSICTICADVPEEAVISCCGHVFCRQCISEKLATSDDTECPFAKCSMQLNTALIYSL
ZZEI_scaffold_2000667	AVRAGPGNKVVACKSACAAFGGERYCCTGIYGSPQQCKPTAYSKLFKTACPRAYSYAYDDPT
ZZEI_scaffold_2000668	AVRAGPGNKVVACKSACAAFGGERYCCTGIYGSPQQCKPTAYSKLFKTACPRAYSYAYDDPT
ZZEI_scaffold_2001646	IHEQRKAGVKWVCPRCRGGCGPGCSNCCNCGPCRKAQGLEPTGQL
"""

# function to remove trailing new lines
def remove_trailing_newlines(data):
    while data[-1] == "\n":
        data = data[:-1]
    return data

# load CB data as a list
cb_file = open("cball.txt", "r")
cb_string = remove_trailing_newlines(cb_file.read())
cb_list = cb_string.split("\n")

# load CRP file
crp_file = open("crpall.txt", "r")

# iterate CRP file, detect CB, write NCB
ncb_file = open("ncball.txt", "w")
for line in crp_file:
    if line.strip() in cb_list:
        continue
    else:
        ncb_file.write(line.strip())
        ncb_file.write("\n")
        
# close all files
cb_file.close()
crp_file.close()
ncb_file.close()