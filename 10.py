import prime_check

def sum_of_primes(prime_ceiling):
	sum_=0
	primes=[]
	for i in range(2,prime_ceiling):
		if prime_check.is_Prime(i)==True:
			primes.append(i)
	print sum(primes)

sum_of_primes(2000000)