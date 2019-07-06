import prime_check

def prime_counter(max_count):
	counter=0
	i=1
	while counter<max_count:
		i+=1
		if prime_check.is_Prime(i)==1:
			counter+=1
		
	print i

prime_counter(10001)