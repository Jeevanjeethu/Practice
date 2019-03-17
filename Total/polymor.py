class A:
	def f1(self):
		print(f1)
class B:
	def f2(self):
		print('f2')

class C:
	def code(self,ide):
		ide.execute()


ide=B
a1=C()
a1.code(ide)