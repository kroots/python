

def divideBy2(decNumber):

	remstack = []

	while (decNumber > 0):
		rem = decNumber % 2
		remstack.append(rem)
		decNumber = decNumber // 2

	binString = ''

	while len(remstack) > 0:
		binString = binString + str(remstack.pop())

	return binString


print divideBy2(42)





