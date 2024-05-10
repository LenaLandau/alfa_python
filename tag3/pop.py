personen=["Alf", "Bert", "Charlie", "Dora", "Emil", "Frieda", "Gustav"]

for i in range(len(personen)-2):
	opfer = personen.pop()
	print("Entschuldige", opfer)

print(personen)