# # # def add(x,y=10):
# # # 	print(x+y)

# # # add(10)

# # #arbitary argument/keyword arguments

# # def g(*names):
# # 	for i in names:
# # 		print('hello', i ,"good morning")
# # g('a','b','c')


# #recursion

# def greet():
# 	print('good mo') 
# 	greet()
# greet()

#factorial using recursion

# def fact(x):
# 	c=1
# 	f=range(1,x+1)
# 	for i in f:
# 		c=c*i
# 	print(c)
# fact(5)

# def fact(x):
# 	if x==1:
# 		return 1
# 	else:
# 		return(x*fact(x-1))
# x=int(input('enter a no'))
# print('the fact id',x,'is',fact(x))


def sum(x):
	if x==1:
		return 1
	else:
		return(x+sum(x-1))
x=int(input('enter a no'))
print('the sum',sum(x))
