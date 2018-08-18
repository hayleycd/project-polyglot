# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def is_factor(my_number, factor):
	if my_number % factor == 0:
		return True
	else:
		return False

def return_factors(my_number):
	factors = [1]
	limit_check = my_number
	number_to_check = 2

	while number_to_check < limit_check:
		if is_factor(my_number, number_to_check):
			factors.append(number_to_check)
			limit_check = my_number//number_to_check
			factors.append(limit_check)
		number_to_check += 1

	factors.append(my_number)

	return factors

def is_prime(my_number):

	factors = return_factors(my_number)

	if len(factors) > 2:
		return False
	else:
		return True

def find_largest_prime_factor(my_number):
	
	factors = return_factors(my_number)
	factors.sort()
	factors.reverse()

	for each in factors:
		if is_prime(each):
			return each
		



