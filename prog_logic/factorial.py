def factorial(x):
	if type(x) != type(1):
		return 'invalid input'

	if x > 998:
		return 'input is too large!'

	if x < 0:
		return 'invalid input'
	if x == 1 or x == 0:
		return 1
	return x * factorial(x-1)