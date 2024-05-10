def hello(nachricht):
		print("Hello, World!",nachricht)

def kontakt(funktion, nachricht):
	funktion(nachricht)

kontakt(hello,"Gruß") # Hello, World!
