import guessgame
import gameguess
print('Welcome to the game')
screctcode=guessgame.generate_code()
cluesreport=[]
while cluesreport != 'CODE IS CRACKED':
	guess=guessgame.get_guess()
	cluesreport=gameguess.generate_clues(guess,screctcode)
	print('Here is your clues for the game')
	for clue in cluesreport():
		print(clue)