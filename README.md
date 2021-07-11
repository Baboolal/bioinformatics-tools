# bioinformatics-tools
Assorted Python scripts for accomplishing bioinformatics tasks and other relevant files\
This readme contains description of all uploaded scripts\
Uploaded scripts are works of Professor James P Tam Lab

Description and usage guidance of individual programs/files:\
crp_finder.py\
Finds CRPs from a collection of sequences by detecting high-density cysteine presence.\
Written by Choo Fang Ting.

dna2aa_mk3.py\
Translates a collection of DNA sequences in a FASTA file to amino-acid sequences.\
This program works like a game. The user have to choose 1 of 6 reading frames of translation that is correct.\
To use this, make sure input FASTA file is in the same directory (working directory)\
Change the following lines to match your input file and desired output file\
Line 33: for row in SeqIO.parse(r"<input_file>.txt", "fasta"):\
Line 76: SeqIO.write(aa_seq_data, "<output_file>.txt", "fasta")\
While the program runs, you have to choose the correct sequences, the output file will be based on your choices.

dna2aa_mk3_allframes_mk2.py\
Same as dna2aa_mk3 but this one translates all 6 frames automatically and saves all 6 translated files.\
Reading frames:\
1: 5'3' frame 1\
2: 5'3' frame 2\
3: 5'3' frame 2\
-1: 3'5' revcomp frame 1\
-2: 3'5' revcomp frame 2\
-3: 3'5' revcomp frame 3

family_species_list_generator.py

fasta_maker.py\
Converts tab-delimited text format into FASTA.\
Program will read .txt file and writes .fa file.

fasta_to_tab_text.py

get_full_sequence.py

get_ncb.py

refseq_viridiplantae_determiner.py

scanprosite_beautify.py

species_family_order.py

cyclotide_syntax.dat

translation_and_motif_search_detailed_v3.pdf
