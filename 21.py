import divisor_gen

def sum_of_amicables_below_x(x):
	amicables=[]
	for i in range(x):
		divisor1=sum(divisor_gen.GO(i)[:-1])
		divisor2=sum(divisor_gen.GO(divisor1)[:-1])
		if i==divisor2 and i!=divisor1:
			amicables.append(i)

	print (sum(amicables))

sum_of_amicables_below_x(10000)
