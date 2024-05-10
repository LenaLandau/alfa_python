def zahlen_generator(max):
	i = 0
	while i < max:
		yield i
		i += 1

for zahl in zahlen_generator(5):
	print(zahl)