# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_even_length(number_to_str):
	return True if len(number_to_str) % 2 == 0 else False

def is_number_a_palindrome(possible_palindrome):

	number_to_str = str(possible_palindrome)

	if is_even_length(number_to_str):
		return even_check(number_to_str)

	else:
		return odd_check(number_to_str)

def even_check(number_to_str):
	
	first = number_to_str[:(len(number_to_str)//2)]
	second = number_to_str[(len(number_to_str)//2):]
	second = reverse_string(second)
	return True if first == second else False

def odd_check(number_to_str):
	
	first = number_to_str[:(len(number_to_str)//2)]
	second = number_to_str[(len(number_to_str)//2) + 1:]
	second = reverse_string(second)
	return True if first == second else False

def reverse_string(mystring):
	new_string = ""

	for each_letter in mystring:
		new_string = each_letter + new_string

	return new_string

def get_palindromes(begin_number, end_number):
	palindromes = []

	for possible_palindrome in range(begin_number, end_number):
		if is_number_a_palindrome(possible_palindrome):
			palindromes.append(possible_palindrome)

	return palindromes

def number_is_product_of_two_three_digit_numbers(number_to_check):
	for possible_factor in range(100, 999):
		if number_to_check % possible_factor == 0:
			paired_factor  = number_to_check // possible_factor
			if len(str(paired_factor))  == 3:
				return True

	return False

def get_largest_palindrome():
	palindromes = get_palindromes(10000, 998001)
	palindromes.reverse()

	for possible_factor in palindromes:
		if number_is_product_of_two_three_digit_numbers(possible_factor):
			return possible_factor

	else:
		None

print(get_largest_palindrome())		
