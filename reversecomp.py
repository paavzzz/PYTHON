#This function reads from a file a DNA string, and returns the reverse compliment of it!
#Simple and easy!

def reversecomp(filepath):
  DNA = open(filepath,'r')
  DNA = DNA.read()
  DNA =  DNA.translate(str.maketrans('ACTG','TGAC'))
  DNA = DNA[::-1]
  return DNA

DNA = reversecomp("./sequence.txt")
print(DNA)
