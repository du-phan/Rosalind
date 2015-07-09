def transcribing(link):
	file = open(linl,'rU')
	DNA = file.read()
	print(DNA.replace("T", "U"))

