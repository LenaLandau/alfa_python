# Ein @classmethod Dekorator wandelt eine Methode in eine Klassenmethode um, die auf die Klasse zugreift, über die sie aufgerufen wird. Diese Methode erhält das Klassenobjekt als erstes Argument (üblicherweise cls genannt) und kann Klassenvariablen ändern, die allen Instanzen gemeinsam sind.
#
#     Vorteile:
#         Nützlich, um Methoden zu definieren, die den Zustand der Klasse ändern müssen oder Zugriff auf Klassenattribute benötigen, unabhängig von einer Instanzierung der Klasse.
#         Ermöglicht es, Fabrikmuster oder Polymorphismus auf Klassenebene einzusetzen.
class Konto:
	zinssatz = 0.05  # Klassenvariable

	def __init__(self, inhaber, saldo=0):
		self.inhaber = inhaber
		self.saldo = saldo

	@classmethod
	def set_zinssatz(cls, neuer_zinssatz):
		cls.zinssatz = neuer_zinssatz