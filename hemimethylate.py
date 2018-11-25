

#These set of functions mimic biochemical process that is a prerequisite for DNA repair machinery. They 
#methylate the original strand (adding methyl markers in place of adenosines), create a complimentary DNA,
#and overall check that hemimethylation is successful.

# Assumption: sequence in input file is written in 5' to 3' direction. 

import numpy as np

def methylate(filepath,output):
  DNA = open(filepath, 'r')
  f = open(output, 'w')
  DNA= DNA.read()
  f.write(DNA.replace('GATC','GmTC'));

def complimentary(filepath,output):
  DNA = open(filepath, 'r')
  f = open(output, 'w')
  DNA= DNA.read()
  DNA= DNA.translate(str.maketrans('ACTG','TGAC'))
  f.write(DNA)


def hemimethylate(filepath):
  DNA = open(filepath,'r')
  DNA = DNA.read()

  methylate(filepath,"methyl.txt")
  complimentary(filepath,"compliment.txt")

  m = open("methyl.txt",'r')
  m = m.read()

  c = open("compliment.txt",'r')
  c = c.read()

  m = np.array(list(m))
  c = np.array(list(c))

  c=np.array(np.where(c=='T'))
  m=np.array(np.where(m=='m'))
  #checks that m is a subset of c
  check1=np.isin(m,c)

  if check1.all:
    print("The DNA strand has been replicated and properly hemimethylated. Can be used to check MutH and MutL-MutS activity.\n")

hemimethylate("./sequence.txt")

