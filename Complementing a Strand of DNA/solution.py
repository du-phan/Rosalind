input = "GTCA"
complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
result = [] 
for i in reversed(input): 
    result.append(complement[i])
print ''.join(result)
