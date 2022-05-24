class dnaString (str): 
    def __new__(self,s): 
        return str.__new__(self,s.upper()) 
    def length (self): 
        return (len(self)) 
    def getATCG (self,num_A,num_T,num_C,num_G): 
        num_A = self.count("A") 
        num_T = self.count("T") 
        num_C = self.count ("C") 
        num_G = self.count ("G") 
        return ( (self.length(), num_A, num_T, num_G, num_C) ) 

    def printnum_A (self): 
        print ("Adenine base content: {0}".format(self.count("A"))) 

dna = input("Enter a dna sequence: ") 
x=dnaString(dna) 
