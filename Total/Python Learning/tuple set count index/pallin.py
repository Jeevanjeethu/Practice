# x=input('enter a value')
# s=''
# for i in x:
# 	s=i+s
# if s==x:
# 	print('its a palindrome')
# else:
# 	print('not')
n=''
a=range(100,501)
a=str(a)
for i in a:
	for j in i:
		j=int(j)
		n=n+(j**3)
if n==i:
	print(i)
# sum=0
# num=407
# num1=str(num)
# for i in num1:
# 	i=int(i)
# 	sum=sum+(i**3)
# if sum==num:
# 	print('armstrong')
# else:
# 	print('not')