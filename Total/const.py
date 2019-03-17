# class a:
# 	sch='ji'
# 	def __init__(self,a,b):
# 		self.a=a
# 		self.b=b

# 	def add(self):
# 		print('sum is',self.a+self.b)
# 	@classmethod
# 	def info(cls,a,b):
# 		cls.a=a
# 		cls.b=b
# 		return(cls.a+cls.b)


# a1=a(2,3)
# a1.add()
# print(a.info(2,3))

class a:
	@classmethod
	def add(cls,a,b):
		cls.a=a
		cls.b=b
		print(cls.a+cls.b)

a.add(2,3)