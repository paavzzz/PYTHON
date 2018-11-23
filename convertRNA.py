#This simply converts a DNA strand to an RNA strand. It is NOT the complement of it. The only difference between DNA and RNA sequence-wise
is uracil in place of thymine.

#Interestingly, a common DNA mutation is the spontaneous deamination of cytosine that converts it into uracil. The fact that DNA does not
contain uracil is what enables cells to differentiate from RNA! Or else it would be very hard to, other than perhaps methylation patterns
or some other regulatory markers.

#Regardless, this is a very simple function, but good to know how to do for easy replacement of sequences. Maybe this could be applied for
methylation patterns. 


def frequency(filepath):
  DNA = open(filepath,'r')
  DNA = DNA.read()
  DNA = DNA.replace('T','U');
  return DNA

DNA = frequency('./sequence.txt')
print(DNA)

