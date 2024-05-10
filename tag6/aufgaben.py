# AUFGABEN
# 1. Schreibe eine Funktion, die ein default Argument hat
# und dieses Argument in der Funktion ausgibt.

# 2. Schreibe eine Funktion, die prüft, ob ein default Argument verändert übergeben wurde.
# Wenn ja, gib eine Meldung aus.
def check_default_argument(x=42):
	if(x!=42):
		print("Default Argument wurde verändert")

check_default_argument(45)

# 3. Schreibe eine Funktion, die versucht ein übergebenes Argument (string) zu verändern.
# global mystring
def modify_string(s):
	s = "hack!"
# save(s)

mystring = "test"
modify_string(mystring)
# mystring = load()
print(mystring)
# Schaffst Du es, dass mystring nach dem Aufruf von modify_string() "verändert" ist?
# Tipp: Hoffentlich nicht;) Warum nicht: strings sind immutable "unveränderlich"

# 4. Schreibe eine Funktion, die beliebig viele Argumente entgegennimmt und das grösste zurückgibt.

# 5. Schreibe eine Funktion, die beliebig viele benamte Argumente entgegennimmt
#  und 42 zurückgibt, wenn ein Argument "sinn" heisst, sonst 0

# 6. schreibe eigene sum funktion

# 7. schreibe eigene max funktion


def no_default_ambiguity(y, x=42, z=44): # SyntaxError: non-default argument follows default argument
	print(y)

no_default_ambiguity(43, 43)