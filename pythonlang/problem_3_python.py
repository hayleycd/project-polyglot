# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import multiples_and_primes as mp 

def find_largest_prime_factor(my_number):
	
	factors = mp.return_factors(my_number)
	factors.sort()
	factors.reverse()

	for each in factors:
		if mp.is_prime(each):
			return each
		



