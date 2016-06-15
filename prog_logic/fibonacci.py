def fibonacci(n):
	if n < 1:
		print('Nothing to print')
		return None #prevent code after else block from being executed
	elif n == 1:
		fibo_list = [0]
	else:
		fibo_list = [0,1]
	counter = 1
	while True:
		if len(fibo_list) == n:
			break
		fibo_list.append(fibo_list[counter - 1] + fibo_list[counter])
		counter += 1
	print(fibo_list)
fibonacci (10)
fibonacci(2)
fibonacci(1)
fibonacci(0)
fibonacci(-2)