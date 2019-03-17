x=int(input('enter x'))
y=int(input('enter y'))
g=0
for i in range(2,x+1):
	if x%i==0:
		if y%i==0:
			if i>g:
				g=i

print(g)


# x=input('enter a value')
# y=input('enter a search')
# for i in x:
# 	if i==y:
# 		print(yes)



