#Password Generator using random
#Generates required no of password with mentioned length
import random
char='abcdefghijklmnopqrstuvwxyz0123456789'
y=int(input('Enter nummber of password required'))
x=int(input('Enter required length of the Password'))

for j in range(y):
    password=''
    for i in range(x):
        password+=random.choice(char)
    print(password)
