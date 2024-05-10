class Person:

	count = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		Person.count += 1

	@staticmethod
	def counted():
		print(f'Es gibt {Person.count} Personen')

person1 = Person('John', 30)
person2 = Person('Jane', 25)
person3 = Person('Jack', 40)
print(Person.counted())