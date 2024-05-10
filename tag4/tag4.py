#!/usr/bin/env python3
import mein_modul
mein_modul.meine_modul_funktion()
print(mein_modul.xxx) # Variablen aus modul.py stehen per modul-Präfix zur Verfügung

# spezielle Funktionen und Variablen eines Moduls direkt zugänglich machen:
from mein_modul import meine_modul_funktion, xxx
print(xxx)
meine_modul_funktion()