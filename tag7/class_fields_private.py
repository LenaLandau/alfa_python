class Konto:
	def __init__(self, inhaber, saldo):
		self.__inhaber = inhaber
		self.__saldo = saldo

	def getSaldo(self):
		return self.__saldo

	def einzahlen(self, betrag, token):
		if token != "1234":
			print("Zugriff verweigert")
			return
		self.__saldo += betrag

mein_konto = Konto("Max Mustermann", 1000)
# mein_konto.__saldo = 500  # kein Zugriff auf privates Feld
# print(mein_konto.__saldo)  # kein Zugriff auf privates Feld

print(mein_konto.getSaldo()) # Puh, unverändert 1000!

# mein_konto._Konto__saldo = 500  # hacky Zugriff auf privates Feld
# print(mein_konto._Konto__saldo)  # hacky Zugriff auf privates Feld

