"""
Der Begriff set in Python bezeichnet eine Sammlung, die keine doppelten Elemente enthält und deren Reihenfolge nicht definiert ist. Dies ist besonders nützlich, wenn man eine Gruppe von einzigartigen Elementen verwalten möchte, ohne sich um die Reihenfolge oder doppelte Werte kümmern zu müssen.

Hier sind einige grundlegende Operationen mit set:

Erstellung eines Sets:
Ein Set wird mit geschweiften Klammern {} erstellt, wobei die Elemente durch Kommata getrennt sind. Ein leeres Set wird jedoch mit set() und nicht mit {} erstellt, da {} ein leeres Dictionary darstellt.
"""
zahlen = {1, 2, 3, 4}
leeres_set = set()
"""
Hinzufügen von Elementen:
Mit der Methode .add() kann ein einzelnes Element zu einem Set hinzugefügt werden.
"""
zahlen.add(5)
"""
Entfernen von Elementen:
Elemente können mit der Methode .remove() entfernt werden. 
Wenn das Element nicht im Set vorhanden ist, wird ein Fehler ausgelöst.
"""
zahlen.remove(2)
"""
Alternativ kann .discard() verwendet werden, das keinen Fehler auslöst, wenn das Element nicht existiert.
"""
zahlen.discard(10)
"""
Prüfung, ob ein Element im Set ist:
Dies kann mit dem in Schlüsselwort überprüft werden.
"""
if 1 in zahlen:
	print("1 ist im Set")
"""
Set-Operationen:
Sets unterstützen mathematische Mengenoperationen wie Vereinigung, Schnitt und Differenz.
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

vereinigung = set1 | set2  # {1, 2, 3, 4, 5}
schnitt = set1 & set2      # {3}
differenz = set1 - set2    # {1, 2}

"""
Diese Operationen machen set zu einem mächtigen Werkzeug für viele Probleme, bei denen es um die Verwaltung einzigartiger Elemente geht.
"""
