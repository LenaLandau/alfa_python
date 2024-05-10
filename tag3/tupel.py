
leeres_tupel = ()
tupel = (1, 2, 3, 4)

for i in tupel:
	print(i)

print(tupel[0])  # Ausgabe: 1
len(tupel)  # Ausgabe: 4

# Jedwelche Modifikation scheitert aber oder ist nur durch Kreation eines neuen Tupels erlaubt:
# tupel[0] = 5  # TypeError: 'tuple' object does not support item assignment
# tupel.append(5)  # AttributeError: 'tuple' object has no attribute 'append'

# Kreation eines neuen Tupels
neues_tupel = tupel + (5,)


from collections import namedtuple
Person = namedtuple("Person", ["name", "age", "city"])