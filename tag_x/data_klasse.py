from dataclasses import dataclass
# In Python, eine Datenklasse (dataclass) ist ein Dekorator, der eine Klasse zur Speicherung von Datenobjekten definiert, indem er Boilerplate-Code automatisch generiert. Datenklassen wurden in Python 3.7 eingeführt

@dataclass
class Beispiel:
	attribute1: int
	attribute2: str = 'Standardwert'

	def methode(self):
		return self.attribute1 + 1

a = Beispiel(1)
a.x = 7  # type: ignore


# Wenn frozen=True gesetzt ist, macht dies die Instanz der Datenklasse unveränderlich,
# ähnlich wie ein Tupel. Versuche, nach der Instanziierung einer frozen Datenklasse deren Attribute zu ändern, führen zu einem FrozenInstanceError.
@dataclass(frozen=True)
class Punkt0:
	x=0
	y=0

p0 = Punkt0()
p0.x = 1 # AttributeError: can't set attribute
p0.z = 2 # AttributeError: 'Punkt0' object has no attribute 'z'
p0.w = 7 # type: ignore  # hilft nicht

# Wenn order=True gesetzt ist, werden zusätzlich zu den üblichen Methoden Vergleichsmethoden (__lt__, __le__, __gt__, __ge__) zur Klasse hinzugefügt, die es ermöglichen, Instanzen der Datenklasse basierend auf ihren Attributen lexikographisch zu vergleichen.
@dataclass(frozen=True,order=True)
class Punkt:
	x: int
	y: int

a = Punkt(1, 2)
b = Punkt(1, 3)
c = Punkt(2, 1)
print(a < b) # True
print(a < c) # True
