for i in range(10):
	if i == 5:
		break  # Verlässt die Schleife, wenn i gleich 5 ist
	print(i)
# Ausgabe: 0 1 2 3 4

for i in range(10):
	if i % 2 == 0:
		continue  # Überspringt die folgenden Befehle in der Schleife, wenn i gerade ist
	print(i)
# Ausgabe: 1 3 5 7 9


for letter in "abcd":
	if ist_vokal(letter):
		continue
print(letter)
# Ausgabe: b c d


def finde_erste_gerade(zahlen):
	for num in zahlen:
		if num % 2 == 0:
			return num  # Gibt die erste gerade Zahl zurück und verlässt die Funktion
	return None  # Keine gerade Zahl gefunden

# während break nur die Schleife verlässt, wird mit return auch die Funktion verlassen

while True:
	connection = accept_client()
	connection.send("Hello")