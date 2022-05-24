DNASeq = input("Enter a DNA sequence: ")

SeqLength = len(DNASeq)

print('Sequence Length:', SeqLength)

BaseKey = list(set(DNASeq)) #creates a list from the unique characters in the DNASeq

Dict = {}

for char in BaseKey:
	Dict[char] = 100*(DNASeq.count(char)/SeqLength)
print(Dict)
