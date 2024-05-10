# Beispiel reine Funktion
def fakultät(n):
	if n==0 : return 1
	return n * fakultät(n - 1)

print(fakultät(5)) # 120

# Beispiel unreine Funktion
andere_werte = [42]
def seiteneffekte():
	andere_werte.append(43)
	print("Hallo Welt")

seiteneffekte()
print(andere_werte)