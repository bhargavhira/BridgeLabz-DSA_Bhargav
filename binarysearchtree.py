class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
            return
        self._insert(self.root, data)
    
    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(node.right, data)
    
    def delete(self, data):
        self.root = self._delete(self.root, data)
    
    def _delete(self, node, data):
        if not node:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            temp = self._min_value(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
        return node
    
    def _min_value(self, node):
        while node.left:
            node = node.left
        return node
    
    def get(self, data):
        return self._get(self.root, data)
    
    def _get(self, node, data):
        if not node or node.data == data:
            return node
        if data < node.data:
            return self._get(node.left, data)
        return self._get(node.right, data)
    
    def update(self, old_data, new_data):
        self.delete(old_data)
        self.insert(new_data)
    
    def is_empty(self):
        return self.root is None
    
    def total_elements(self):
        return self._count_nodes(self.root)
    
    def _count_nodes(self, node):
        if not node:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)
    
    def inorder(self):
        self._inorder(self.root)
        print()
    
    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data, end="  ")
            self._inorder(node.right)

bst = BST()
nums = [50, 30, 70, 20, 40, 60, 80]
for num in nums:
    bst.insert(num)

bst.inorder()
print("Total Elements:", bst.total_elements())

bst.update(40, 45)
bst.inorder()
print("Total Elements:", bst.total_elements())

bst.delete(30)
bst.inorder()
print("Total Elements:", bst.total_elements())

print("Is BST empty?", bst.is_empty())
print("Search 60:", "Found" if bst.get(60) else "Not Found")
print("Search 100:", "Found" if bst.get(100) else "Not Found")
