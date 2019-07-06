def sum_of_multiples(x):
	numbers=0
	for i in range(x):
		if i % 3 == 0 or i % 5 == 0:
			numbers+=i
	print numbers

sum_of_multiples(1000)