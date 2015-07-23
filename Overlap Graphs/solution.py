import re

def overlap(link): 
	file = open(link,'rU')
	liste = file.read().split('\n')
	liste = ''.join(liste)
	result = []

	tuple = re.findall(r'(Rosalind_\d+)(\w+)>*', liste)

	for k1, v1 in tuple:
    		for k2, v2 in tuple:
	            if k1 != k2 and v1.endswith(v2[:3]):
	                result.append((k1, k2))
	                
	for k,v in result:
		print k,v


overlap('rosalind_grph.txt')