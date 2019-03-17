# # # # # a=[1,2,3,4]
# # # # # b=[4,5,6,7]
# # # # # c=[]
# # # # # for i in a:
# # # # # 	if i in b:
# # # # # 		c.append(i)
# # # # # 	if i not in b:
# # # # # 		c.append(i)
# # # # # for j in b:
# # # # # 	if j not in a:
# # # # # 		c.append(j)

# # # # # print(c)

# # # # a=[1,2,3,4,5,3,7,2]
# # # # m=0
# # # # for i in a:
# # # # 	if i>m:
# # # # 		m=i
# # # # print(m)
# # # # print(max(a))

# # # import doc
# # # print(doc.__doc__)

# # import random
# # def shuffle(x):
# # 	l=range(x)
# # 	random.shuffle(l)
# # 	print(l)
# # shuffle(5)

# x=[1,2,3,4,5,6,7]
# y=[i for i in x if i%2==0]
# print(y)
# y=[i for i in x if i<5]
# print(y)