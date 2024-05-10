class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	@staticmethod
	def json_to_person(json):
		return Person(json['name'], json['age'])

person = Person.json_to_person({'name': 'John', 'age': 30})