#input file
fin = open("footer.html", "rt")
#output file to write the result to
fout = open("footer-min.html", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('\n', ''))
#close input and output files
fin.close()
fout.close()