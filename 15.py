
def routes_counter(grid_width):
	frac1=factorial(grid_width*2)
	frac2=factorial(grid_width)
	routes_total=frac1/(frac2*frac2)
	print routes_total

def factorial(n):    
	
	a = 1
	  
	for i in range(1,n+1): 
	    a = a * i 
	return a

routes_counter(20)