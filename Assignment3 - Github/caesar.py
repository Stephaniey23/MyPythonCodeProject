"""
File: caesar.py
Name: Stephanie
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TO decipher the ciphered string with secret code.
    """
    pass
    secret_num = 7
    print('Secret Number:'+str(secret_num))
    ciphered_str = input('What is the ciphered string?').upper()
    old_str = ALPHABET
    new_str = define(secret_num, old_str)
    # print(new_str)
    result = deciphered(new_str, ciphered_str)
    print('The deciphered string is:'+result)


def define(secret_num, old_str):
    old_str = ALPHABET
    ans = ''
    for i in range(len(old_str)-secret_num, len(old_str)):
        ch = old_str[i]
        ans = ans+ch
    for i in range(0, len(old_str)-secret_num):
        ch = old_str[i]
        ans = ans+ch
    return ans


def deciphered(new_str, ciphered_str):
    s = ciphered_str
    old_str = ALPHABET
    result = ''
    for ch in s:
        i = new_str.find(ch)
        if i != -1:
            result += old_str[i]
        else:
            result = result + ch
    return result







# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
