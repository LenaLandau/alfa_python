#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
	print("Bitte Grad Celsius als Argument übergeben.")
	sys.exit(1)

celsius = sys.argv[1] # 1. Argument celsius als str
fahrenheit = 9/5 * float(celsius) + 32
print(f"{celsius} Grad Celsius sind {fahrenheit} Grad Fahrenheit.")