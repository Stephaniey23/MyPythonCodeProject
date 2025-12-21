"""
File: file_reading.py
—————————————————————————————————
This program reads in a file ”data.txt” and processes each line.
The program will go through all the digits that are existed in the file
and printed the maximum, minimum as well as the average of digits on Console.
"""

FILE = 'data.txt'
FILE1 = 'data_1.txt'


def main():
    pass
    minimum = 100
    maximum = 0
    count = 0
    total = 0
    f = open(FILE, 'r')
    # 可視需求在上述code中導入FILE或FILE1
    for line in f:
        if line != 'Nan\n':
            data = float(line)
            if data > maximum:
                maximum = data
            if data < minimum:
                minimum = data
            count = count + 1
            total = total + data
            avg = total/count
        elif line == 'Nan\n':
            nan = 0
            count = count + nan
            total = total + nan
    f.close()
    if count == 0:
        print('No data in this file')
    else:
        print('Max:'+str(maximum))
        print('Min:'+str(minimum))
        print('Avg:'+str(avg))





if __name__ == '__main__':
    main()
