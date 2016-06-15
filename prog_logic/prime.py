def primenos(n):
	primelist=[2,3]
	starter = 4
	while True:
		for i in range(2,(starter//2)+1):
			if starter % i == 0:
				break
		else:		
			primelist.append(starter)
		starter+=1
		if len(primelist) == n:
			break
	return primelist
print(primenos(10))
