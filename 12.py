import math

def divisor_counter(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            number_of_factors +=2
        else:
            continue
    return number_of_factors

i=1
triangle_numbers=[1]
condition=False
while condition==False:
	i+=1

	triangle_numbers.append(triangle_numbers[-1]+i)
	divs=divisor_counter(triangle_numbers[-1])

	if divs>=500:
		print triangle_numbers[-1]
		condition=True

