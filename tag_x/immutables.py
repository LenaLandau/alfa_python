# # In Python sind einige grundlegende Datentypen unveränderlich (immutable). Diese Unveränderlichkeit bedeutet, dass, einmal ein Objekt eines dieser Datentypen erstellt wurde, sein Inhalt oder sein Zustand nicht mehr geändert werden kann. Hier sind einige Beispiele für unveränderliche Datentypen in Python:
#
# Integers
# Ganze Zahlen können nicht verändert werden. Jede Operation, die eine Zahl zu verändern scheint, erstellt tatsächlich ein neues Integer-Objekt.
#
# Floats
# Wie ganze Zahlen sind auch Gleitkommazahlen unveränderlich.
#
# Strings
# Zeichenketten sind in Python unveränderlich. Änderungen an einem String führen zur Erstellung eines neuen String-Objekts.
#
# Tuples
# Ein Tuple ist eine Sammlung von Python-Objekten, die, einmal erstellt, nicht mehr geändert werden kann. Versuche, ein Element eines Tuples zu ändern, führen zu einem Typfehler.
#
# Frozensets
# Ein frozenset ist eine unveränderliche Version eines Sets. Es kann nicht bearbeitet werden, nachdem es erstellt wurde, was bedeutet, dass man keine Elemente hinzufügen oder entfernen kann.

# Erstellung und Verwendung eines frozensets
fset = frozenset([1, 2, 3, 4])
try:
	fset.add(5)
except AttributeError as e:
	print(e)  # 'frozenset' Objekt hat kein Attribut 'add'