"""
File: hailstone.py
Name: Stephanie
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    implement a console program that simulates the execution of the Hailstone sequence
    """
    pass
    print('This program computes the hailstone sequences')
    print('')
    n = int(input('Your choose:'))
    step = 0
    while n != 1:
        if n % 2 == 1:
            print(str(n)+' is odd, so I do 3n+1:'+str(3*n+1))
            n = 3*n+1
            step += 1
        # if n % 2 == 1:
        #    n = 3*n+1
        #    old_n = (n-1)//3
        #    print(str(old_n)+is odd, so I do 3n+1:'+str(n))
        else:
            n //= 2
            old_n = n*2
            print(str(old_n)+' is even, so I take half:'+str(n))
            step += 1
    print('It took '+str(step)+' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
