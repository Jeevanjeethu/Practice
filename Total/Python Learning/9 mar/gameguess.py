def generate_class(code,usergenerate):
	if code==userguess:
		return 'CODE IS CRACKED'
	clues=[]
	for ind,num in enumerate(userguess):
		if num==code[ind]:
			clues.append('MATCH')
		elif num in code:
			clues.append('CLOSE')
	if clues==[]:
		return ['NOPE']
	else:
		return clues
