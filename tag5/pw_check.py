Passwort = "asf4A@%"
zeichen_im_passwort = set(Passwort)
hat_zahl = zeichen_im_passwort & set("0123456789")
hat_upper = zeichen_im_passwort & set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
hat_lower = zeichen_im_passwort & set("abcdefghijklmnopqrstuvwxyz")
hat_sonder = zeichen_im_passwort & set("@#$%&!?")

if hat_zahl and hat_upper and hat_lower and hat_sonder: # truthy, wenn set nicht leer ist
	print("OK")
else:
	print("Nicht OK")

# alternative lösungen:
# mittels
# isdigit()
# isupper()
# islower()
# isalnum()

# oder mittels regulärer Ausdrücke
# können wir noch nicht

# oder mittels ASCII-Werten (unübersichtlich)

# oder mittels Vergleichsoperatoren
for zeichen in Passwort:
	hat_zahl = "9" >= zeichen >= "0"
	hat_upper = "Z" >= zeichen >= "A"
	hat_lower = "z" >= zeichen >= "a"
	hat_sonder = zeichen in "@#$%&!?"
