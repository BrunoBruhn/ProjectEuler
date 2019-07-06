
def find_answer(p):
	finished=0
	i=2500

	while finished==0:

		i+=20
		n=p/2+1

		while n <= p and i%n==0:
	
			if n==p:
				print i
				finished=1
				break

			n+=1


find_answer(20)








