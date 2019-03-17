#file readinf
f=open("C:\\Users\\Jeevan K\\Desktop\\Python Learning\\file handling\\sample.txt",'r')
# print(f.read())
# print(f.readline())
# print(f.read(4))
# f.close()

for i in f.readlines():
	if 'jeevan' in i:
		print(i)

print(f.tell())
print(f.seek(10))
print(f.tell())
f.close()