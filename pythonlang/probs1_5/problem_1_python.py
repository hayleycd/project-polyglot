# Multiples of 3 and 5
# Problem 1

# If we list all the natural numbers below 10 that are 
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these 
# multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

import multiples_and_primes as multp

def find_multiple_sum(limit_num, multiple):
	multiple_sum = 0
	current_number = multiple
	while current_number < limit_num:
		multiple_sum += current_number
		current_number += multiple
	return multiple_sum


multiple_of_5_sum = find_multiple_sum(1000, 5)
multiple_of_3_sum = find_multiple_sum(1000, 3)
multiple_of_3_and_5 = find_multiple_sum(1000, 15)

print(multiple_of_5_sum + multiple_of_3_sum - multiple_of_3_and_5)
