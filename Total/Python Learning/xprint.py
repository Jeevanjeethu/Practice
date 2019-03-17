i=int(input('enter ua no'))
import random
x=random.randint(1,10)
print(x)
while x!=i:
	print('wrong guess')
	i=int(input('enter no'))
else:
	print('Guessed the no correctly')