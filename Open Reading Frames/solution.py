def read(link):
	file = open(link,'rU')
	dna = file.read().split('\n')
	dnaList = [''.join(dna[1:])] 

	complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
	result = [] 
	for i in reversed(dnaList[0]): 
	    result.append(complement[i])
	dnaReverse =  ''.join(result)
	
	dnaList.append(dnaReverse)
	#print dnaList
	DNA_codon_table = { 'TTT': 'F',      'CTT': 'L',      'ATT': 'I',      'GTT': 'V',
						'TTC': 'F',      'CTC': 'L',      'ATC': 'I',      'GTC': 'V',
						'TTA': 'L',      'CTA': 'L',      'ATA': 'I',      'GTA': 'V',
						'TTG': 'L',      'CTG': 'L',      'ATG': 'M',      'GTG': 'V',
						'TCT': 'S',      'CCT': 'P',      'ACT': 'T',      'GCT': 'A',
						'TCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
						'TCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
						'TCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
						'TAT': 'Y',      'CAT': 'H',      'AAT': 'N',      'GAT': 'D',
						'TAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
						'TAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
						'TAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
						'TGT': 'C',      'CGT': 'R',      'AGT': 'S',      'GGT': 'G',
						'TGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
						'TGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
						'TGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G' } 
	
	listResult = []
	for dna in dnaList: 			
		while dna.find('ATG') != -1:
			start = dna.find('ATG')
			#print 'dna:',dna 
			result = ''
			#start = dna.find('ATG')
			#print 'start:',start
			check = 'ATG'
			counter = 0 
			stopped = True
			while check != 'TAG' and check != 'TGA' and check != 'TAA' and len(check) == 3: 
				codon = dna[start + 3*counter : start + 3*counter + 3]
				#print 'codon', codon
				result += DNA_codon_table[codon]
				check = dna[start + 3*counter + 3 : start + 3*counter + 6]
				counter += 1
				if check == '': 
					stopped = False
			if stopped:
				listResult.append(result)
			dna = dna[start+3:]
			#print '*** dna ***', dna
			#print len(dna)
	
	for x in list(set(listResult)):
		print x

result = read('test.txt')

'''
lst1 = ['MPAGGRFPQNFRPFCWTLFIGSEGQARLQIQGCGLLGPGRTVGGRNKMLGRVRDASLYFAQARGFSLSDVAGLVLYYTGLPLARTARSKRRLLAGH', 'MLGRVRDASLYFAQARGFSLSDVAGLVLYYTGLPLARTARSKRRLLAGH', 'MQVYILRKLGVFPCPM', 'M', 'MPGGHYKTKQKVQRLSTDYGEVHDLYRVATR', 'MAKFTIFTE', 'MCSLLGY', 'MARITRSPRGGSHRSAPRLGCTKDSSNFLPLCVAIKNVDYLHTLQRKLA', 'MRRQ', 'MVDCEVYK', 'MLTVGQILLTL']
lst2 = ['MRDASYKWATLTICRPHNRPYSGLIIQMPETRLLCKVTGGASYTGKTSRPV', 'MQVTSGPL', 'MPETRLLCKVTGGASYTGKTSRPV', 'MEVVDVLNSHTERQKIATILRAAQPRSTAVAAAPRAPCYPRHSRSAGSKAQ', 'MNTWRSSRSLPSSYSVKIVNFAIICRQPLDLLLRFVMPSGHEMFLVPRKQSSLGSGRPSERQTSVIENKSSYIGQGKTPSLRKI', 'MAKFTIFTE', 'MPSGHEMFLVPRKQSSLGSGRPSERQTSVIENKSSYIGQGKTPSLRKI', 'MKCS', 'MFLVPRKQSSLGSGRPSERQTSVIENKSSYIGQGKTPSLRKI']
lst3 = lst1 + lst2 

found = False
for x in lst3:
	for y in result:
		if x == y:
			found = True
			break 
	if not found :
		print "*****ERRROOOORRRRR******:",x
'''





