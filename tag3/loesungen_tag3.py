# Erstelle eine Funktion, die zwei Listen erhält und prüft, ob in beiden die Zahl 42 vorkommt
def pruefe_42(liste1, liste2):
		return 42 in liste1 and 42 in liste2

# Erstelle eine Funktion, die prüft, ob alle Elemente einer Liste in einer anderen Liste vorhanden sind. (nicht notwendig an der selben Position)
def alle_in(liste1, liste2):
		for x in liste1:
				if x not in liste2:
						return False
		return True

# gemeinsamen Elemente zweier Listen:
# Schreibe eine Funktion, die die Schnittmenge zweier Listen zurückgibt.
def schnittmenge(liste1, liste2):
		return list(set(liste1) & set(liste2))

# • Definiere pure sortier Funktion sort([2,3,1]) oder sort(3,1,2) => [1,2,3]
def sort(*args):
		return sorted(args)

def sorted_manuell(liste):
	pass
	# too hard, see Jan ;)


# Entferne Duplikate aus einer Liste (ohne Set-Verwendung, modifizierend oder per Konstruktion)
def entferne_duplikate(liste):
		neu = []
		for x in liste:
				if x not in neu:
						neu.append(x)
		return neu

# Identifiziere das Element, das in einer Liste am häufigsten vorkommt. ( via dict )
def am_haeufigsten(liste):
		max = 0
		max_key = None
		zaehler = {}
		for x in liste:
				if x in zaehler:
						zaehler[x] += 1
						if zaehler[x] > max:
								max = zaehler[x]
								max_key = x
				else:
						zaehler[x] = 1
		return max_key

def test_am_haeufigsten():
	liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 1, 1, 1, 1,2,2,0]
	assert am_haeufigsten(liste) == 1

# Funktion Permutation / Rotieren von Elementen in einer Liste  z.B. [1,2,3,4] => [2,3,4,1]
def rotiere(liste):
		return liste[1:] + [liste[0]]

# IM KOPF: welche Elemente werden hier ausgewählt:
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
teilstueck = liste[2:6:3] # starte ab 2, schrittweite 3 (also 5), gehe bis 6 also ende
# print(teilstueck) # 2, 5 ;)

def test_rotiere():
	liste = [0, 1, 2, 3, 4]
	rotiert = rotiere(liste)
	erwartet = [1, 2, 3, 4, 0]
	assert rotiert == erwartet

test_rotiere()
print("Alle Tests erfolgreich!")



# LÖSUNGEN TAG 3
# Dictionary (Folie 29±1)

# Zusammenführen von zwei Dictionaries: Schreibe eine Funktion, die zwei Dictionaries zusammenführt und dabei die Werte von übereinstimmenden Schlüsseln addiert
def merge_dicts(dict1, dict2):
		for key in dict1:
				if key in dict2:
						dict2[key] += dict1[key]
				else:
						dict2[key] = dict1[key]
		return dict2

import pytest
def test_merge_dicts():
	d1 = {"a": 1, "b": 2}
	d2 = {"a": 3, "b": 3, "c": 4}
	ergebnis = merge_dicts(d1, d2)
	assert ergebnis == {"a": 4, "b": 5, "c": 4}

# Umkehren der Schlüssel-Werte-Paare in einem Dictionary: Erstelle eine Funktion, die die Schlüssel und Werte eines Dictionaries umkehrt.
# return {v: k for k, v in d.items()}
def invertiere_dict(d):
	neu = {}
	for key in d:
		neu[d[key]] = key
	return neu

# darf eine Datei ( f = open(file_name) ) als Schlüssel verwendet werden? warum(nicht)?
# nein, weil Dateien nicht 'hashbar' sind, weil sie veränderbar sind.