class Person:
		def __init__(self, name, age):
				self.name = name
				self.age = age

person = Person('John', 30)
print(person) # <__main__.Person object at 0x12b2f0a10> …
print(person.name)
print(person.age)
print(type(person))


# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# def zeige_Name(self):
# 	print(f"Mein Name ist {self.name}")

