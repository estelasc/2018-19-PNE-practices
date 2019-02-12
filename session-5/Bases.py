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

