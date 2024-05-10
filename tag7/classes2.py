class Person:
		def __init__(self, name, age):
				self.name = name
				self.age = age

		def zeige_Name(self):
				print(f"Mein Name ist {self.name}")

# Achtung, ohne Einrückung ist das eine ganz normale Funktion, keine Methode von Person
def zeige_Alter(meine_person):
	print(f"Mein Name ist {meine_person.age}")

person = Person('John', 30)
zeige_Alter(person)
person.zeige_Name()

		# def __str__(self):
		# 		return f'{self.name} is {self.age} years old'
		#
		# def __repr__(self):
		# 		return f'Person({self.name}, {self.age})'

person = Person('John', 30)
print(person) # <__main__.Person object at 0x12b2f0a10> …
print(person.name)
print(person.age)
print(type(person))

# person["name"]