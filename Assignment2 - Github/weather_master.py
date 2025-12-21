"""
File: weather_master.py
Name: Stephanie
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -1


def main():
	"""
	Find the Highest, Lowest, Average Temperature and the numbers of the days with temperature below 16.
	"""
	pass
	print("SC001\ Weather Master 4.0")
	data = int(input('Next Temperature : (or -1 to quit) ?'))
	if data == EXIT:
		print('No Temperature were entered.')
	else:
		maximum = data
		minimum = data
		a = 1
		sum = data
		average = sum/a
		if data < 16:
			n = 1
		else:
			n = 0
		while True:
			data = int(input('Next Temperature : (or -1 to quit)?'))
			if data == EXIT:
				break
			# if data != EXIT:
			a = a+1
			sum = sum + data
			average = sum/a
			if data < 16:
				n = n+1
			if data >= maximum:
				maximum = data
			# else:
			if data < minimum:
				minimum = data

		print('the Highest Temperature is:'+str(maximum))
		print('the Lowest Temperature is:'+str(minimum))
		print('the Average Temperature is:'+str(average))
		print('the Cold Days:'+str(n))









# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
