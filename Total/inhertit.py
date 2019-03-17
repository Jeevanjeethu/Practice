# class A:

# 	def f1(self):
# 		print('f1')

# class B:

# 	def f2(self):
# 		print(('f2'))

# class C(A,B):

# 	def f3(self):
# 		print('f3')

# a1=C()
# a1.f1()


# class A:

# 	def __init__(self):
# 		print('init of A')

# class B:

# 	def __init__(self):
# 		print('b')

# class C(A):

# 	def __init__(self):
# 		super().__init__()
# 		print('c')
# 	def add(self):
# 		print(add)


# a1=C()

class computer:
	def __init__(self):
		print('init')

	def config(self):
		print('dell')

	@classmethod
	def confg(cls):
		print('class')

# a1=computer()
# a1.config()

computer.confg()





























