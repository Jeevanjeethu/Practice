# # # # # # a=[1,2,3,4,5,6]
# # # # # # b=[4,5,6,7,8,9,10]
# # # # # # c=[]
# # # # # # for i in a:
# # # # # # 	if i in b:
# # # # # # 		c.append(i)
# # # # # # 	else:
# # # # # # 		c.append(i)
# # # # # # for j in b:
# # # # # # 	if j not in a:
# # # # # # 		c.append(j)

# # # # # # print(c)

# # # # # # max value

# # # # # # x=[1,2,3,6,11,9,4,7,10]
# # # # # # m=0
# # # # # # for i in x:
# # # # # # 	if i>m:
# # # # # # 		m=i
# # # # # # print(m)

# # # # # # x='python'
# # # # # # y=''

# # # # # # for i in x:
# # # # # # 	y=i+y
# # # # # # print(y)

# # # # # # pallindrome

# # # # # # x=input('enter an name')
# # # # # # y=''
# # # # # # for i in x:
# # # # # # 	y=i+y
# # # # # # if x==y:
# # # # # # 	print(yes)
# # # # # # else:
# # # # # # 	print(no)

# # # # # # # Dictionary

# # # # # # a={'a':'apple','b':'ball','c':'cat'}
# # # # # # print(a['a'])

# # # # # # a['b']='bat'
# # # # # # print(a)

# # # # # # for k,v in a.items():
# # # # # # 	print(k,v)

# # # # # # sets

# # # # # a={1,2,3,4,5,6,7}
# # # # # b={5,6,7,8,9,10}

# # # # # # print(a|b)
# # # # # # print(a.intersection(b))
# # # # # # print(a-b)
# # # # # # print(b-a)
# # # # # # print(a^b)
# # # # # # a.add(99)
# # # # # # print(a)
# # # # # # a.discard(4)
# # # # # # print(a)
# # # # # # a.update([1,2,3])
# # # # # # print(a)
# # # # # print(a.isdisjoint(b))

# # # # #defining functions

# # # # # def add(x,y):
# # # # # 	print(x+y)

# # # # # add(10,20)

# # # # def add(a,*b):
# # # # 	for i in b:
# # # # 		sum=a
# # # # 		sum=sum+i
# # # # 		print(sum)
		

# # # # add(1,2,3,4,5)

# # # #importing

# # # doc string - import filename
# # # 			 print(filename.__doc__)

# # # normal - import filename
# # # 		 print(filename.functin())


# # # import total
# # # print(total.add(1,2))

# # # import total
# # # add(1,2)
# # # print(total.__doc__)

# # # import total
# # # x=int(input('x'))
# # # y=int(input('y'))
# # # print(total.add(x,y))

# # #number system

# # # print(bin(10))
# # # print(oct(10))
# # # print(hex(10))

# # # #compliment biwise and bitweise or bitwise xor left shift and right shift operators
# # # print(~12)
# # # print(12&13)
# # # print(12|13)
# # # print(12^13)
# # # print(10<<2)
# # # print(10>>2)


# # # def x(a,b='name'):
# # # 	print( '{} is his {}'.format(a,b))

# # # # x('jeevan')
# # # # x('raj')


# # # # import total
# # # # x='jeevan'
# # # # print(total.x(x))

# # # import total

# # # x=int(input('x'))
# # # y=int(input('y'))
# # # print(total.m(x,y))


# # # a=10

# # # def x():
	
# # # 	a=9
# # # 	print(a)
# # # 	globals() ['a']=15


# # # x()

# # # print('outside',a)

# # # print(a+1)


# # # a=9

# # # def x():

# # # 	a=15
# # # 	print('local',a)
# # # 	globals()['a']=20
# # # x()
# # # print('global',a)

# # # factorial using recursion

# # # def fact(x):
# # # 	if x==1:
# # # 		return 1
# # # 	else:
# # # 		return(x*fact(x-1))

# # # print(fact(5))


# # # def sum(x):
# # # 	if x==1:
# # # 		return 1
# # # 	else:
# # # 		return(x+sum(x-1))
# # # print(sum(int(input(x))))


# # # f=lambda a:a*a

# # # print(f(5))

# # a= lambda x,y:x+y

# # print(a(1,2))



# # b=lambda x,y:x-y


# # print(b(2,1))

# #filter function

# # def even(n):
# # 	return n%2==0

# # l=[1,2,3,4,5,6,7]
# # even=list(filter(even,l))
# # print(even)


# # def n(x):
# # 	return x%5==0

# # l=range(0,50)
# # x=list(filter(n,l))
# # print(x)


# # def p(x):
# # 	for i in range(2,x):
# # 		if x%i!=0:
# # 			return x

# # l=range(0,50)
# # p=list(filter(p,l))
# # print(p)


# # def e(x):
# # 	return x%2==0


# # l=range(0,10)
# # f=list(filter(lambda l: l%2==0,l))
# # print(f)

# sum= lambda a,b: a+b

# s=sum(2,3)
# print(s)


# l=range(0,30)
# s=list(filter(lambda n:n%3==0,l))
# print(s)


# x=lambda n:n*2

# def s(n):
# 	return n%4==0

# l=range(0,20)
# f=list(filter(s,l))
# print(f)

l=range(0,10)
n=map(lambda n:n*2,l)
print(n)

s=reduce(lambda a,b:a+b,l)
print(s)

j=filter(lambda n:n%2==0,l)
print(j)



































































