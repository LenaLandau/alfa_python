import datetime

now = datetime.datetime.now()
x = True
for i in range(100_000_000):
		if x:
			pass

end = datetime.datetime.now()
print(end - now)

# Bei performanz: import von Modulen in anderen Sprachen
# Vorschau Mojo ist kompiliert und 10000 schneller als Python
# @superfast