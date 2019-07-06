def chainsize(x):
		size=0
		while x!=1:
			size+=1
			if x%2==0:
				x=x/2
			else:
				x=3*x+1
		return size

def longest_sequence(max_range):

	incumbent=0
	i_max=0
	for i in range(1,max_range):

		a=chainsize(i)
		
		if incumbent<a:
			incumbent=a
			i_max=i

	print i_max

	
longest_sequence(10**6)