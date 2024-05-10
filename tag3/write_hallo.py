# Texte (strings) und allgemeine Daten lassen sich in Dateien schreiben und lesen
# Dafür können wir die open() Funktion auf folgende Weise nutzen:

file_name = "test"

file_out = open(file_name, "w") # "w" ≈ "write"
file_out.write("Hallo Welt")
# file_out.write({"Nachricht":"Hallo Welt"})
file_out.close() # ⚠️ nicht vergessen, nach dem Schreiben die Datei schliessen!

file_in = open(file_name)  # "r" ≈ "read" optional
zeilen = file_in.readlines()

print(zeilen)
# Aufgabe: was passiert wenn ich ein dict in eine Datei speichern möchte?