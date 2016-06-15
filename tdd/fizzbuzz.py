def fizz_buzz(number):
	"""return fizz when divisible by 3
	return buzz when divisible by 5 
	return fizzbuzz when divisible by 15
	"""

	if number % 15 == 0:
		return 'fizzbuzz'

	elif number % 5 == 0:
		return 'buzz'

	elif number % 3 == 0:
		return 'fizz'
		