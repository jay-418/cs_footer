# Original file
fin = open("footer.html", "rt")

# Modified file
fout = open("footer-min.html", "wt")

for line in fin:
	# Remove each line break
	fout.write(line.replace('\n', ''))

fin.close()
fout.close()