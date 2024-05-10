d = {"a": 1, "b": 4, "c": 3, "d": 2}
sortiert = sorted(d, key=d.get, reverse=True) # gives only sorted keys based on values !!!
for w in sortiert:
	print(w, d[w])