def counting(link):
	file = open(link,'rU')
	DNA_string = file.read()
	counter = 0
	length = len(DNA_string)/2 
	for x in range(len(DNA_string)/2): 
		if DNA_string[x] != DNA_string[length+x]:
			counter += 1
	print counter


#counting('rosalind_hamm.txt')




