def prob(k,m,n):
	dominant = k*(m+n) + k*(k-1)/2 
	hetero = 0.75*m*(m-1)/2 + 0.5*m*n
	total = k*(k-1)/2 + m*(m-1)/2 + n*(n-1)/2 + k*m + k*n + m*n
	return (dominant + hetero)/float(total)

print prob(30,17,28)