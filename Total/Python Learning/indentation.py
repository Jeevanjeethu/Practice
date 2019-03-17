x=int(input("enter value of x"))
y=int(input("enter value of y"))
if x>y:
	print('{} is greater than {}'.format(x,y))
	print('end of if')
elif x==y:
	print('{} is equals to {}'.format(x,y))
else:
	print('{} is greatet than {}'.format(y,x))
	print('end of else')
