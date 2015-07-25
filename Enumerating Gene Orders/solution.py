import itertools

def permutation(n):
	if n == 1: 
		return 1 
	else: 
		return n * permutation(n-1)

def enumerate(n):
	print permutation(n)
	for x in list(itertools.permutations([i for i in range(n,0,-1)])):
		for y in x:
			print y,
		print 

enumerate()