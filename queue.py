#queue.py

class Queue:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self,item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]


q = Queue()

q.enqueue('her there')
print q.dequeue()