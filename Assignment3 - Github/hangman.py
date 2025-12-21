"""
File: hangman.py
Name: Stephanie
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    TODO: Character Guessing
    """
    pass
    intro()
    ans = random_word()
    dash = hiding(ans)
    print(dash)
    guess(ans, dash, N_TURNS)


def guess(ans, dash, lives):
    while lives != 0:
        input_ch = input('Your guess?').upper()
        i = ans.find(input_ch)
        if i != -1:
            result = ""
            for j in range(len(ans)):
                ch = ans[j]
                if ch == input_ch:
                    result += ch
                else:
                    result += dash[j]
            dash = result
            if dash != ans:
                print('You are correct! The word looks like : '+str(dash))
                print('You have '+str(lives)+' wrong guesses left !')
            else:
                print('You Win !')
                print('The answer is ' + str(ans) + '!')
                break
        else:
            lives -= 1
            print('There is no '+str(input_ch)+'\'s in the word')
            if lives != 0:
                print('The word looks like : ' + str(dash))
                print('You have '+str(lives)+' wrong guesses left.')
            else:
                print('You are completely hung :(')
                print('The answer is '+str(ans)+'!')


def intro():
    print('The word looks like : _______')
    print('You have 7 wrong guesses left.')


def hiding(ans):
    dash = ''
    for i in range(len(ans)):
        dash = dash + '-'
    return dash


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
