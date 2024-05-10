
exit_outer = False
for i in range(10): # [0..10)
	if exit_outer:  # sogenanntes Schleifen Flag
		break # verlässt die i-Schleife
	for j in range(10): # [0..10)
		print(i, j)
		if i > 2 and j == 5:
			exit_outer = True
			break  # verlässt die j-Schleife

# Aufgabe: selbes Programm/Logik umwandeln in while Schleifen
# i = 0
# while i < 10: ...