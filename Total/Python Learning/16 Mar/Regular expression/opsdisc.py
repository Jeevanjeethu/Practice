import re
with open('C:\\Users\\Jeevan K\\Desktop\\Python Learning\\16 Mar\\Regular expression\\sample.txt') as f:
	res=[]
	for i in f.readlines():
		r=re.findall(r'\w+.\w+@\w+.\w+',i)
		if len(r)!=0:
			# res.append(r)
			g=open('C:\\Users\\Jeevan K\\Desktop\\Python Learning\\16 Mar\\Regular expression\\sample5.txt','a')
			for i in r:
				g.write(i)
	# res=[]
	# for i in f.readlines():
	# 	r=re.findall(r'\d\d\d\d\d\d\d\d\d\d',i)
	# 	if len(r)==10:
	# 		res.append(r)
	# print(res)