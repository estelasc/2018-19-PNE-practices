# Since I have created more function than required in both exercises 1 and 2 in order
# to make my program more ordered and easier, I will copy here those functions as well.
from Bases import count_bases


def percentage(bas):
    """Calculating the percentage of the basis in a sequence."""

    if tot_len > 0:
        perc = round(100.0 * n_bases[bas] / tot_len, 1)
    else:
        perc = 0

    return perc


def print_info(basis):
    """Printing all the information"""

    print("Base {}".format(basis))
    print("Counter: {}".format(n_bases[basis]))
    print("Percentage: {}".format(percentage(basis)))

    return


# Main program
s1 = input("Enter the sequence 1: ")
s1 = s1.upper()
s2 = input("Enter the sequence 2: ")
s2 = s2.upper()
my_list = [s1, s2]

# Calculate the total sequence length
for i, sequ in enumerate(my_list):
    tot_len = len(sequ)
    print("Sequence", i+1, "is {} bases in length".format(tot_len))
    n_bases = count_bases(sequ)
    print_info('A')
    print_info('T')
    print_info('C')
    print_info('G')
    print()
