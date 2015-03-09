#fibonacci.py

arr = [1,1]
tmp = 0

while tmp < 200:
	print arr[1]
	tmp = sum(arr)
	arr.append(tmp)
	del arr[0]


	