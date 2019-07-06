
def quersumme(power_of):
	
	value=str(2**power_of)

	summe=0
	for i in range(len(value)):
		summe+=int(value[i])

	print summe

quersumme(1000)

