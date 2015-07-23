def calculate(input):
	liste = input.split()
	liste = [ int(i) for i in liste]
	print 2*(liste[0]+liste[1]+liste[2]) + 2*0.75*liste[3] + 2*0.5*liste[4]

calculate('17302 19067 18006 19193 16050 16104')