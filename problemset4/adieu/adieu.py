import inflect

p = inflect.engine()

lists = []

while True:
	try:
		name = input('Name: ')
		lists.append(name)
	except EOFError:
		break


print(f'Adieu, adieu, to {p.join(lists)}')
