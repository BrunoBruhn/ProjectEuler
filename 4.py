import math

def largest_made_from_product(x):
	list_of_all=list_all_palindromes(x)
	list_of_all.sort(reverse=True)

	for i in range(len(list_of_all)):
		value=int(list_of_all[i])
		root=value**.5
		
		a=math.ceil(root)
		b=value/a

		while b%1!=0 and x>=len(str(int(a))):
			a+=1
			b=value/a

		if b%1==0 and a%1==0:
			print int(a),int(b),value
			break

def list_all_palindromes(x):
	palindrome_list=[]
	for i in range(10**(x-1),10**x):
		new_palindrome=str(i)
		for n in range(x):
			i=str(i)

			new_palindrome=new_palindrome+str(i[x-n-1])
		palindrome_list.append(new_palindrome)

	
	return palindrome_list
		
largest_made_from_product(3)