import re

def motif(link):	
	file = open(link,'rU')
	file = file.read().split()
	file = ''.join(file)
	dna = re.findall(r'\d+(\w+)>*',file)

	model = min(dna, key=len)
	criteria = ''
	found = True

	for i in range(len(model),0,-1):
		length = i-1
		counter = len(model) - length - 1 
		for j in range(counter+1): 
			criteria = model[j:j+length+1]
			for x in dna: 
				if x.find(criteria) == -1:
					found = False
					break
				found = True
			if found:
				return criteria
		counter += 1 

print motif('rosalind_lcsm.txt')





