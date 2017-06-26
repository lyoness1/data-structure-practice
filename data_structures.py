# built in lower level: list, string, num, dict, set

class LinkedListNode:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class DoubleyLinkedListNode: 
	def __init__(self, data, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev

class LinkedList: 
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def is_node_in_list(self, node): 
		"""
			>>> node_a = LinkedListNode('a')
			>>> node_b = LinkedListNode('b')
			>>> node_c = LinkedListNode('c')
			>>> node_a.next = node_b
			>>> node_b.next = node_c
			>>> linked_list = LinkedList(node_a)
			>>> linked_list.is_node_in_list(node_c)
			True

		"""
		curr_node = self.head
		while curr_node: 
			if curr_node == node:
				return True
			curr_node = curr_node.next
		
		return False


class Queue: 
	def __init__(self): 
		self.queue = []

	def enqueue(self, data): 
		self.queue.append(data)

	def dequeue(self): 
		return self.queue.pop(0)

	def peek(self): 
		return self.queue[0]

	def is_empty(self): 
		return not self.queue


class Stack: 
	def __init__(self): 
		self.stack = []

	def add(self, data): 
		self.stack.append(data)

	def remove(self): 
		return self.stack.pop(-1)

	def peek(self): 
		return self.stack[-1]

	def is_empty(self):
		return not self.stack


class GraphNode: 
	def __init__(self, data, adjacencies=None):
		self.data = data
		self.adjacencies = adjacencies or set()

	def add_adjacency(self, node):
		self.adjacencies.add(node)

	def add_adjacencies(self, nodes):
		for node in nodes:
			self.adjacencies.add(node)

class Graph:
	def __init__(self, nodes=None): 
		self.nodes = nodes or set()

	def add_node(self, node):
		self.nodes.add(node)

	def add_data_as_node(self, data):
		self.nodes.add(GraphNode(data))

	def are_nodes_connected_iteratively(self, node_1, node_2):
		"""
			>>> node_a = GraphNode('a')
			>>> node_b = GraphNode('b')
			>>> node_c = GraphNode('c')
			>>> node_d = GraphNode('d')
			>>> node_a.add_adjacencies([node_c, node_b])
			>>> node_b.add_adjacencies([node_a, node_c])
			>>> graph = Graph()
			>>> for node in [node_a, node_b, node_c, node_d]:
			...     graph.add_node(node)
			>>> graph.are_nodes_connected_iteratively(node_a, node_c)
			True
			>>> graph.are_nodes_connected_iteratively(node_b, node_d)
			False

		"""
		possible_nodes = Queue()
		possible_nodes.enqueue(node_1)
		seen = set()

		while not possible_nodes.is_empty(): 
			curr_node = possible_nodes.dequeue()
			if curr_node == node_2:
				return True
			seen.add(curr_node)
			possible_adjacencies = curr_node.adjacencies - seen
			for node in possible_adjacencies:
				possible_nodes.enqueue(node)
				
		return False

	def are_nodes_connected_recursively(self, node_1, node_2, seen=None):
		"""
			>>> node_a = GraphNode('a')
			>>> node_b = GraphNode('b')
			>>> node_c = GraphNode('c')
			>>> node_d = GraphNode('d')
			>>> node_a.add_adjacencies([node_c, node_b])
			>>> node_b.add_adjacencies([node_a, node_c])
			>>> graph = Graph()
			>>> for node in [node_a, node_b, node_c, node_d]:
			...     graph.add_node(node)
			>>> graph.are_nodes_connected_recursively(node_a, node_c)
			True
			>>> graph.are_nodes_connected_recursively(node_b, node_d)
			False

		"""
		if node_1 == node_2: 
			return True

		seen = set() if not seen else seen
		seen.add(node_1)

		for node in (node_1.adjacencies - seen):
			if self.are_nodes_connected_recursively(node, node_2, seen):
				return True

		return False


class TreeNode: 
	def __init__(self, data, children=None):
		self.data = data
		self.children = children or []

	def add_child(self, child):
		self.children.append(child)

	def add_data_as_child(self, data):
		self.children.append(TreeNode(data))


class Tree:
	def __init__(self, root=None):
		assert isinstance(root, TreeNode), "Root must be a TreeNode"
		self.root = root

	def is_node_in_tree_bfs_iterative(self, node_to_find):
		"""
			>>> node_a = TreeNode('a')
			>>> node_b = TreeNode('b')
			>>> node_c = TreeNode('c')
			>>> node_d = TreeNode('d')
			>>> node_e = TreeNode('e')
			>>> node_f = TreeNode('f')
			>>> node_a.add_child(node_b)
			>>> node_a.add_child(node_c)
			>>> node_c.add_child(node_d)
			>>> node_c.add_child(node_e)
			>>> tree = Tree(node_a)
			>>> tree.is_node_in_tree_bfs_iterative(node_e)
			True
			>>> tree.is_node_in_tree_bfs_iterative(node_f)
			False

		"""
		to_visit = Queue()
		to_visit.enqueue(self.root)

		while not to_visit.is_empty():
			curr_node = to_visit.dequeue()

			if curr_node == node_to_find: 
				return True

			for node in curr_node.children:
				to_visit.enqueue(node)

		return False

	def is_node_in_tree_dfs_iterateive(self, node_to_find):
		"""
			>>> node_a = TreeNode('a')
			>>> node_b = TreeNode('b')
			>>> node_c = TreeNode('c')
			>>> node_d = TreeNode('d')
			>>> node_e = TreeNode('e')
			>>> node_f = TreeNode('f')
			>>> node_a.add_child(node_b)
			>>> node_a.add_child(node_c)
			>>> node_c.add_child(node_d)
			>>> node_c.add_child(node_e)
			>>> tree = Tree(node_a)
			>>> tree.is_node_in_tree_dfs_iterateive(node_e)
			True
			>>> tree.is_node_in_tree_dfs_iterateive(node_f)
			False

		"""
		to_visit = Stack()
		to_visit.add(self.root)

		while not to_visit.is_empty():
			curr_node = to_visit.remove()
			if curr_node == node_to_find:
				return True
			for node in curr_node.children:
				to_visit.add(node)

		return False

	def is_node_in_tree_recursive(self, node_to_find, curr_node=None):
		"""
			>>> node_a = TreeNode('a')
			>>> node_b = TreeNode('b')
			>>> node_c = TreeNode('c')
			>>> node_d = TreeNode('d')
			>>> node_e = TreeNode('e')
			>>> node_f = TreeNode('f')
			>>> node_a.add_child(node_b)
			>>> node_a.add_child(node_c)
			>>> node_c.add_child(node_d)
			>>> node_c.add_child(node_e)
			>>> tree = Tree(node_a)
			>>> tree.is_node_in_tree_recursive(node_e)
			True
			>>> tree.is_node_in_tree_recursive(node_f)
			False

		"""
		if node_to_find == curr_node:
			return True

		if not curr_node:
			curr_node = self.root

		for node in curr_node.children:
			if self.is_node_in_tree_recursive(node_to_find, node):
				return True

		return False


class BinaryTreeNode:
	def __init__(self, data, right=None, left=None):
		self.data = data
		self.left = left
		self.right = right

	def add_left_child(self, child):
		self.left = child 

	def add_right_child(self, child):
		self.right = child


class BinaryTree:
	def __init__(self, root=None):
		assert isinstance(root, BinaryTreeNode), "Root must be a BinaryTreeNode"
		self.root = root

	def is_node_in_tree_bfs_iterative(self, node_to_find):
		"""
			>>> node_a = BinaryTreeNode('a')
			>>> node_b = BinaryTreeNode('b')
			>>> node_c = BinaryTreeNode('c')
			>>> node_d = BinaryTreeNode('d')
			>>> node_e = BinaryTreeNode('e')
			>>> node_f = BinaryTreeNode('f')
			>>> node_a.add_left_child(node_b)
			>>> node_a.add_right_child(node_c)
			>>> node_c.add_left_child(node_d)
			>>> node_c.add_right_child(node_e)
			>>> tree = BinaryTree(node_a)
			>>> tree.is_node_in_tree_bfs_iterative(node_e)
			True
			>>> tree.is_node_in_tree_bfs_iterative(node_f)
			False

		"""
		to_visit = Queue()
		to_visit.enqueue(self.root)

		while not to_visit.is_empty():
			curr_node = to_visit.dequeue()
			if curr_node == node_to_find:
				return True
			if curr_node.left: 
				to_visit.enqueue(curr_node.left)
			if curr_node.right:
				to_visit.enqueue(curr_node.right)

		return False

	def is_node_in_tree_dfs_iterative(self, node_to_find):
		"""
			>>> node_a = BinaryTreeNode('a')
			>>> node_b = BinaryTreeNode('b')
			>>> node_c = BinaryTreeNode('c')
			>>> node_d = BinaryTreeNode('d')
			>>> node_e = BinaryTreeNode('e')
			>>> node_f = BinaryTreeNode('f')
			>>> node_a.add_left_child(node_b)
			>>> node_a.add_right_child(node_c)
			>>> node_c.add_left_child(node_d)
			>>> node_c.add_right_child(node_e)
			>>> tree = BinaryTree(node_a)
			>>> tree.is_node_in_tree_dfs_iterative(node_e)
			True
			>>> tree.is_node_in_tree_dfs_iterative(node_f)
			False

		"""
		to_visit = Stack()
		to_visit.add(self.root)

		while not to_visit.is_empty():
			curr_node = to_visit.remove()
			if curr_node == node_to_find:
				return True
			if curr_node.left: 
				to_visit.add(curr_node.left)
			if curr_node.right:
				to_visit.add(curr_node.right)

		return False

	def is_node_in_tree_recursive(self, node_to_find, curr_node=None):
		"""
			>>> node_a = BinaryTreeNode('a')
			>>> node_b = BinaryTreeNode('b')
			>>> node_c = BinaryTreeNode('c')
			>>> node_d = BinaryTreeNode('d')
			>>> node_e = BinaryTreeNode('e')
			>>> node_f = BinaryTreeNode('f')
			>>> node_a.add_left_child(node_b)
			>>> node_a.add_right_child(node_c)
			>>> node_c.add_left_child(node_d)
			>>> node_c.add_right_child(node_e)
			>>> tree = BinaryTree(node_a)
			>>> tree.is_node_in_tree_recursive(node_e)
			True
			>>> tree.is_node_in_tree_recursive(node_f)
			False

		"""
		if node_to_find == curr_node:
			return True

		curr_node = curr_node or self.root

		if curr_node.left:
			if self.is_node_in_tree_recursive(node_to_find, curr_node.left):
				return True

		if curr_node.right:
			if self.is_node_in_tree_recursive(node_to_find, curr_node.right):
				return True

		return False



if __name__ == '__main__':
	import doctest
	if doctest.testmod().failed == 0:
		print "\n\nALL TESTS PASSED!!\n\n"


