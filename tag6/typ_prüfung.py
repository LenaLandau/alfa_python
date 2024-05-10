# import mypy
# import pytorch

# @typecheck
def addiere(zahl1: int, zahl2: int) -> int:
	return zahl1 + zahl2


x : int
x = "a"

addiere("1", "2")

# Frage: bestimmt ein default Parameter automatisch den Typ?
# def connect(server="localhost", port=8080): pass
# connect("myhost.com", 80.1)

def polyparams(*varargs):  # varargs ist jetzt ein tuple!
	for arg in varargs:
		print("Wie in Liste: ", arg)


polyparams(1, 2, 3, 4, 5)
polyparams([1, 2, 3, 4, 5])
polyparams(*[1, 2, 3, 4, 5])  # unpacking Ausblick


# polyparams(1, 2, 3, 4, "5")


def polyKeywords(**kwargs):  # kwargs ist jetzt ein dict!
	for key, value in kwargs.items():
		print(f"{key}: {value}")


def polyKeywords2(**kwargs):
	for key in kwargs:
		value = kwargs[key]
		print(f"{key}: {value}")


def nimmEinDict(werte: dict):
	for key, value in werte.items():
		print(f"{key}: {value}")


polyKeywords(a=1, b=2, c=3)  # pseudo dict


# polyKeywords(a=1, a=2, c=3) # Fehler: keyword argument repeated
# nimmEinDict({"a":1, "a":2, "c":3})


# PS: Man kann default Argumente auch mit Typen versehen, aber das ist optional.
def go_deeper(x: int = 0):
	# if x>800:
	# 	print("deep enough")
	# 	return
	print(x)
	# print(x)
	go_deeper(x + 1)
# go_deeper()

# Beispiel
# def generatePassord():
# 	if(not goodPassword()):
# 		return generatePassord()





def get_temperature():
	i = 1
	return 42+i # Placeholder # TODO!

def show_temp():
	j = 10
	temperature = get_temperature()
	print("Temperatur ist ",temperature)

show_temp()

# Listen, Dict, Set sind bisher die einzig bekannte Ausnahme, welche als Referenz übergeben werden
# damit kann man den WERT verändern, aber nicht die REFERENZ
def modify_anything(s):
	# s = "hack!" # Zuweisung bring gar nichts, weil
	s.append(42) # aber hier wird die Liste verändert

l = [1,2,3]
modify_anything(l) # argument l bleibt immer die selbe Referenz
print(l) # Objekt hinter der Referenz wurde verändert (Referenz ist unverändert)



# if x is True:
# 	print("x ist True")