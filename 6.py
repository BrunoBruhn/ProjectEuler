def difference(n):
	squares=[]
	straigts=[]
	for i in range(n+1):
		squares.append(i**2)
		straigts.append(i)

	sum_of_squares=sum(squares)
	sum_of_straigts=sum(straigts)**2

	print sum_of_straigts-sum_of_squares

difference(100)