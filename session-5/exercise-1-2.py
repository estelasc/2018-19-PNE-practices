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
s = input("Enter the sequence: ")
s = s.upper()

# Calculate the total sequence length
tot_len = len(s)
print("This sequence is {} bases in length.".format(tot_len))

# Bases information
n_bases = count_bases(s)

# Printing the information calling the appropriate function
print_info('A')
print_info('T')
print_info('C')
print_info('G')
