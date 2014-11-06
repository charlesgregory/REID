from Bio import SeqIO
for usrseq in SeqIO.parse(input("File Name"), "fasta"):
    print(usrseq.id)
    print(repr(usrseq.seq))
    print(len(usrseq))
    print(usrseq.seq.count("GAATTC")) #EcoRI
    print(usrseq.seq.count("GGATCC")) #BamHI
    print(usrseq.seq.count("AAGCTT")) #HindIII
    print(usrseq.seq.count("CCCGGG")) #SmaI
