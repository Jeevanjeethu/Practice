#python directory

import os
import shutil
print(os.getcwd())
os.chdir("C:\\Users\\Jeevan K\\Desktop\\total")
print(os.getcwd())
print(os.listdir("C:\\Users\\Jeevan K\\Desktop\\total"))
# os.mkdir('computer')
# print(os.listdir("C:\\Users\\Jeevan K\\Desktop\\total"))
# os.rename("computer","laptop")
# print(os.listdir("C:\\Users\\Jeevan K\\Desktop\\total"))
# os.mkdir("C:\\Users\\Jeevan K\\Desktop\\total\\laptop\\program")
# print(os.listdir("C:\\Users\\Jeevan K\\Desktop\\total"))
os.rmdir('C:\\Users\\Jeevan K\\Desktop\\Total\\laptop')

shutil.rmtree('C:\\Users\\Jeevan K\\Desktop\\Total\\New folder')