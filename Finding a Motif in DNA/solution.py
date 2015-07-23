def motif(link):
	file = open(link, 'rU')
	l = file.readlines()
	l = [t.strip('\n') for t in l]
	s,t = l[0], l[1]
	s_list = list(s)
	result = []
	while (s.find(t) != -1):
		position = s.find(t)
		result.append(position+1)
		s_list[position] = '0'  
		s = "".join(s_list)
	print result



motif('rosalind_subs.txt')
