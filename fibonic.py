print "Fibonacci Series"
a = -1
b = 1
sum = 0
i=0
while(i<10):
	sum = a + b
	print sum
	a, b = b, sum
	i+=1

