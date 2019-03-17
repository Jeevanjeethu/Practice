# # # # Add two no's usinf input 
# # # # x=int(input('x'))
# # # # y=int(input('y'))
# # # # z=x+y
# # # # print('sum of {} and {} is {}'.format(x,y,z) )

# # # #concatination of strings
# # # str1 = 'hello'
# # # str2 = 3
# # # c=str1*str2
# # # print(c)

# # # greatest of two no's

# # # x=int(input('x'))
# # # y=int(input('y'))

# # # if x>y:
# # # 	print('{} is greater than {}'.format(x,y))
# # # elif x==y:
# # # 	print('{} is equal to {}'.format(x,y))
# # # else:
# # # 	print('{} is less than {}'.format(x,y))

# # #even or odd

# # x=int(input('x'))
# # if x%2==0:
# # 	print(' {} is even'.format(x))
# # else:
# # 	print(' {} id odd'.format(x))

# #for loop using list

# l=['hi','hello']
# for i in l:
# 	print(i)
# for j in range(0,10):
# 	print(i)

# even no's using range

# for i in range(10,21):
# 	if i%2==0:
# 		print(i)

# length function

# l=['hi','hello', 1,2,4]
# print(len(l))

# prime or not

# x=int(input('x'))
# for i in range(2,x):
# 	if x%i==0:
# 		print('not')
# 		break
# else:
# 	print('prime')

# prime no btw range

# x=int(input('start'))
# y=int(input('end'))
# p=[]
# np=[]
# for i in range(x,y+1):
# 	for j in range(2,i):
# 		if i%j==0:
# 			np.append(i)
# 			break
# 		else:
# 			p.append(i)
# 			break
# print('prime no',p)
# print('not prime no',np)

#leap year
# x=int(input('year'))
# if x%400==0:
# 	print('leap year')
# elif x%100==0:
# 	print('not')
# elif x%4==0:
# 	print('leap')
# else:
# 	print('not')

# l=['c','c++','java','turbo']
# for i in l:
# 	print(len(i),i)

#while loop

# i=0
# while i<=10:
# 	print(i)
# 	i+=1

# random

# import random
# r=random.randint(1,11)
# print(r)
# x=int(input('enter a no btw 1 to 10'))

# while x!=r:
# 	print('wrong gues')
# 	x=int(input('enter a no'))
# else:
# 	print('correct')

# import random
# x=['hi','hello','me']
# r=random.choice(x)
# print(r)


# deep copy and shallow copy
# import copy
# x=[1,2,3,4]

# # y=x
# # print('x',id(x))
# # print('y',id(y))

# y= x.copy()
# print('x',id(x))
# print('y',id(y))

# even odd usind append

# d=[1,2,3,4,5,6,7,8,9,10]
# e=[]
# o=[]
# for i in d:
# 	if i%2==0:
# 		e.append(i)
# 	else:
# 		o.append(i)

# print(o)
# print(e)
# print(d.sort())
# print(d[:2])
# print(d[3:])
# print(d[:])
# print(d.pop())
# print(d)


# n=['hi','hello','me']
# print(n.reverse())

#operation on list

# l=[1,2,3,4,5,6]

# l[0]=2
# print(l)
# l[1:3]
# print(l)

# def add(x,y):
# 	print(x+y)

# def add(x,y):
# 	print(x+y)
# print(add.__doc__)

# def x(a,b='name'):
# 	print( '{} is his {}'.format(a,b))

# x('jeevan')
# x('raj')


def m(x,y):
	return x*y
	

















































































































