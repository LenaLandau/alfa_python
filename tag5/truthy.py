
if True: print("truthy")

# Logische Operatoren:
a = True
b = False
bedingung = a or b
if bedingung: print("truthy")

# via Vergleichsoperatoren
a = 5
b = 10
bedingung = a < b  # Dies ergibt True, weil 5 kleiner als 10 ist.
if bedingung: print("truthy")

# neu: Identitätsoperatoren
a = [1, 2]
b = [1, 2]
bedingung2 = a is b  # Dies ergibt False, weil a und b unterschiedliche Objekte sind, obwohl sie denselben Inhalt haben.

# Mitgliedschaftsoperatoren:
liste = [1, 2, 3]
bedingung = 2 in liste  # Dies ergibt True, weil 2 ein Element der Liste ist.

def freunde():
	return None


if 1: print("truthy!")
if "a": print("truthy!")
if [1]: print("truthy!")
