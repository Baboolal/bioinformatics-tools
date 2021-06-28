# Translates DNA to AA mark 3, hopefully its faster and can translate 3 frames
# main feature: you get to visually pick the frame you want

from Bio import SeqIO
from Bio.Seq import Seq, reverse_complement, translate
from Bio.SeqRecord import SeqRecord

# colour printer
def colour_printer(aa_seq):
    M_state = False
    for letter in aa_seq:
        if letter == "M":
            M_state = True
        elif letter == "*":
            M_state = False

        if M_state and (letter != "C"):
            print("\033[0;30;41m{}".format(letter), end="") # print highlighted
        elif M_state and (letter == "C"):
            print("\033[0;30;44m{}".format(letter), end="") # print a cysteine
        elif letter == "C":
            print("\033[0;30;44m{}".format(letter), end="") # print a cysteine
        else:
            #print("\033[0;37;40m{}".format(letter), end="") # print normal
            print("\033[0m{}".format(letter), end="") # print normal
    
    print("\033[0m") # newline

# storage of AA sequence in list (frame 1 translaton is default)
aa_seq_data = []

# iterate and convert DNA to AA
for row in SeqIO.parse(r"translate_tester.txt", "fasta"):
    frame_n_seq = [] # declare
    print(row.id)
    frame_n_seq.append(translate(str(row.seq))) # frame 1
    frame_n_seq.append(translate(str(row.seq)[1:])) # frame 2
    frame_n_seq.append(translate(str(row.seq)[2:])) # frame 3
    frame_n_seq.append(str(translate(reverse_complement(row.seq)[2:]))) # frame -3
    frame_n_seq.append(str(translate(reverse_complement(row.seq)[1:]))) # frame -2
    frame_n_seq.append(str(translate(reverse_complement(row.seq)))) # frame -1
    print("Frame 1: ", end="") # replace all these prints with colour printer
    colour_printer(frame_n_seq[0])
    print("Frame 2: ", end="")
    colour_printer(frame_n_seq[1])
    print("Frame 3: ", end="")
    colour_printer(frame_n_seq[2])
    print("Frame -1: ", end="")
    colour_printer(frame_n_seq[-1])
    print("Frame -2: ", end="")
    colour_printer(frame_n_seq[-2])
    print("Frame -3: ", end="")
    colour_printer(frame_n_seq[-3])

    # choice
    choice = int(input("What frame you want? "))
    while (choice < -3) or (choice > 3) or (choice == 0):
        choice = int(input("Out of range. What frame you want? "))
    
    if choice > 0:
        choice -= 1

    #print("Debug: ", frame_n_seq[choice]) # debug

    # print some lines
    print("----------------------------------------------")

    frame_record = SeqRecord(
        Seq(frame_n_seq[choice]),
        id = row.id,
        description = row.description,
    )
    aa_seq_data.append(frame_record)

# write all files here
SeqIO.write(aa_seq_data, "translate_tester_aa.txt", "fasta")