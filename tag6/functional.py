def square(x):
	return x * x

def divide(x):
	return x / 2

def divide_2_by_x(x):
	return 2 / x

def is_even(x):
	return x % 2 == 0

numbers = [0, 1, 2, 3, 4, 5]
# list(map(divide_2_by_x, numbers))

# Using map() to square numbers
squared_numbers = list(map(square, numbers))
assert squared_numbers == [0, 1, 4, 9, 16, 25]

# Using filter() to filter even numbers
even_numbers = list(filter(is_even, numbers))
assert even_numbers == [0, 2, 4]

# def problematic_falsy(x):
# 	return
# even_numbers = list(filter(problematic_falsy, numbers))

from functools import reduce

def multiply(x, y):
	return x * y



def quadrat(x):
	return x * x

meine_funktion = quadrat
print(meine_funktion(5))  # Gibt 25 aus

# Funktionen als Argumente
def ausfuehren(funktion, argument):
	return funktion(argument)

print(ausfuehren(quadrat, 5))  # Gibt 25 aus


def erzeuge_addierer(x):
	def addierer(y):
		return x + y
	return addierer

add_fuenf = erzeuge_addierer(5)
print(add_fuenf(3))  # Gibt 8 aus


# Using reduce() to compute the product of elements in a list
product = reduce(multiply, [1, 2, 3, 4, 5]) # 5*4*3*2*1
print(product)
multiply(multiply(multiply(multiply(1,2),3),4),5)

# permute list functionally
# fold(permute,list,[])