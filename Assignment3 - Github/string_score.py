"""
File: string_score.py
Name: Stephanie
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    TODO: To calculate number according to the different data type and print the sum
    """
    pass
    string = input('?')
    result = score(string)
    print(result)

    score('1aB4rC')    # digit->1 ; upper->2; lower->3
    # 12
    score('aaaaA3')
    # 15


def score(string):
    ans = 0
    ch = [string]
    for ch in string:
        if ch.isupper():
            ans += 2
        if ch.islower():
            ans += 3
        elif ch.isdigit():
            ans += 1
    return ans


if __name__ == '__main__':
    main()