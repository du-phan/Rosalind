import numpy as np
import re 

def random_string(link):
	file = open(link,'rU')
	input = file.read()
	probaList = re.findall(r'(0\.\d+)', input)
	probaList = map(float,probaList)

	dna = input.split('\n')
	dna = ''.join(dna)
	dna = re.findall(r'(\w+)0.',dna)
	dna = dna[0]

	resultList=[]

	for proba in probaList: 
		result = 0
		for x in dna:
			if x=='G' or x=='C':
				result += np.log10(proba/2)
			else:
				result += np.log10((1-proba)/2)
		resultList.append(round(result,3))
	
	for y in resultList:
		print y, 

random_string('rosalind_prob.txt')	