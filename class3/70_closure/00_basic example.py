"""
closure is a technique which allows the storing of values in spite
of the fact that the context in which they have been created does not exist anymore.
"""


def outer(x):
	y = x
	def inner():
		return y
	return inner

f = outer(4)

print(f())