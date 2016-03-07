def series(n):
	a=-1
	b=1
	for i in range (0, n):
		sum = a + b
		print sum
		a, b = b, sum

