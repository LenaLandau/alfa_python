# In Python sind Dekorateure eine sehr leistungsfähige und ausdrucksstarke Funktion zur Modifikation von Funktionen oder Methoden. Ein Dekorateur ist im Wesentlichen eine Funktion, die eine andere Funktion umschließt, um ihr Verhalten zu erweitern oder zu ändern, ohne sie direkt zu modifizieren.
# Grundkonzept
#
# Ein Dekorateur nimmt eine Funktion als Argument und gibt eine Funktion zurück. Die einfachste Form eines Dekorateurs sieht folgendermaßen aus:

def dekorateur(funktion):
	print("Funktion wird umhüllt", funktion)

	def umhuellende(*args, **kwargs):
		print("Umhüllende Funktion vor Aufruf von ",funktion)
		# Code vor dem Aufruf der Funktion
		ergebnis = funktion(*args, **kwargs)
		# Code nach dem Aufruf der Funktion
		print("Umhüllende Funktion nach Aufruf von ",funktion)
		return ergebnis
	return umhuellende

# Anwendung eines Dekorateurs
# Dekorateure werden mit dem @-Symbol vor einer Funktion definiert:

@dekorateur
def hallo():
	print("Funktionsaufruf hallo")

hallo()