#RE used to find replace from a given string
import re
# str1='Hello how Hello are you'
# result=re.match(r'Hello',str1)
# print(result.group(0))
# result=re.search(r'Hi',str1)
# print(result.group(0))
# result=re.findall(r'Hello',str1)
# print(result)
# print(len(result))
# str1="Beasant"
# str1="Beasant"
# result=re.split(r'a',str1)
# print(result)

# s1='Python is best'
# x=re.sub(r'python','java',s1)
# print(x)
# s1='AV analytics AV'
# pattern=re.compile('AV')
# # x=pattern.findall('AV analytics')
# x=pattern.findall(s1)
# print(x)

s1='Python is great language'
# x=re.findall(r'.',s1)
# print(x)
x=re.findall(r'?',s1)
print(x)