import re
def counting(arr):
	return arr.count('A'), arr.count('C'), arr.count('G'), arr.count('T')


def profile(link):
	file = open(link,'rU')
	lst = file.read().split('\n')
	lst = ''.join(lst)
	lst = re.split(r'>Rosalind_\d+', lst) 
	lst = lst[1:]
	codon = ['A','C','G','T']
	matrix = []
	for i in range(len(lst[0])): 
		count_list = ''
		#while j < len(lst):
		for j in range(len(lst)): 
			count_list += lst[j][i]
		A,C,G,T = counting(count_list)
		matrix.append((A,C,G,T))

	result = ''
	for i in range(len(matrix)):
		result += codon[matrix[i].index(max(matrix[i]))]
	print result

	print "A:",
	for i in range(len(matrix)): 
		print matrix[i][0],

	print 

	print "C:",
	for i in range(len(matrix)): 
		print matrix[i][1],

	print 

	print "G:",
	for i in range(len(matrix)): 
		print matrix[i][2],

	print 

	print "T:",
	for i in range(len(matrix)): 
		print matrix[i][3],


profile('rosalind_cons.txt')