if True:
	print("wahr")

elemente = [1, 2, 3, 4]
for element in elemente:
	if element % 2 == 0:
		elemente.remove(element)

# Erwartetes Ergebnis könnte [1, 3, 4] sein, tatsächlich ist es aber [1, 3], weil die Schleife einige Elemente überspringt


i = 0
while i < 5:
	print(i)
	if i == 2:
	# Eine Modifikation, die die Bedingung beeinflusst
		i = 5  # Setzt i direkt auf 5, was die Schleife abrupt beendet
	else:
		i += 1
