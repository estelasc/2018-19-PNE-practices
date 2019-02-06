sequence = open("CPLX2.txt", "r")
lines = sequence.readlines()
sequence.close()
sequence = open("CPLX2.txt", "w")
totA = 0
totC = 0
totG = 0
totT = 0
tot_bases = 0
for line in lines:
    if line[0] != ">":
        sequence.write(line)
        totA = line.count("A") + totA
        totC = line.count("C") + totC
        totG = line.count("G") + totG
        totT = line.count("T") + totT
        tot_bases = tot_bases + len(line) - 1

sequence.close()


print("The number of Adenine bases is: {}".format(totA))
print("The number of Cytosine bases is: {}".format(totC))
print("The number of Guanine bases is: {}".format(totG))
print("The number of Thymine bases is: {}".format(totT))
print("The total number of bases is: {}".format(tot_bases))