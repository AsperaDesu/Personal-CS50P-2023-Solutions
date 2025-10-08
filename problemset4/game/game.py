import random

def get_int(prompt : str):
	while  True:
		try:
			num = int(input(prompt))

			if num <= 0:
				return get_int(prompt)
			else:
				return num
		except ValueError:
			pass

def init_guess(level : int):
	answer = random.randint(1, level)
	guess = ''
	while True:
		guess = get_int('Guess: ')

		if guess < answer:
			print('Too small!')
		elif guess > answer:
			print('Too large!')
		else:
			print('Just right!')
			break

	return

def main():
	level = get_int('Level: ')
	init_guess(level)

if __name__ == '__main__':
	main()