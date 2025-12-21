"""
File: complement.py
Name: Stephanie
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    TODO: To print DNA letters with its alternatives
    """

    print(build_complement('ATC'))
    print(build_complement(""))
    print(build_complement('ATGCAT'))
    print(build_complement('GTACAGT'))


def build_complement(dna):
    dna = dna.upper()
    if dna != '':
        ans = ''
        if dna != '':
            for i in range(len(dna)):
                ch = dna[i]
                if ch == 'A':
                    ans = ans + 'T'
                if ch == 'T':
                    ans = ans + 'A'
                if ch == 'C':
                    ans = ans + 'G'
                if ch == 'G':
                    ans = ans + 'C'
            return ans
    else:
        return 'DNA strand is missing'






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
