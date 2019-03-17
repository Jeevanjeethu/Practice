# # x=['a','b','c','c']
# # x.count('c')
# # x.index('c')
# # print(x)
# str1=''
# data='python'
# for i in data:
# 	str1=i+str1
# print(str1)
x=input('enter a value')
s=''
for i in x:
	s=i+s
if s==x:
	print('its a palindrome')
else:
	print('not')
