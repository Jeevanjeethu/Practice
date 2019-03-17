import random
def get_guess():
	return list(input('enter ua guess'))

def generate_code():
	digits=(str(num) for num in range(10))
	random.shuffle(digits)
	return digits[:3]
