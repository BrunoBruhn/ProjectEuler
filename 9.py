def pythagorean_triplet_product(x):
	done=False
	a=0
	while done==False:
		a+=1

		if a!=x:
			b=((a**2-(x-a)**2))/(-2*(x-a))
			c=(a**2+b**2)**0.5


			if c%1==0 and b%1==0:

				print int(a*b*c)
				done=True

pythagorean_triplet_product(1000)







