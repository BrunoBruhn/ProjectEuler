def largest_prime_factor(x):

	i=2
	prime_factors=[]

	while x != 1:
		if x % i == 0:
			prime_factors.append(i)
			x=x/i
			i=2
		else:
			i+=1


	print max(prime_factors)

largest_prime_factor(600851475143)