class Konto:
	def __init__(self, inhaber, saldo):
		self.inhaber = inhaber
		self.saldo = saldo

mein_konto = Konto("Max Mustermann", 1000)
mein_konto.saldo = 500  # Direkter Zugriff auf öffentliches Feld


