# # f=open("C:\\Users\\Jeevan K\\Desktop\\Python Learning\\file handling\\sample.txt",'w')
# # f.write('Hello good morning\n')
# # f.write('How are you')

# # f.close()

# #append

# # f=open("C:\\Users\\Jeevan K\\Desktop\\Python Learning\\file handling\\sample.txt",'a')
# # f.write('\ni am jeevan\n')
# # f.write('How are you')

# # f.close()

# f=open("C:\\Users\\Jeevan K\\Desktop\\Python Learning\\file handling\\sample1.txt",'r')
# x=f.readlines()
# for i in x:
# 	if 'python' in i:
# 		g=open("C:\\Users\\Jeevan K\\Desktop\\Python Learning\\file handling\\python1.txt","a")
# 		g.write(i)
# g.close()
# f.close()


#context manager

# with open("C:\\Users\\Jeevan K\\Desktop\\Python Learning\\file handling\\sample1.txt",'r') as f:

# 	print(f.readlines())

