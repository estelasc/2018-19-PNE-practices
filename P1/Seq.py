class Seq:
    """A class for analyzing DNA sequences"""
    def __init__(self, strbase):

        self.strbase = strbase

    def len(self):
        return len(self.strbase)

    def complement(self):
        bas_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        comp_chain = ""
        for basis in self.strbase:
            if basis == 'A':
                comp_chain += bas_dict['A']
            elif basis == 'T':
                comp_chain += bas_dict['T']
            elif basis == 'C':
                comp_chain += bas_dict['C']
            elif basis == 'G':
                comp_chain += bas_dict['G']
        return comp_chain

    def reverse(self):
        rev_chain = self.strbase[::-1]
        return rev_chain

    def count(self, base):
        counter = self.strbase.count(base)
        return counter

    def perc(self, base):
        tot_len = len(self.strbase)
        if tot_len > 0:
            perc = round(100.0 * self.strbase.count(base) / tot_len, 1)
        else:
            perc = 0
        return perc
