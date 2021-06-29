# Translates DNA to AA mark 3, hopefully its faster and can translate 3 frames
# main feature: you get to visually pick the frame you want

from Bio import SeqIO
from Bio.Seq import Seq, translate
from Bio.SeqRecord import SeqRecord

# storage of AA sequence in list (declaration)
aa_seq_data = [[],[],[],[],[],[]]

# iterate and convert DNA to AA
for row in SeqIO.parse(r"seqdump_caripe1.txt", "fasta"):
    frame_n_seq = [] # declare
    #print(row.id)
    frame_n_seq.append(translate(str(row.seq))) # frame 1
    frame_n_seq.append(translate(str(row.seq)[1:])) # frame 2
    frame_n_seq.append(translate(str(row.seq)[2:])) # frame 3
    frame_n_seq.append(translate(str(row.seq)[::-1][2:])) # frame -3
    frame_n_seq.append(translate(str(row.seq)[::-1][1:])) # frame -2
    frame_n_seq.append(translate(str(row.seq)[::-1])) # frame -1

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
SeqIO.write(aa_seq_data[0], "seqdump_caripe1_aa_frame1.fa", "fasta")
SeqIO.write(aa_seq_data[1], "seqdump_caripe1_aa_frame2.fa", "fasta")
SeqIO.write(aa_seq_data[2], "seqdump_caripe1_aa_frame3.fa", "fasta")
SeqIO.write(aa_seq_data[-1], "seqdump_caripe1_aa_frame-1.fa", "fasta")
SeqIO.write(aa_seq_data[-2], "seqdump_caripe1_aa_frame-2.fa", "fasta")
SeqIO.write(aa_seq_data[-3], "seqdump_caripe1_aa_frame-3.fa", "fasta")