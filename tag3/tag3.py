import random

# Zeitmessung
x = 4
print(x)

import datetime
start = datetime.datetime.now()
sum = 0
for i in range(10000000):
	sum += i
ende = datetime.datetime.now()
print(ende - start)
print((ende - start).seconds)
print((ende - start).microseconds , "µs")


ziffern = "0123456789"
ziffern_as_int = [int(ziffer) for ziffer in ziffern]

wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

for i in wochentage:
	print(i)

print(wochentage[0])

type([1,2,3])
# <class 'list'>

1 in [1,2,3] # True

def test(*args):
	print(args[0])

test(1,2,3,4,5)

translations = {"dog":"Hund", "cat":"Katze"}
flaggen={"Deutschland":"🇩🇪","Frankreich":"🇫🇷","Spanien":"🇪🇸"};
einwohner={"Deutschland": 80_000_000, "Frankreich": 67_000_000, "Spanien": 47_000_000}

squares = [x**2 for x in range(10)]

evens = [x for x in range(20) if x % 2 == 0]

# for i in range(1_000_000_000):
# 	x = random.random()*100
# 	if i > 700_000_000 + x:
# 		if i % 1_000_000 == 0:
# 			print(i)

# Erstellung eines Dictionary
person = {"name": "Maria", "alter": 30, "beruf": "Ingenieurin"}

# Zugriff auf den Wert mit dem Schlüssel 'name'
print(person["name"])  # Ausgabe: Maria

# Ändern des Wertes mit dem Schlüssel 'alter'
person["alter"] = 31

# Hinzufügen eines neuen Schlüssel-Wert-Paares
person["wohnort"] = "Berlin"

print(person)
# Ausgabe: {'name': 'Maria', 'alter': 31, 'beruf': 'Ingenieurin', 'wohnort': 'Berlin'}


# Ein Dictionary, das unterschiedliche Datentypen speichert
komplexes_dict = {
	"string": "Hallo Welt",     # Ein String
	"integer": 42,              # Eine Ganzzahl
	"float": 3.14159,           # Eine Fließkommazahl
	"list": [1, 2, 3],          # Eine Liste
	"dict": {"a": 1, "b": 2},   # Ein weiteres Dictionary
	"bool": True,               # Ein Boolescher Wert
	"function": print           # Eine Funktion (print-Funktion)
}

# Beispiel von erlaubten schlüsseln:
wahrheitswerte = {True: "Wahr", False: "Falsch"}
ziffern_zu_namen = {0: "null", 1: "eins", 2: "zwei", 3: "drei", 4: "vier", 5: "fünf", 6: "sechs", 7: "sieben", 8: "acht", 9: "neun"}
tuple_als_schluessel = {(1, 2): "Eins und Zwei", (3, 4): "Drei und Vier"}

# Beispiel von verbotenen schlüsseln:
# list_als_schluessel = {[1, 2]: "Eins und Zwei"}  # TypeError: unhashable type: 'list'

# dict_als_schluessel = {{1: 2}: "Eins und Zwei"}  # TypeError: unhashable type: 'dict'

x=5
variable_als_schluessel = {x: "Variable hatte Wert 5"}
print(variable_als_schluessel.keys())	# Ausgabe: dict_keys([5])
print(variable_als_schluessel[5])  # Ausgabe: 'Variable'



import json

obj = {"name": "Max", "alter": 25}
file_name = "../data.json"

s = json.dumps(obj) # object als String serialisieren
json.dump(obj, open(file_name, "w"))  # object als Datei serialisieren

obj = json.loads(s) # object aus String laden
obj = json.load(open(file_name)) # object aus Datei laden

print(obj)





file_name = "test"

open(file_name, "w").write("Hallo Welt")
zeilen = open(file_name).readlines()

print(zeilen)


liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
liste[1:9][8::-2] #ist das selbe wie
teillist1=liste[1:9]
endergebnis=teillist1[8::-2]

hauptstädte = {"Deutschland": "Berlin", "Frankreich": "Paris", "Spanien": "Madrid"}
währungen = {"Deutschland": "Euro", "Frankreich": "Euro", "Spanien": "Euro", "USA": "Dollar"}
# Verschachtelte Daten
# Da ein dict in python beliebige Werte enthalten kann, unter anderem auch wieder ein dict, lassen sich hervorragend hierarchische / verschachtelte Daten damit abbilden.

# Beispiel:
# Ein Dictionary, das Informationen über eine Person enthält
person = {
	"vorname": "Max",
	"nachname": "Mustermann",
	"alter": 25,
	"wohnort": {
		"straße": "Musterstraße 42",
		"plz": 12345,
		"stadt": "Musterstadt"
	}
}
# eutschland": "Deutsch", "Frankreich": "Französisch", "Spanien": "Spanisch"}
buch_autoren = { "Der Pate": "Mario Puzo", "Der Herr der Ringe": "J.R.R. Tolkien", "Harry Potter": "J.K. Rowling" }
wahrzeichen = { "Deutschland": "Brandenburger Tor", "Frankreich": "Eiffelturm", "Spanien": "Sagrada Familia" }
auto_marken_modelle = { "VW": ["Golf", "Polo", "Passat"], "BMW": ["3er", "5er", "7er"], "Audi": ["A3", "A4", "A6"] }

x = 10
y = x+x
z = y+x
