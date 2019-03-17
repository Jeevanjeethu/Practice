# # # # # # # # # # # # # import sys
# # # # # # # # # # # # # x=int(sys.argv[1])
# # # # # # # # # # # # # y=int(sys.argv[2])
# # # # # # # # # # # # # z=x+y
# # # # # # # # # # # # # print(z)

# # # # # # # # # # # # i=0
# # # # # # # # # # # # while i<=5:
# # # # # # # # # # # # 	print('hello',i)
# # # # # # # # # # # # 	i=i+1

# # # # # # # # # # # i=1
# # # # # # # # # # # while i<=5:
# # # # # # # # # # # 	print("hello ",end="")
# # # # # # # # # # # 	j=1
# # # # # # # # # # # 	while j<=2:
# # # # # # # # # # # 		print('jeevan')
# # # # # # # # # # # 		j=j+1
# # # # # # # # # # # 	i=i+1
# # # # # # # # # # # 	print()

# # # # # # # # # # for i in range(1,100):
# # # # # # # # # # 	if i%3==0:
# # # # # # # # # # 		continue
# # # # # # # # # # 	print(i)

# # # # # # # # # import array
# # # # # # # # # v= array('i',[5,6,7,8])
# # # # # # # # # # print(v.buffer_info())
# # # # # # # # # print(v[0])

# # # # # # # # def g():
# # # # # # # # 	print('hello')
# # # # # # # # 	print('good morning')

# # # # # # # # g()

# # # # # # # def add(x,y):
# # # # # # # 	print(x+y)

# # # # # # # add(5,3)

# # # # # # def add(x,y):
# # # # # # 	return x+y

# # # # # # print(add(5,8))

# # # # # def stm(x,y):
# # # # # 	print('hi {} your roll no is {} '.format(x,y))

# # # # # a = input('enter name')
# # # # # b= input(' roll no')
# # # # # stm(a,b)

# # # # def add_sub(x,y):
# # # # 	return x+y,x-y

# # # # print(add_sub(3,2))

# # # x='python'

# # # c=[]
# # # for i in x:
# # # 	c.insert(0,i)
# # # print(c)

# # def update(x):
# # 	print(id(x))
# # 	x=5
# # 	print(id(x))
# # 	print(x)

# # a=10
# # print(id(a))
# # update(a)
# # print(id(a))


# # # # def update(list):
# # # 	list[0]=4
# # # 	print(list)
# # # l=[1,2,3,4]
# # # update(l)


# # def p(n,a):
# # 	print(n)
# # 	print(a-5)	

# # p(a=27,n='j')

# # def add(a,*b):
# # 	c=a
# # 	for i in b:
# # 		c=i+c
# # 	print(c)
# # add(1,2,3,4)

# def add(a,*b):
	
# 	for i in b:
# 		a=i+a
# 	print(a)
# add(1,2,3,4)

def add(*b):
	c=0
	for i in b:
		c=i+c
	print(c)
add(1,2,3,4)






