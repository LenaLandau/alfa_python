# Verschachtelte Daten
# Da ein dict in python beliebige Werte enthalten kann, unter anderem auch wieder ein dict, lassen sich hervorragend hierarchische / verschachtelte Daten damit abbilden.

# Beispiel:
# Ein Dictionary, das Informationen über eine Person enthält
person1 = {
	"vorname": "Max",
	"wohnort": "Musterstadt",
	"alter": 123,
}
person2 = {
	"vorname": "Anna",
	"wohnort": "Musterstadt",
}
person3 = {
	"vorname": "Max",
	"wohnort": "Berlin",
}
print(person1 | person3)
#
# personen = [person1, person2, person3]
#
# print(personen)
# print(personen[2]["wohnort"])
#
#
# # person.