def kombiniere_kwargs(**kwargs):
	print("OK")

# kombiniere_kwargs("a","b","c")  # TypeError: kombiniere_kwargs() takes 0 positional arguments but 3 were given
# GEHT NICHT

kombiniere_kwargs(a=1, b=2, c=3)  # pseudo dict