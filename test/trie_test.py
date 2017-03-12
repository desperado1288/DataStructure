import sys
sys.path.insert(0, '../') 


from trie import trie
import unittest

class TestTrieMethods(unittest.TestCase):
  def test_basic(self):
    t = trie()
    t.add('next')
    t.add('nexas')
    find = t.search('next')
    self.assertTrue(find)
    self.assertTrue(t.search('nexas'))
    #search substring
    self.assertFalse(t.search('nexa'))

    #search string that is not in the tree
    self.assertFalse(t.search('null'))

  def test_delete(self):
    t = trie()
    t.add('next')
    t.add('nexas')
    self.assertTrue(t.delete('nexas'))
    self.assertFalse(t.delete('nexas'))
    self.assertFalse(t.delete('ne'))
    self.assertFalse(t.search('nexas'))
    #search substring of the one just deleted
    self.assertFalse(t.search('nexa'))
    #make sure not effecting other words
    self.assertTrue(t.search('next'))
    self.assertFalse(t.search('ne')) 



if __name__ == '__main__':
    unittest.main()
