#!/usr/bin/env python3
import sys

# # hardcoded filenames
# filename1 = "c:/user/github/tag4/tag4.py"
# filename2 = "tag4/mein_modul.py"

# flexibler: Dateinamen als Argumente übergeben
print(sys.argv) # index 0 ist der Name des Skripts
if len(sys.argv) > 1:
	print("Zusatzargument 1", sys.argv[1])
	# print("Zusatzargument 2", sys.argv[2])
# Aufgabe gebe alle Argumente aus ^^

	# filename=sys.argv[1]
	# with open(filename, "r") as file:
	# 	print(file.read())
