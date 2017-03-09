from tree import tree
l = [1,5,8,'#',6,7,9,4,'#','#','#','#',15]
print('import tree:\n{}'.format(l))
t = tree(l)
print(t.depth())
l_preorder = t.preorder()
print('preorder sequence:\n{}'.format(l_preorder))
if l_preorder == l:
	print('tree import correct: same with preorder seq')
else:
	print('tree import wrong: different from preorder seq')
