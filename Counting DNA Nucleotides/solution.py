def counting(string):
	file = open(string, "rU")
	dna = file.read()
	file.close()
	#print dna.count('A'),dna.count('G'),dna.count('C'),dna.count('T')
	print map(dna.count,"AGCT")

counting("dna.txt")

