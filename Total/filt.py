# # # # # # # # # a=15

# # # # # # # # # def add():


# # # # # # # # # 	a=10
# # # # # # # # # 	print(a)
# # # # # # # # # 	globals()['a']=19

# # # # # # # # # add()
# # # # # # # # # print(a)

# # # # # # # # x=range(20)
# # # # # # # # y=[i for i in x if i%2==0]
# # # # # # # # print(y)


# # # # # # # x=range(20)
# # # # # # # y=lambda n:n%2==0
# # # # # # # evens=filter(y,x)
# # # # # # # print(evens)

# # # # # # lambda n:n*2

# # # # # # x=['x-man','y-man']

# # # # # # for num,i in enumerate(x,10):
# # # # # # 	print(num,i)

# # # # # #file handling functions

# # # # # f=open("C:\\Users\\Jeevan K\\Desktop\\Python Learning\\file handling\\sample.txt",'r')

# # # # # print(f.read())
# # # # # print(f.readline())
# # # # # print(f.tell())
# # # # # print(f.seek(10))
# # # # # print(f.tell())
# # # # # f.close()

# # # # f.read()
# # # # f.readline()
# # # # f.open()
# # # # f.close()
# # # # f.tell()
# # # # f.seek(10)



# # # x=range(40)
# # # y=lambda n: n*2
# # # z=list(filter(y,x))
# # # print(z)

# # class computer:
# # 	def config(self):
# # 		print('config is dell')

# # com1=computer()
# # com1.config()


# class comp:

# 	def __init__(self,a,b):
# 		self.a=a
# 		self.b=b
# 	def config(self):
# 		print(' config of ua computer is ',self.a,self.b)

# com1=comp(10,20)
# com1.config()



























