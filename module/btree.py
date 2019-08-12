#!/usr/bin/python
class Node():
  def __init__(self):
    self.val    = None
    self.left   = None
    self.right  = None
    self.parent = None

  def setLeft(self, node):
    if not isinstance(node, Node):
      raise Exception('node should be Node class')
    self.left = node
    node.parent = self

  def setRight(self, node):
    if not isinstance(node, Node):
      raise Exception('node should be Node class')
    self.right = node
    node.parent = self

  def setValue(self, val):
    self.val = val

  def getValue(self):
    return self.val

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right

  def __gt__(self, anode):
    return (self.val > anode.val) if anode is not None else True

  def __lt__(self, anode):
    return (self.val < anode.val) if anode is not None else True

  def __str__(self):
    return str(self.val)

  __repr__ = __str__

class BTree(object):
  def __init__(self, l = None):
    self.root = None

    if isinstance(l, list):
      for e in l:
        self.insert(e)

  def travel_or_alloc(self, node, queue):
    if node is None :
      new_node = Node()
      return new_node
    else:
      queue.append(node)
    return None

  def allocate_bottom_node(self):
    node = self.root
    if node is None:
      self.root = Node()
      return self.root
    queue = []
    while(node is not None):
      n = self.travel_or_alloc(node.left, queue)
      if n is not None:
        node.left = n
        n.parent = node
        return n

      n = self.travel_or_alloc(node.right, queue)
      if n is not None:
        node.right = n
        n.parent = node
        return n

      node = queue.pop(0)

  def insert(self, element):
    node = self.allocate_bottom_node()
    node.val = element
    return node

  def extract(self):
    prev_node = None
    node = self.root
    queue = []

    while(node is not None):
      if node.left is not None:
        queue.append(node.left)
      if node.right is not None:
        queue.append(node.right)
      prev_node = node
      try:
        node = queue.pop(0)
      except:
        break

    if(prev_node is not None):
      parent_node = prev_node.parent
      if parent_node is not None:
        if parent_node.left == prev_node:
          parent_node.left = None
        else:
          parent_node.right = None
      else:
        self.root = None
      return prev_node.val
    return None

  def dfs_(self, node):
    if node is None:
      return
    self.dfs_(node.left)
    print node.val,
    self.dfs_(node.right)

  def DFS(self):
    self.dfs_(self.root)
    print ''

  def BFS(self):
    node = self.root
    if node is None:
      print 'None',
      return
    queue = [node]

    while(queue):
      node = queue.pop(0)
      if node is None:
        print 'None',
        continue
      print node.val,

      queue.append(node.left)
      queue.append(node.right)

    print ''

  def __iter__(self):
    return self

  def next(self):
    val = self.extract()
    if val is None:
      raise StopIteration
    else:
      return val

class BHeap(BTree):
  def reorder(self):
    node = self.root
    while (node is not None):
      if node.left is not None:
        min_node = node.left if node.left < node.right else node.right
        MIN_NODE = node if node < min_node else min_node

        if MIN_NODE is not node:
          temp_val = node.val
          node.val = MIN_NODE.val
          MIN_NODE.val = temp_val
          node = MIN_NODE
        else:
          node = None
      else:
        node = None

  def reorder_from_bottom(self, node):
    while (node is not None):
      pnode = node.parent
      if(pnode is None):
        node = None
        continue
      if node.val < pnode.val:
        t = pnode.val
        pnode.val = node.val
        node.val = t
        node = pnode
      else:
        node = None

  def insert(self, val):
    node = super(BHeap, self).insert(val)
    self.reorder_from_bottom(node)

  def extract(self):
    if self.root is None:
      return None
    ret = self.root.val
    val = super(BHeap, self).extract()
    if self.root is not None:
      self.root.val = val
      self.reorder()
    return ret

class BST(BTree):
  def __init__(self, l = None):
    self.root = None

    if isinstance(l, list):
      l.sort()
      self.root = self.createMinTree(l, 0, len(l)-1)

  def insert(self, val):
    pass

  def createMinTree(self, arr, l_idx, r_idx):
    mid_idx = l_idx + (r_idx - l_idx + 1) / 2

    node = Node()
    node.setValue(arr[mid_idx])

    if(l_idx != r_idx):
      l_node = self.createMinTree(arr, l_idx, mid_idx-1)
      node.setLeft(l_node)
      if(r_idx - l_idx > 1):
        r_node = self.createMinTree(arr, mid_idx+1, r_idx)
        node.setRight(r_node)

    return node

#from random import shuffle
#
#if __name__ == "__main__":
#  #tree = BTree()
#  #tree.insert(0)
#  #tree.insert(1)
#  #tree.insert(2)
#  #tree.insert(3)
#  #tree.insert(4)
#  #tree.insert(5)
#  #tree.insert(6)
#  INPUT = [i for i in range(10)]
#  shuffle(INPUT)
#
#  print INPUT
#  tree = BTree(INPUT)
#  print 'DFS', tree.DFS()
#  print 'BFS', tree.BFS()
#
#  for e in tree:
#    print e,
#  print ''
#
#  heap = BHeap(INPUT)
#  print 'DFS', heap.DFS()
#  print 'BFS', heap.BFS()
#  for e in heap:
#    print e,
#  print ''
