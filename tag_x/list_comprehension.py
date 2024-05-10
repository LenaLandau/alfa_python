# list comprehension
# [expression for item in iterable if condition]
# [ausdruck for element in iterable if bedingung]
# [expression for item in iterable]

# ähnlich Mengen Definition früher in Mathe: R+={x | x in R und x>0}

[x*x for x in range(10)]

[x*x for x in range(10) if x % 2 == 0]

# List comprehension kann auch verwendet werden, um eine Liste von Tupeln zu erstellen:
[(x, x*x) for x in range(10)]

liste = [1, 2, 3, 4, 5]
f = lambda x: x*x
# ähnlich Schleifen und map Funktionen
[f(x) for x in liste]
map(f, liste)
results = []
for x in liste: results.append(f(x))


# Verschachtelte List Comprehension
listen = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flache_liste = [element   for unterliste in listen   for element in unterliste]
print(flache_liste) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Achtung die innere Schleife ist die letzte Schleife

# List comprehensions sind ein mächtiges Werkzeug in Python, das hilft, Code, der Listen bearbeitet, kürzer, lesbarer und oft schneller auszuführen als traditionelle Schleifen und map/filter-Funktionen.