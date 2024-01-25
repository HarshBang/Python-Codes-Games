x=int(input("Enter any num"))
fact=1
if(x==0):
	fact=1
else:
	for i in range(1,x+1):
		fact=fact*i
print(fact)
