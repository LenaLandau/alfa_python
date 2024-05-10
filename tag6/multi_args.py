def quadrat(x):
	return x*x

def hoch_drei(x):
	return x*x*x

def execute(meine_funktionen,arg):
	for f in meine_funktionen:
		print(f(arg))

execute([quadrat, hoch_drei],2)