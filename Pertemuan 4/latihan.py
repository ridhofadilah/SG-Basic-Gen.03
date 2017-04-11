class Node:
	def __init__(self,val):
		self.info = val
		self.left = None
		self.right = None

	def insert(self, val):
		if (val < self.info) :
			if self.left is None :
				self.left = Node(val)
			else:
				self.left.insert(val)
		elif (val > self.info):
			if self.right is None:
				self.right = Node(val)
			else:
				self.right.insert(val)
	
	def inOrder(self):
		if self.left :
			self.left.inOrder()
		print (self.info, end=" - ") 
		if self.right:
			self.right.inOrder()

	def preOrder(self):
		print (self.info , end = " - ")
		if self.left :
			self.left.preOrder()
		if self.right :
			self.right.preOrder()

	def postOrder(self):
		if self.left :
			self.left.postOrder()
		if self.right :
			self.right.postOrder()
		print (self.info , end = " - ")

	def Search(self, val):
		if self.info > val :
			if self.left :
				return self.left.Search(val)
			else :
				return False
		elif (self.info < val):
			if self.right :
				return self.right.Search(val)
			else :
				return False
		elif (self.info == val) :
			return True

	def height(self):
		if self.left is None or self.right is None :
			return 0
		u = self.left.height()
		v = self.right.height()
		if (u > v) :
			return u + 1
		else :
			return v + 1

	def levelOrder(self,x):
		counter = 0
		for i in x :
			if (self.info == i):
				counter += 1
		if counter == 0:
			x.append(self.info)
		if self.left :
			self.left.levelOrder(x)
		if self.right :
			self.right.levelOrder(x)

BT = Node(23)
BT.insert(10)
BT.insert(16)
BT.insert(19)
BT.insert(65)
BT.insert(45)
BT.insert(24)
BT.insert(50)
BT.insert(67)
print ("inOrder =", end = " ")
BT.inOrder()
print()
print ("preOrder =", end = " ")
BT.preOrder()
print ()
print ("postOrder =", end = " ")
BT.postOrder()
print ()
print (BT.Search(19))
print (BT.height())
x = []
BT.levelOrder(x)
for i in x :
	print (i)