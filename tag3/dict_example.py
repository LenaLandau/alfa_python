# zaehlen von worten mit dict
text = "Hallo Erde, Hallo Welt, Hallo Sonne"
worte={}
for wort in text.split():
	if not wort in worte:
		worte[wort] = 1
	else:
		worte[wort] += 1




print(worte)
max = 0
haeufigstes_wort = ""
for wort in worte:
	zahl = worte[wort]
	if zahl > max:
		max = zahl
		haeufigstes_wort = wort

print(max, haeufigstes_wort)

# sort(worte, key=lambda x: x[1])
