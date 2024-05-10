# 1. FizzBuzz
# Das Standard-FizzBuzz-Problem besteht darin, Zahlen von 1 bis 20 auszudrucken, aber für Vielfache von drei „Fizz“ anstelle der Zahl und für die Vielfachen von fünf „Buzz“ auszugeben. Für Zahlen, die Vielfache von sowohl drei als auch fünf sind, geben Sie „FizzBuzz“ aus.
for i in range(1, 20):
	if i % 3 == 0:
		print("Fizz")
	elif i % 5 == 0:
		print("Buzz")
	elif i % 3 == 0 and i % 5 == 0:
		print("FizzBuzz")
	else:
		print(i)

# 2a. Passwortprüfer
# Schreibe ein Programm, das prüft ob ein Passwort eine Mischung aus Buchstaben (Groß- und Kleinbuchstaben), Ziffern und Sonderzeichen enthält. Tipp: if x in "abcde…"
Passwort = "asf4A@%"
zeichen_im_passwort = set(Passwort)
hat_zahl = zeichen_im_passwort & set("0123456789")
hat_upper = zeichen_im_passwort & set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
hat_lower = zeichen_im_passwort & set("abcdefghijklmnopqrstuvwxyz")
hat_sonder = zeichen_im_passwort & set("@#$%&!?")

if hat_zahl and hat_upper and hat_lower and hat_sonder: # truthy, wenn set nicht leer ist
	print("OK")
else:
	print("Nicht OK")

# alternative lösungen:
# mittels
# isdigit()
# isupper()
# islower()
# isalnum()

# oder mittels regulärer Ausdrücke
# können wir noch nicht

# oder mittels ASCII-Werten (unübersichtlich)

# oder mittels Vergleichsoperatoren
for zeichen in Passwort:
	hat_zahl = "9" >= zeichen >= "0"
	hat_upper = "Z" >= zeichen >= "A"
	hat_lower = "z" >= zeichen >= "a"
	hat_sonder = zeichen in "@#$%&!?"

# 2b. Passwortgenerator
# Schreiben Sie ein Programm, das ein sicheres Passwort generiert. Das Programm sollte nach der gewünschten Länge des Passworts fragen und sicherstellen, dass das generierte Passwort eine Mindestkomplexitätsanforderung (2a) erfüllt. (TIPP: nutze zB Funktion randint(0,26)  lower_chars[my_rand_index]  )
import random
import string
def generiere_passwort(laenge):
	upper_chars = string.ascii_uppercase
	lower_chars = string.ascii_lowercase
	digits = string.digits
	sonder = "@#$%&!?"
	passwort = ""
	for i in range(laenge):
		zeichen = random.choice([upper_chars, lower_chars, digits, sonder])
		passwort += random.choice(zeichen)

# 3. Temperaturumrechnungstabelle
# Schreiben Sie ein Python-Skript, das eine Tabelle von Temperaturen von Grad Celsius in Fahrenheit für 0 bis 100 Grad Celsius in 5-Grad-Schritten ausdruckt. Verwenden Sie eine Schleife, um jedes Paar im Format "XX°C ist YY°F" zu berechnen und auszudrucken.
def celsius_to_fahrenheit(celsius):
	return celsius * 9/5 + 32
for celsius in range(0, 101, 5):
	fahrenheit = celsius_to_fahrenheit(celsius)
	print(f"{celsius}°C ist {fahrenheit}°F")

# 4. Implementiere die Collatz-Vermutung:
# Wenn n gerade ist, teilen Sie sie durch 2.
# Wenn n ungerade ist, multipliziere sie mit 3 und addieren Sie 1.
# Setze den Prozess fort, bis n 1 wird. Das Programm sollte jeden Zwischenwert von n ausdrucken.
# Starte Programm mit verschiedenen Werten. Es sollte immer bei 1 landen.
def collatz(n):
	while n != 1:
		print(n)
		if n % 2 == 0:
			n //= 2
		else:
			n = 3 * n + 1
	print(n)

collatz(10)

# Schulnoten Bewertung
# gegeben Note von 1 bis 6, gib mit if…elif… das passende Wort aus (2==Gut)
note = 2
if note == 1:
	print("Sehr gut")
elif note == 2:
	print("Gut")
elif note == 3:
	print("Befriedigend")
elif note == 4:
	print("Ausreichend")
elif note == 5:
	print("Mangelhaft")
else:
	print("Ungenügend")


# Tropen
# Schreibe einfaches if…elif… welches für verschiedene Temperatur-Bereiche folgende Ausgaben tätigt:
# Heiße Zone
# Gemäßigte Zone
# Kalte Zone
temperatur = 20
if temperatur > 30:
	print("Heiße Zone")
elif temperatur > 10:
	print("Gemäßigte Zone")
else:
	print("Kalte Zone")

# Nutzerstatus
# Es gibt zwei Arten von Nutzern mit passendem Status:
# rolle = "Editor" / "Admin"
# status = "aktiv" / "inaktiv"
# Schreibe ein Programm welches für alle Kombinationen eine passende Meldung ausgibt, z.B. Admin+aktiv: print("Vollzugriff gewährt.")
rolle = "Admin"
status = "aktiv"
if rolle == "Admin" and status == "aktiv":
	print("Vollzugriff gewährt.")
elif rolle == "Admin" and status == "inaktiv":
	print("Eingeschränkter Zugriff.")
elif rolle == "Editor" and status == "aktiv":
	print("Bearbeiten erlaubt.")
else:
	print("Kein Zugriff.")