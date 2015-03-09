#binary_search

def binarySearch(alist, item):
	if len(alist) == 0:
		return False
	else:
		midpoint=len(alist)//2
			if alist[midpoint] == item:
				return True
			else:
				if item < alist[midpoint]:
					return binarySearch(alist[:midpoint], item)