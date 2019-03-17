# # data=[1,2,3,4,5,6,7,8,9,10]
# # even=[]
# # odd=[]
# # for i in data:
# # 	if i%2==0:
# # 		even.append(i)
# # 	else:
# # 		odd.append(i)
		
# # print(even)
# # print(odd)
# # print(data[2:])
# # print(data[:5])
# # print(data[:])
# # print(data.remove(7))
# # print(data)
# # print(data.pop())
# # print(data.pop())
# # print(data)


# # ndata = ['c','c++','java','net','python']
# # help(list.sort)

# ndata=['c','c++','java','net','python']
# # ndata.clear()
# # print(ndata)
# ndata.sort()
# print(ndata)
# ndata.reverse()
# print(ndata)

# # copy - deep copy

# x=[1,2,3,4]
# y=x
# print(x)
# print(y)
# x.append(5)
# print(x)
# print(y)

# copy - shallow copy
import copy
x=[1,2,3,4]
y=x.copy()
print(id(x))
print(id(y))
print(x)
print(y)
x.append(5)
print(x)
print(y)











