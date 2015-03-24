#factorial.py


def fact(n):
	if (n <= 1):
		return 1
	else:
		return n * (n - 1)


print fact(100)