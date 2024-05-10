def f(x):
	if x > 0:
		return "positiv"
	elif x < 0:
		return "negativ"


a = [1, 2]


def modify_list(liste): liste.pop()


modify_list(a)
a == [1]


def drucke_info(name, alter, beruf):
	print(f"Name: {name}")
	print(f"Alter: {alter}")
	print(f"Beruf: {beruf}")


drucke_info(alter=30, beruf="Ingenieurin", name="Maria")


def addiere(zahl1: int, zahl2: int) -> int:
	return zahl1 + zahl2


# addiere("a", "b")
#
# x:int
# x = "a"

def connect(server="localhost", port=8080): pass


connect()  # ok
connect(port=80)
connect(server="myhost.com")
connect(port=80, server="myhost.com")


def polyparams(*varargs):
	for arg in varargs:
		print("Wie in Liste: ", arg)


polyparams(1, 2, 3, 4, 5)
polyparams([1, 2, 3, 4, 5])
polyparams(*[1, 2, 3, 4, 5])
x, y, *rest = [1, 2, 3, 4, 5]

def polyKeywords(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")

def polyKeywords2(**kwargs):
	for key in kwargs:
		value = kwargs[key]
		print(f"{key}: {value}")

polyKeywords(a=1, b=2, c=3) # pseudo dict


# Docstrings
def function_name(param1, param2):
	"""
	Description of what the function does.

	Args:
			param1 (type): Description of param1.
			param2 (type): Description of param2.

	Returns:
			type: Description of return value.

	Raises:
			ExceptionType: Why and when this exception is raised.

	"""
	# function body
	pass




def show_temp():
	temperature = get_temperature()
	print("Temperatur ist ",temperature)

def get_temperature():
	return 42 # Placeholder # TODO!

show_temp()

def default_ambiguity(x=42,y,z=44): # SyntaxError: non-default argument follows default argument
	print(y)

default_ambiguity(43,43) # x,y or y,z ??