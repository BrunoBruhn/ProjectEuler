import pandas as pd

def alphabetical_sum(string):
	dictionary = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
	
	sum_=0
	
	nm=str(string)
	
	for letter in range(len(nm)):

		correct_letter=nm[letter].lower()
		sum_+=dictionary['{}'.format(correct_letter)]
		
	return sum_

T_data = pd.read_csv('p22_names.txt', sep=",", header=None)

data=T_data.T

df=data.rename(columns={0: 'Names'})
df=df.sort_values('Names')

length=df.shape[0]

alphabetical_values=[]

for i in range(length):		

		name=df.iloc[i][0]
		alphabetical_values.append((i+1)*alphabetical_sum(name))
		
		print(i,alphabetical_values[-1],name)

df['AV']=alphabetical_values

print(sum(alphabetical_values))