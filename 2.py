def sum_of_even_valued(x):
	fibonacci=[1,2]
	fibonacci_even=[2]
	while fibonacci[-1]<=x:
		fibonacci.append(fibonacci[-1]+fibonacci[-2])

		if fibonacci[-1]%2==0:
			fibonacci_even.append(fibonacci[-1])
			
	print sum(fibonacci_even)

sum_of_even_valued(4*10**6)