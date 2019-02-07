def count_bases(seq):
    """Counting the number of As, Ts, Cs and Gs in the sequence."""

    # Counter for the As, Ts, Cs and Gs
    result_a = 0
    result_t = 0
    result_c = 0
    result_g = 0

    for b in seq:
        if b == 'A':
            result_a += 1
        elif b == 'T':
            result_t += 1
        elif b == 'C':
            result_c += 1
        elif b == 'G':
            result_g += 1

    my_dict = {'A': result_a, 'T': result_t, 'C': result_c, 'G': result_g}

    # Return the result
    return my_dict


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
