# Kommentar
print("Hallo 🌍") # Ausgabe von Text auf der Konsole kann auch Sonderzeichen enthalten

# print("Kein Hallo 🌎")  # Zeile 'auskommentieren' mit #

# Variablen

gruss = "Hallo Welt"
print(gruss)

ergebnis = 3 * 2 # Achtung, formeln werden direkt und automatisch ausgerechnet
print(ergebnis) # Ausgabe: 6  (nicht : 3 * 2)

hallö = "Hallo Erde" # Variablennamen können auch Umlaute enthalten
print(hallö)
# hallo⼟ = "Hallo Erde" #
# hallo🌐 = "Hallo Erde" #
# hallo🌎 = "Hallo Erde" # Variablennamen dürfen (noch) keine Sonderzeichen enthalten

# "Variable" heisst 'veränderlich'
# Variablen können Werte speichern, die sich verändern können
alter = 25
print(alter)
alter = 26
print(alter)

# Variablen in Python können Werte von verschiedenen Typen speichern
alter = 25 # Zahl
print(alter)
alter = "fünfundzwanzig" # Text
print(alter)


#Integer (Ganzzahlen)
x = 5
#Float (Fließkommazahlen)
y = 3.14
#Strings (Zeichenketten)
name = "Bob"
#Boolean (Wahrheitswerte)
is_valid = True
#Listen
fruits = ["apple", "banana", "cherry"]
#Dictionaries (Wörterbücher)
person = {"name":"Anna", "age": 28}

global_var = 10	# Globale Variable, überall im Code gültig

# Funktionen sind Code-Blöcke, die wiederverwendet werden können
# Variablen können auch in Funktionen definiert werden, sind (in der Regel) dann aber nur in dieser Funktion gültig
def my_function():
	local_var = 5  # Lokale Variable, nur in dieser Funktion gültig
	print(global_var)  # Ausgabe: 10

# print(local_var)  # Fehler: NameError: name 'local_var' is not defined

# ⚠️ Achtung: Python ist case-sensitive
"Dies ist ein String."
'Dies ist auch ein String.'
# ⚠️ Achtung, in Python gibt es keine 'Char'-Datentypen
# Stattdessen werden einzelne Zeichen in Python als Strings mit der Länge 1 behandelt.

# print('Wie heißt du?')  # Frage nach dem Namen
# meinName = input()
# print('Es ist schön, dich zu treffen, ' + meinName)

# Zugriff auf einzelne Zeichen in einem String
name = "Alice"
print(name[0])  # Ausgabe: A

print("Hi😼"[2])
# 😼


# Teilstring extrahieren (Slicing): [start:stop:step]
name = "Alice"
print(name[0:3])  # Ausgabe: Ali

# Länge eines Strings
name = "Alice"
print(len(name))  # Ausgabe: 5

len("😼") # Ausgabe: 1
# Länge eines Strings in python ist die Anzahl der Zeichen im String,
# ⚠️ nicht die Anzahl der Bytes wie in anderen Programmiersprachen

# Strings können auch Unicode-Zeichen enthalten
# print("\U+26A1")	# Ausgabe: ⚡
# len("\U+26A1")	# Ausgabe: 1

# Strings können in Python mit einfachen oder doppelten Anführungszeichen erstellt werden
"Hallo"
'Hallo'

""" 
Hallo """


import datetime
jetzt = datetime.datetime.now()
print(jetzt) # 2024-04-29 14:48:52.923587

formatiert = jetzt.strftime("%d-%m-%Y")
print(formatiert) # 29-04-2024

# "a".upper() # Ausgabe: A

first_name = "ada"
last_name = "lovelace"
print(first_name+" "+last_name)
print("Hallo "+str(2024))
full_name = f"{first_name} {last_name}"
print(full_name)

year = 2024
print(f"Hello, {2024}!")
print(f"Hello, {year}!")

for char in "Python":
	print(char)

print("P" in "Python")	# Ausgabe: True
print("p" in "Python")	# Ausgabe: False
print("tho" in "Python")	# Ausgabe: True

original = "Hallo Welt! Hallo Python!"
ersetzt = original.replace("Hallo", "Guten Tag")
print(ersetzt)

# Vorschau Funktionen
# in Mathe: f(x) = 2x
# in Python:
def f(x):
	return 2 * x


def hoch(x, y):
	return x ** y

# x, y heissen Parameter / Argumente

print(f(3))  # Ausgabe: 6


from typeguard import typechecked

@typechecked
def test_int(value: int) -> int:
	return value

a = test_int(5)  # Correct type, passes without an issue
b = test_int('test')  # Incorrect type, will raise a TypeError


# langer_text =
"""
Dies ist ein mehrzeiliger String,
der als Kommentar verwendet werden kann.
Python wird diesen String ignorieren, da er keiner Variablen zugewiesen ist.
"""

# print(dir(3))

#besterFreund = "Tim"
# bester Freund = "Tim" Verboten


"a".isdigit()
"1".isdigit() # Ausgabe: True ist eine Zahl


temperatur = 22
if temperatur > 25:
	print("Es ist warm")
	print("wirklich")
else:
	print("Es ist kühl")

for zeichen in "Python":
	print(zeichen)

# f(x) = 2x
def f(x):
	print(x)
	return 2 * x

print(f(3))  # Ausgabe: 3, 6

def ausgabe(x):
	print(x)

ausgabe(f(3))
