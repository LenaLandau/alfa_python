# Aufgaben Tag 2

# Schreibe Programm welches nach Namen Fragt und Länge ausgibt
name = input("Wie heißt du? ")
print("Dein Name hat", len(name), "Zeichen.")

# Schreibe Programm welches den Namen (o.ä.) umdreht Lars => sraL  (via for loop)
new_name = ""
for c in name:
	new_name = c + new_name

# Schreibe Programm welches vom Namen (o.ä.) jedes a in e (…) umwandelt ( if letter == 'a': … )
name.replace("a", "e")

# Schreibe Programm welches vom Namen (o.ä.) die Vokale (aeiou) zählt
count = 0
for c in name:
	if c in "aeiou":
		count += 1

# Schreibe Programm welches im  Namen (o.ä.) Leerzeichen einfügt: "Lars" => "L a r s"
new_name = ""
for c in name:
	new_name = new_name + c + " "

	# Palindrom-Prüfung
	# prüfe, ob ein gegebener String ein Palindrom ist (ein Wort, das vorwärts und rückwärts gelesen gleich bleibt)
	# z.B. abacaba
word = "abacaba"
print(word == word[::-1]) # oder
print(word == reversed(word))




# Zusatzaufgaben
# Formatiere Name und Vorname und Titel => mit f"{title} …" => "Herr Ferdinant Mustermann"
name = "Mustermann"
vorname = "Ferdinant"
titel = "Herr"
print(f"{titel} {vorname} {name}")

# Berechnung des Alters anhand des Geburtsjahres ±1
import datetime
geburtsjahr = 2000
print(datetime.datetime.now().year - geburtsjahr) # ±1

# Umrechnung von Temperaturen
# Schreibe eine Funktion, die eine Temperatur in Celsius entgegennimmt und diese in Fahrenheit umrechnet.
def celsius_to_fahrenheit(celsius):
	return celsius * 9/5 + 32

# Umwandlung von Minuten in Stunden und Minuten
def minuten_in_stunden_und_minuten(minuten):
	stunden = minuten // 60
	minuten = minuten % 60
	return stunden, minuten # oder als Tuple, rückwirk

# Schreibe eine Funktion, die eine Anzahl von Minuten entgegennimmt und diese in Stunden und Minuten umwandelt.
# Trivialer Taschenrechner mit Funktionen
# Schreibe eine Python-Anwendung, die Grundoperationen (Addition, Subtraktion, Multiplikation, Division) über Funktionen ermöglicht.
def addiere(x,y):
	return x+y
def subtrahiere(x,y):
	return x-y
def multipliziere(x,y):
	return x*y
def dividiere(x,y):
	return x/y

print(dividiere(10, 5), "kinderkram, nur um sich mit Funktionen 101 vertraut zu machen")