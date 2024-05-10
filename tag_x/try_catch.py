# In Python werden Fehler oft mit einer Struktur namens try-except behandelt. Das ermöglicht es, auf Fehler zu reagieren und das Programm trotzdem fortzusetzen.
# try-Block: Dieser Block enthält Code, von dem man erwartet, dass er möglicherweise einen Fehler verursachen könnte. Python führt diesen Code zunächst normal aus.
# except-Block: Wenn im try-Block ein Fehler auftritt, springt Python in den except-Block, wo der Fehler behandelt werden kann. Wenn kein Fehler auftritt, wird der except-Block übersprungen.


try:
	x = 1 / 0  # Versuch, durch Null zu teilen, was einen Fehler verursacht
except ZeroDivisionError:
	print("Es wurde versucht, durch Null zu teilen.")


def dangerous_function():
	1/0


try:
	dangerous_function()
except:
	print("Unbekannter Fehler")


try:
	dangerous_function()
except Exception as e:
	print(f"Ein Fehler ist aufgetreten: {e}")
	# A blank raise raises the last exception.
	raise