# Quadrat < Vieleck < Form
class Form:
	def area(self):
		print("Berechne Fläche nicht möglich für abstrakte Form")
		pass

class Circle(Form):
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return 3.14159 * self.radius ** 2

class Vieleck(Form):
	def __init__(self, number_of_edges, number_of_corners):
		self.number_of_corners = number_of_corners
		self.number_of_edges = number_of_edges

class Quadrat(Vieleck):
	def __init__(self, length):
		super().__init__(4, 4) # verwende die __init__ Methode von Vieleck oder per Hand
		# self.number_of_corners = 4
		# self.number_of_edges = 4
		self.length = length

	def area(self):
		return self.length ** 2