"""
File: coin_flip_runs.py
Name: Stephanie
-----------------------
This program simulates a sequence of coin flips until
the number of runs specified by the user is reached.

A run is defined as consecutive occurrences of the same
result, either 'H' or 'T'. For example, the sequence
'HHHHHTHTT' is considered a 2-run result.

The program stops immediately once the total number of
runs reaches the user-defined value.
"""

import random as r


def main():
	"""
	TODO: To simulate the outcome when flipping a coin based on the different appointed numbers of run
	"""

	print("Let's flip a coin!")
	num_run = int(input("Number of runs: "))

	first_flip = r.choice(['H', 'T'])
	result_str = first_flip

	current_run_count = 0
	last_flip = first_flip

	while current_run_count < num_run:
		new_flip = r.choice(['H', 'T'])
		result_str += new_flip

		if new_flip == last_flip:
			current_run_count += 1
		else:
			# 當投出不同的面時，重新開始計算連續次數
			current_run_count = 0
			last_flip = new_flip

	print(result_str)

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
