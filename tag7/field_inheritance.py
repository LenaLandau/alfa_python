# Fahrrad, Auto, Zug < Vehicle
# Dreieck, Kreis, Viereck < Form
# Admin, Editor, Tester < Person
# Hund, Katze, Maus < Tier

class Vehicle:
	# def __init__(self):
	# 	pass
	def honk(self):
		pass

	def drive(self):
		print('brum brum')

class Car(Vehicle):
	def honk(self):
		super().drive()
		print('honk honk, tut tut')

class Bike(Vehicle):
	def honk(self):
		print('ding ding, ring ring')

def letVehicleHonk(fahrzeug:Vehicle):
	fahrzeug.honk()
	fahrzeug.drive()

car = Car()
bike = Bike()

letVehicleHonk(car)
letVehicleHonk(bike)