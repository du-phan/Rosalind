def enumerate(link):
	file = open(link,'rU')
	input = file.readlines()
	symbol = input[0].split()
	symbol = ''.join(symbol)
	n = int(input[-1])
	
	'''
	symbol_list = {}
	counter = 0
	for x in symbol: 
		symbol_list[counter] = x 
		counter += 1
	'''

	result = [[None]*n for i in range(len(symbol)**2)] #*(len(symbol)**2)
	repeat = 1
	counter = 1

	for b in range(n-1,-1,-1):
		x = 1
		j = 0 
		for a in range(len(result)):
			result[a][b] = symbol[j]
			#print 'result', result[a][b]
			x += 1 
			if x > repeat: 
				x = 1
				j = (j+1)%len(symbol)
		#print result
		repeat = len(symbol)*counter
		counter += 1


	for i in range(len(result)):
		output = []
		for j in range(n):
			output.append(result[i][j])
		output = ''.join(output)
		print output 





enumerate('rosalind_lexf.txt')


