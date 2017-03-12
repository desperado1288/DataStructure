#trie tree
class trie(object):
	class trienode(object):
		def __init__(self):
			self.children = [None]*26
			self.isword = False
	
	def __init__(self):
		self.root = self.trienode()
	
	def add(self, word):
		word = word.lower()
		it = self.root
		for w in word:
			i = ord(w) - ord('a')
			if it.children[i] is None:
				it.children[i] = self.trienode()
			it = it.children[i]
		it.isword = True

#only delete the deepest node
	def delete(self, word):
		word = word.lower()
		it = self.root
		for i in range(len(word)):
			idx = ord(word[i]) - ord('a')
			if i == len(word) - 1 and it.children[idx] and it.children[idx].isword:
				it.children[idx] = None
				return True
			it = it.children[idx]
			if it is None:
				return False
		return False

	def search(self, word):
		word = word.lower()
		it = self.root
		for w in word:
			i = ord(w) - ord('a')
			it = it.children[i]
			if it is None:
				return False
		return it.isword
