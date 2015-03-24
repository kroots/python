
def f(n): 
	for x in range(n): 
		yield x**2 

for x in f(5): 
	print x,