import calendar

counter=0
for y in range(1,11):
	
	year=1990+y

	for m in range(1,13):
		
		localtime = calendar.weekday(year,m,1)

		if localtime==6:
			counter+=1

print counter
