x=int(input("enter value of x"))
for i in range(2,x):
	if x%i==0:
		print('x is not a prime no')
		break
else:
	print('x is prime')

Print from 300 to 700 all prime no's

count=0
x=int(input('enter your start value'))
y=int(input('enter your end value'))
for i in range(x,y):
	for j in range(2,i):
		if i%j==0:
			break
	else:
		print('the given {} is prime'.format(i))
		count=count+1
print('the count of preime no is',count)
