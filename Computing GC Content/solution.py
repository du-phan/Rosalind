def computing(DNA):
	return 100 * (DNA.count('C') + DNA.count('G'))/ float(len(''.join(DNA.splitlines())))

def GCcontent(link):
	file = open(link,'rU')
	l = file.readlines()
	DNA_list = []
	dna = ''
	for n in l:
		if n.startswith('>'):
			if len(dna)!=0 : DNA_list.append(dna) 
			DNA_list.append(n)
			dna = ''
		else:
			dna += n
	if len(dna)!=0 : DNA_list.append(dna)
	
	list = {}
	length = len(DNA_list)/2
	for d in range(length):
		content = computing(DNA_list[2*d+1])
		list[content] = DNA_list[2*d]
	print list[max(list.keys())][1:]
	print round(max(list.keys()),6)

GCcontent('rosalind_gc.txt')
