# 2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

def optimize_list(upper_limit):
	my_list = [each for each in range(1, upper_limit + 1)]
	optimize_list = []

	for index in range(len(my_list)):
		redundant = False
		for next in range(index + 1, len(my_list)):
			if my_list[next] % my_list[index] == 0:
				redundant = True
				break
		if redundant == False:
			optimize_list.append(my_list[index])
	return optimize_list
		
def smallest_positive_divisible(opt_list):

	divisible = False
	start = opt_list[-1]

	while not divisible:
		factors = []
		start = start + 2

		for each in opt_list:
			if start % each == 0:
				factors.append(each)
				divisible = True if len(opt_list) == len(factors) else False
			else:
				break
	
	return start

print(smallest_positive_divisible(optimize_list(20)))