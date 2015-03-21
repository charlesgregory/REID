Created using Python3.4 for 64 bit, Biopython 1.64 for 64 bit, xlwt future 0.8, xlrd.
The program name is REIDv0.5.2 (Restriction Enzyme Identify version 0.5.2)
Created by Charles Gregory.

Only fasta files.The fasta file must be in the same directory as the program.

If it isn't, the Movefile option can do that or the multiple fasta
program can.

However, you must pull these fasta files from a seperate directory
and it will pull all those files in that directory.

Enter the complete file name including the fasta extension.

If you use the multiple prgram it will automatically analyze
all the .fasta files in the program directory.

Check the restriction enzyme(s) you want and whether you want
restriction sites or fragments or both.

Click Analyze.

The program will print the location of the RE site cuts and fragments in an
excel document saved to the directory of the program.

If nothing is printed there are no sites.

If you use the multiple program each .fasta will have a seperate sheet
in the excel file.

Simulate will find similar fragment ranges that are present within all
of the fasta files in the digest and report them back in txt file.
This is based on a simulation of a virtual gel digest. Currently the 
parameters are hard coded but that will change in future versions.

This program was created in an effort to make a connection
between clusters of fragment sizes from restricion enzyme digest of 
bacteriophages and bacteriophage clusters.

