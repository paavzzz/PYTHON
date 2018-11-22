#This python function reads a text file and relays information about the basic raw count of nucleotides in the DNA sequence.
#For practice, I utilized 3 different methods of formatted printing in Python3, for my own personal reference/notes.

def frequency(filepath):
  DNA = open(filepath,'r')
  DNA = DNA.read()
  a = DNA.count('A')
  c = DNA.count('C')
  t = DNA.count('T')
  g = DNA.count('G')

  list = [a,c,g,t]
  print (" ".join(str(x) for x in list))
  
  print("\n")
  
  print(*list)

  print("\n")
  
  print('A: {}'.format(list[0]))
  print('C: {}'.format(list[1]))
  print('T: {}'.format(list[2]))
  print('G: {}'.format(list[3]))
  
 

frequency('./sequence.txt')
