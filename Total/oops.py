# # class computer:
# # 	def config(self):
# # 		print("dell")

# # com1=computer()
# # com2=computer()

# # com1.config()
# # com2.config()

# # computer.config(com1)


# # class calculator:
# # 	def __init__(self,a,b):
# # 		self.a=a
# # 		self.b=b

# # 	def add(self):
# # 		print('sum is',self.a,self.b)

# # a=calculator(2,3)
# # a.add()

# # class computer:
# # 	def __init__(self,ram,cpu):
# # 		self.ram=ram
# # 		self.cpu=cpu

# # 	def config(self):
# # 		print(' config is',self.ram,self.cpu)

# # com1=computer(15,250)
# # com1.config()

# # class sub:
# # 	def __init__(self,a,b):
# # 		self.a=a
# # 		self.b=b



# # 	def m(self):
# # 		print('product is',self.a*self.b)

# # x=sub(3,5)
# # # x.m()

# # # class sqaure:
# # # 	def __init__(self,a):
# # # 		self.a=a

# # # 	def sq(self):
# # # 		print('square of {} is'.format(self.a),self.a*self.a)

# # # s=sqaure(4)
# # # s.sq()


# # class add:
# # 	def a(self):
# # 		print('config')

# # c=add()
# # c.a()

# #instance variables and class or static variable

# class car:
# 	wheel=4
# 	def __init__(self,mil,com):
# 		self.mil=mil
# 		self.com=com

# 	def cars(self):
# 		print('config of car is',self.mil,self.com)

# c1=car(15,'car')


# c1.cars()
# print(c1.wheel())

class school:
	sch='Hello'
	def __init__(self,m1,m2,m3):
		self.m1=m1
		self.m2=m2
		self.m3=m3

	def avg(self):
		return (self.m1+self.m2+self.m3)/3
	@classmethod
	def inf(cls):
		return cls.sch

s1=school(10,20,30)

print(s1.avg())
print(school.inf())






















































