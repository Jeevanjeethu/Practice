# x=('hello',1,'me')
# x[1]
# print(x[1])
# # print(x[3]=8)
# print(x[1:3])
# print(x[-1])
# # x.append(1)

# # empty tuple - x=()
# x=()
# x=1,
# print(type(x))

x=(1,2,3,4,[5,6,7])
# x[4]=[2]
x[4][1]=4
print(x)
print(x.count(3))
print(x.index(3))
# x.clear() - not possible
del x
print(x)