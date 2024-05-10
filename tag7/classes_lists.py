class Person:
		def __init__(self, name, age):
				self.name = name
				self.age = age

		def __str__(self):
				return f'{self.name} is {self.age} years old'
		#
		# def __repr__(self):
		# 		return f'Person({self.name}, {self.age})'

person = Person('John', 30)
person2 = Person('Jane', 25)
person3 = Person('Jack', 40)
liste = [person, person2, person3]
print(liste)