from ds import queue
class tree(object):
	class treenode(object):
		def __init__(self, v):
			if type(v) is not int:
				print('need int as node value')
				return
			self.t = v 
			self.left = None
			self.right = None
		def __repr__(self):
			return('val: {}, left: {}, right: {}'.format(self.t, self.left, self.right))

	def __init__(self, l):
		#default order
		s = queue()
		if l:
			s.add(self.treenode(l[0]))
			self.root = s.top()
		else:
			print('empty tree imported')
		i = 1
		while i < len(l):
			curnode = s.pop()
			ll = l[i]
			if ll != '#':
				newnode = self.treenode(ll)
				s.add(newnode)
				curnode.left = newnode
			i += 1
			if i >= len(l):
				break
			ll = l[i]
			if ll != '#':
				newnode = self.treenode(ll)
				s.add(newnode)
				curnode.right = newnode

			i += 1
		print('tree import completed')
		
	def add(self, a):
		r = self.root
		while r:
			if a < r.t:
				if not r.left:
					r.left = self.treenode(a)
					break
				else:
					r = r.left
			elif a > r.t:
				if not r.right:
					r.right = self.treenode(a)
					break
				else:
					r = r.right
			else:
				print('node value cannot be equal with')
	def depth(self):
		r = self.root
		def depth_(node):
			if not node:
				return 0
			else:
				return max(depth_(node.left), depth_(node.right)) + 1
		return depth_(r)
	def preorder(self):
		r = self.root
		q = queue()
		if r:
			q.add(r)
		else:
			print('empty tree')
		l = []
		while not q.isempty():
			n = q.pop()
			if n:
				l.append(n.t)
			else:
				l.append('#')
				continue
			q.add(n.left)
			q.add(n.right)
		while l[-1] == '#':
			l.pop()
		return l

		
