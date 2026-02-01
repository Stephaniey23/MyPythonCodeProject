"""
File: class_reviews.py
Name: Stephanie
-------------------------------
At the beginning of the program, the user is asked to enter
a class name, either SC001 or SC101. The input should be
case-insensitive.

If the user enters "-1" as the class name, the program will
calculate and display the maximum, minimum, and average
values among all the collected inputs.
"""

SECRET = -1
count1 = 0
count2 = 0
total1 = 0
total2 = 0
maximum1 = 0
minimum1 = 0
maximum2 = 0
minimum2 = 0
score_entered = False


def main():
    """
    To deal with the score data of class: SC001 & SC101, and print the MAX, MIN, AVG of each class
    """
    global count1, count2, total1, total2, maximum1, minimum1, maximum2, minimum2, score_entered
    while True:
        class_type = input('?')
        class_type = class_type.upper()
        print('Which Class ?'+class_type)

        if class_type == str(SECRET):
            break
        # print('No class scores were entered')

        else:
            score = int(input('Score: '))
            score_entered = True
            if count1 + count2 == 0:
                maximum1 = score
                minimum1 = score
                maximum2 = score
                minimum2 = score

            if class_type == 'SC001':
                count1 += 1
                total1 += score
                if score >= maximum1:
                    maximum1 = score
                if score <= minimum1:
                    minimum1 = score
            else:
                count2 += 1
                total2 += score
                if score >= maximum2:
                    maximum2 = score
                if score <= minimum2:
                    minimum2 = score

    if not score_entered:
        print('No class scores were entered')
    else:
        print('=====================SC001=======================')
        if count1 == 0:
            print('No score for SC001')
        else:
            avg1 = total1/count1
            print('MAX= ' + str(maximum1))
            print('MIN= ' + str(minimum1))
            print('AVG= ' + str(avg1))
            print('Count= ' + str(count1))

        print('=====================SC101=======================')
        if count2 == 0:
            print('No score for SC101')
        else:
            avg2 = total2/count2
            print('MAX= ' + str(maximum2))
            print('MIN= ' + str(minimum2))
            print('AVG= ' + str(avg2))
            print('Count= ' + str(count2))

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
