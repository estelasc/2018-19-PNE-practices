f = open("dna.txt", "r")
sequence = f.read()
f.close()
sequence = sequence.replace(" ", "").replace("\n", "")

num_basis = len(sequence)

A = sequence.count("A")
C = sequence.count("C")
T = sequence.count("T")
G = sequence.count("G")

print("The total number of bases is: {}".format(num_basis))
print("The number of Adenine bases is: {}".format(A))
print("The number of Cytosine bases is: {}".format(C))
print("The number of Thymine bases is: {}".format(T))
print("The number of Guanine bases is: {}".format((G)))



