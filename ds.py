#stack & queue
#queue in two ways
from collections import deque
class stack():
	def __init__(self):
		self.l = []
	def push(self, a):
		self.l.append(a)
	def pop(self):
		if self.l:
			return self.l.pop()
		else:
			return 'cannot pop on an empty stack'
	def isempty(self):
		return not self.l
	def __repr__(self):
		return repr(self.l)

class queue():
	def __init__(self):
		self.l = deque()
	def __repr__(self):
		return repr(self.l)
	def add(self, a):
		self.l.append(a)
	def pop(self):
		if self.l:
			return self.l.popleft()
		else:
			return 'connot pop on an empty queue'
	def top(self):
		return self.l[0]
	def isempty(self):
		return not self.l

class queue1():
	def __init__(self):
		self.stack1 = stack()
		self.stack2 = stack()
	def add(self, a):
		self.stack1.push(a)
	def pop(self):
		if not self.stack2.isempty():
			return self.stack2.pop()
		elif not self.stack1.isempty():
			while not self.stack1.isempty():
				self.stack2.push(self.stack1.pop())
			return self.stack2.pop()
		else:
			return 'connot pop on an empty queue'
	def __repr__(self):
		return 'stack1: {}, stack2: {}'.format(self.stack1, self.stack2)
