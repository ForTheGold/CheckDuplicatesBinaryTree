class Node:

	# --- Binary tree node --- #
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	# --- Insert the data --- #
	def insert(self, data):
		if self.data:
			# --- Insert on the left if the value is smaller than the current value --- #
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)

			 # --- Insert on the right if the value is greater than the current value --- #
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)

		# --- Insert in the current node if it is empty --- #
		else:
			self.data = data

	# --- Print tree by levels --- #
	def printtree(self):
		# --- Keep track of the values in the current level --- #
		cur_level = [self]
		while cur_level:

			# --- Print all the values in a certain level on one line --- #
			print(' '.join(str(node.data) for node in cur_level))

			# --- Keep track of the next level values --- #
			next_level = list()
			for node in cur_level:
				if node.left:
				    next_level.append(node.left)
				if node.right:
				    next_level.append(node.right)

				# --- Move down to the next level --- #
				cur_level = next_level


def identicaltree(root1, root2):
	# --- If there is no tree, then we return true --- #
	if root1 is None and root2 is None:
		return True
	# --- If there is a tree check if the nodes are the same, and recursively walk down the tree --- #
	if root1 is not None and root2 is not None:
		return ((root1.data == root2.data) and identicaltree(root1.left, root2.left) and identicaltree(root1.right, root2.right))
	# --- If there are extra nodes or the data is different return False --- #
	return False



print("Hello, I am a computer program that will insert whatever values you give me into a binary tree.")
print("Two binary trees actually, but let's go one at a time.  We can start with the first tree.")
firsttree = input("Please enter the values that you would like inserted into the first tree separated by spaces: ").split()

try:
	tree1 = Node(firsttree[0])
	for i in range(len(firsttree)):
		tree1.insert(firsttree[i])
except:
	print("Please insert a value!")

print("I have made the first tree for you.  I will start on the second one entering the values in the same way.")
secondtree = input("Please enter the values that you would like inserted into the second tree separated by spaces: ").split()

try:
	tree2 = Node(secondtree[0])
	for i in range(len(secondtree)):
		tree2.insert(secondtree[i])
except:
	print("Please insert a value!")

print("I will now test whether or not the two trees are identical to eachother.  I can show you how I chose to store the trees.")
print("Would you like me print the two trees?")
printtrees = input("Type y for yes and n for no: ")
# --- If you entered the same values in a different order, the program may have stored them in a different way --- #
# --- For this reason, it may (and likely will) return False.  You can check how the program stored the values here --- #
if "y" in printtrees:
	tree1.printtree()
	tree2.printtree()
print("Are your trees identical?", identicaltree(tree1, tree2))


