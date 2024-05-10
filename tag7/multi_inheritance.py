class Drucker:
	def drucken(self):
		return "Druckt ein Dokument"

class Scanner:
	def scannen(self):
		return "Scannt ein Dokument"

class Multifunktionsgerät(Drucker, Scanner):
	pass

mfg = Multifunktionsgerät()
print(mfg.drucken())  # Ausgabe: Druckt ein Dokument
print(mfg.scannen())  # Ausgabe: Scannt ein Dokument
