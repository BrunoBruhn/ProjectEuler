def sum_of_fractorial_digits(x):
	def fractorial(n):

		fact = 1
		  
		for i in range(1,n+1): 
		    fact = fact * i 
		return fact

	fact=str(fractorial(x))
	sum_of_digits=0
	for i in range(len(fact)):
		sum_of_digits+=int(fact[i])

	print(sum_of_digits)

sum_of_fractorial_digits(100)

import divisor_gen

print(divisor_gen.GO(220))