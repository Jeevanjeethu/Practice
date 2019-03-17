#global variables

# a=10

# def sum():

# 	a=15
# 	print('inside',a)
# 	globals() ['a']=25
# sum()
# print('outside',a)

# recusrsion

# import sys
# sys.recursionlimit(100)
# print(sys.getrecursionlimit())

# def g():
# 	print('a')
# 	g()

# g()

#factorial using recursion

# def f(x):
# 	if x==1:
# 		return 1
# 	else:
# 		return(x*f(x-1))
# print(f(5))

#lambda

# x=lambda a,b:a+b


# print(x(2,3))


#filters if u want to apply any function on certain list

# def add(a):
# 	return a+1


# l=1,2,3,4
# s=list(filter(add,l))
# print(s)


# l=range(0,5)
# s=list(filter(lambda n:n*n,l))
# print(s)


# def s(x):
# 	if x%2==0:
# 		return x

# l=range(0,10)
# n=list(filter(s,l))
# print(n)


# l=range(0,10)

# # n=list(map(lambda n:n+3,l))
# # print(n)

# n=reduce(lambda a,b:a+b,l)
# print(n)

# import total4

# a=5
# b=8

# s=total4.add(a,b)
# print(s)

# from total4 import sub

# print(sub(4,2))

# print('hi')

def add():
	print('hi')


def sub():
	
	print('hello')

def main():
	add()
	sub()





















