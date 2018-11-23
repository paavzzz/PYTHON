#This function serve to analyze the GC content of various DNA strands in a specified format. High GC content indicates high
#mutation rate, but also indicates stronger and more stable DNA as 3 H bonds can be formed instead of just 2.
#In bacteria, GC rich content indicates elevated levels of heat-resistance! However, in terms of PCR high GC content indicates less
#successful denaturation of DNA because of the higher melting point. :(

#Return:  name of most GC rich sequence
#         percent of GC content


#This is the format of the input file:
# >FASTAseq_2974
# GGTTTGGGCCTCGGTAAATTGAAGCCGTATCTCCAAAACGATTGGGACTATGAGGGACAC
# >FASTAseq_9629
# CTAAAATGATGAGTTCCCCCATACGGACCGGTAGCCACGCAGCCCCACTCCAGATGAGTC
# >FASTAseq_5115
# GCAGAGCCACGTGCTTGCGAATCTTAGTAGATAAAGGGGGGTGTCGTTGAGGCATGGTCG
# >FASTAseq_6828
# TTAGACCTTTCCGACCAAGTACTGCGAGGCCGAACGGAAGGTACCCATCCCGATAAGAAC
# >FASTAseq_0757
# ATAACTAGATTGCATGTAAGTCGCCTGAATGTGGTGCCTACGATTCAACCGTGAAGTCCG


def gcontent(filepath):
  fasta = open(filepath,'r')
  fasta = fasta.readlines()
  names=[]
  freqs=[]
  for line in fasta:
    if line[0] == ">":
      names.append(line)
    else:
      freqs.append((line.count('C')+line.count('G'))/len(line)*100)
  
  return(names[freqs.index(max(freqs))],max(freqs))
  
(name, percentage) = gcontent('./fasta.txt')
print(name[1:len(name)])
print(percentage)

