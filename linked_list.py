#linked_list.py


class Node:

	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

class LinkedList:

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0

		while current != None:
			count = count + 1
			current = current.getNext()

		return count

	def search(self,item):
		current = self.head
		found = False

		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found


myList = LinkedList()

myList.add(1213)
myList.add(12212)

print myList.search(1213)





