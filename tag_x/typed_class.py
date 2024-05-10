import mypy

class Personen:
	def __init__(self, liste:list):
		self.liste = liste
	def __int__(self):
		return 1
	def __adsf__(self):
		print("hallo")

# meine_personen = Personen([{'name':'John', 'age':30}, {'name':'Jane', 'age':25}])
meine_personen = Personen("hallo")
meine_personen.__adsf__()

# diese Funktion gibt den Typ int zurück
def pruefe_type(y:int) -> int:
	return "test"
	# return 1

x:int
x= "sadf"

print(pruefe_type(1))
print(pruefe_type("hallo"))