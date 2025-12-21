"""
File: prime_checker.py
Name: Stephanie
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	The program will continually ask the user to enter an integer >1 to checks if it is a prime number.
	"""
	pass
	print('Welcome to the prime checker!')
	while True:
		n = int(input('n:'))
		if n == EXIT:
			break
		else:
			start = 2
			while start != n:
				if n % start == 0:
					print('n is not a prime number')
					break
				else:
					start = start + 1
			if start == n:
				print('n is a prime number')
	print('Have a good one !')




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
