# Translates DNA to AA mark 3, hopefully its faster and can translate 3 frames
# main feature: you get to visually pick the frame you want

from Bio import SeqIO
from Bio.Seq import Seq, translate
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

# storage of AA sequence in list (declaration)
aa_seq_data = [[],[],[],[],[],[]]

# iterate and convert DNA to AA
for row in SeqIO.parse(r"HC-1A-Trinity.fa", "fasta"):
    frame_n_seq = [] # declare
    print(row.id)
    frame_n_seq.append(translate(str(row.seq))) # frame 1
    frame_n_seq.append(translate(str(row.seq)[1:])) # frame 2
    frame_n_seq.append(translate(str(row.seq)[2:])) # frame 3
    frame_n_seq.append(translate(str(row.seq)[::-1][2:])) # frame -3
    frame_n_seq.append(translate(str(row.seq)[::-1][1:])) # frame -2
    frame_n_seq.append(translate(str(row.seq)[::-1])) # frame -1
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

    # print some lines
    print("----------------------------------------------")

    # save data of all frames
    frames = [0, 1, 2, -1, -2, -3]

    for k in frames:
        frame_record = SeqRecord(
            Seq(frame_n_seq[k]),
            id = row.id,
            description = row.description,
        )
        aa_seq_data[k].append(frame_record)

# write all files here
SeqIO.write(aa_seq_data[0], "HC-1A-Trinity_aa_frame1.fa", "fasta")
SeqIO.write(aa_seq_data[1], "HC-1A-Trinity_aa_frame2.fa", "fasta")
SeqIO.write(aa_seq_data[2], "HC-1A-Trinity_aa_frame3.fa", "fasta")
SeqIO.write(aa_seq_data[-1], "HC-1A-Trinity_aa_frame-1.fa", "fasta")
SeqIO.write(aa_seq_data[-2], "HC-1A-Trinity_aa_frame-2.fa", "fasta")
SeqIO.write(aa_seq_data[-3], "HC-1A-Trinity_aa_frame-3.fa", "fasta")