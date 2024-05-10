temperatur = 20
if temperatur > 15:
	print("Es ist warm.")

temperatur = 10
if temperatur > 15:
	print("Es ist warm.")
else:
	print("Es ist kalt.")


temperatur = 10
if temperatur > 15:
	print("Es ist warm.")
elif temperatur > 5:
	print("Es ist kühl.")
else:
	print("Es ist kalt.")


for buchstabe in "abc":
	print(buchstabe)

for zahl in [1, 2, 3]:
	print(zahl)


for key in {"a": "eins", "b": "zwei", "c": "drei"}:
	print(key)

for zahl in range(5):
	print(zahl)

zaehler = 0
while zaehler < 5:
	print(zaehler)
	zaehler += 1