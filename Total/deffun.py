# def oddeven(*a):
# 	e=[]
# 	o=[]
# 	counte=0
# 	counto=0
# 	for i in a:
# 		if i%2==0:
# 			e.append(i)
# 			counte+=1
# 		else:
# 			o.append(i)
# 			counto+=1
# 	print(e)
# 	print(o)
# 	return counte,counto

# x,y = oddeven(1,2,3,4,5,6,7,8)

# # oddeven(1,2,3,4,5,6,7,8)
# print(x,y)

# factorial

# def fact(x):
# 	f=1
# 	for i in range(1,x+1):
# 		f=f*i
# 	print(f)
# x=int(input('x'))
# fact(x)


# import sys
# sys.setrecursionlimit(100)
# print(sys.getrecusrionlimit())

# def g():
# 	print('hello')
# 	g()

# g()

import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
print(x+y)