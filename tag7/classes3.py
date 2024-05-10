class Person:
		def __init__(self, name, age):
				self.name = name
				self.age = age

		def zeige_Name(self):
				print(f"Mein Name ist {self.name}")

person = Person('John', 30)
person.zeige_Name()
