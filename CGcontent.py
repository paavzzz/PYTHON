#These are 2 functions, both that accomplish the same thing. The top function has notably fewer lines of code, while the bottom uses numpy
and I would say is more general of a solution. It forced me to use numpy functions, while the top takes advantage of the .count function.

#Both of these functions serve to analyze the GC content of various DNA strands in a specified format. High GC content indicates high
mutation rate, but also indicates stronger and more stable DNA as 3 H bonds can be formed instead of just 2.
#In bacteria, GC rich content indicates elevated levels of heat-resistance! However, in terms of PCR high GC content indicates less
successful denaturation of DNA because of the higher melting point. :(

This is the format of the input file:
>FASTAseq_2974
GGTTTGGGCCTCGGTAAATTGAAGCCGTATCTCCAAAACGATTGGGACTATGAGGGACAC
>FASTAseq_9629
CTAAAATGATGAGTTCCCCCATACGGACCGGTAGCCACGCAGCCCCACTCCAGATGAGTC
>FASTAseq_5115
GCAGAGCCACGTGCTTGCGAATCTTAGTAGATAAAGGGGGGTGTCGTTGAGGCATGGTCG
>FASTAseq_6828
TTAGACCTTTCCGACCAAGTACTGCGAGGCCGAACGGAAGGTACCCATCCCGATAAGAAC
>FASTAseq_0757
ATAACTAGATTGCATGTAAGTCGCCTGAATGTGGTGCCTACGATTCAACCGTGAAGTCCG


import numpy as np

def gcontent2(filepath):
  fasta = open(filepath,'r')
  fasta = fasta.read()
  freqs = []
  
  #creates list with strings separated by >
  fasta = fasta.split(">")[1:]
  max = 0
  a = -1
  names = []

  for i in fasta:
    c = i.count("C")+i.count("G")
    total= i.count("C") + i.count("G") + i.count("A") + i.count("T")

    a = a+1

    freqs.append((c/total)*100)

    if(c>max):
      index = a
      max = c
 
  for i in range(len(fasta)):
    names.append(fasta[i][0:13])
  
  return(names[index],freqs[index])

(name,percent)=gcontent2("./fasta.txt")
print(name)
print(percent)


def gcontent(filepath):
  fasta = open(filepath,'r')
  fasta = fasta.readlines()

  sizes=[]
  a=0
  max=0
  highest=0
  names=[]
  gl = 0
  cl = 0
  length = 0
  l=[]
  size = 0

  for line in fasta:
      l.append(list(line))

  for i in l:
    if i[0] != ">":
      i = np.array(i)
      gl= gl+ len(list(np.where(i=='G'))[0])
      cl= cl+ len(list(np.where(i=='C'))[0])
      length = length + (len(i)-1)

    if i[0] == ">":
      if a!=0:
        size = (gl+cl)/length
        sizes.append(size)
        gl = 0
        cl = 0
        length = 0

        i = list(i)
        i.pop()
        i.remove('>')
        i = ''.join(i)
        names.append(i)

        if size>max:
          max = size
          highest = a 
        a = a+1
      elif a==0:
        i = list(i)
        i.pop()
        i.remove('>')
        i = ''.join(i)
        names.append(i)
        a= a+1

  size = (gl+cl)/length
  sizes.append(size)

  if size>max:
    max = size
    highest =a 
  return(names[highest-1],sizes[highest-1])

(name,content)=gcontent("./fasta.txt")
print(name)
print(content*100)

gcontent2("./fasta.txt")





      


