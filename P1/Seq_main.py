# Main program
from Seq import Seq

se1 = input("Please, enter the first sequence: ")
se1 = se1.upper()  # In order to avoid errors if the user enter the sequence lowercase.
s1 = Seq(se1)
se2 = input("Please, enter the second sequence: ")
se2 = se2.upper()  # In order to avoid errors if the user enter the sequence lowercase.
s2 = Seq(se2)
s3 = s1.complement()
s4 = s3.reverse()


def print_info(num_seq, dna):
    print("Sequence {}:".format(num_seq), dna.strbase)
    print("Length: {}".format(dna.len()))
    print("Bases count:", "A:{},".format(dna.count('A')), "T:{},".format(dna.count('T')),
          "C:{},".format(dna.count('C')), "G:{}".format(dna.count('G')))
    print("Bases percentage:", "A:{}%,".format(dna.perc('A')), "T:{}%,".format(dna.perc('T')),
          "C:{}%,".format(dna.perc('C')), "G:{}%".format(dna.perc('G')))


print_info(1, s1)
print()
print_info(2, s2)
print()
print_info(3, s3)
print()
print_info(4, s4)
