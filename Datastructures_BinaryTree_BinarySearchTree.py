"""
Implement binary search tree
"""

class BinarySearchNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchNode(data)

    def inorder_traversal(self):
        elements = []

        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def preorder_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.preorder_traversal()

        if self.right:
            elements += self.right.preorder_traversal()

        return elements

    def postorder_traversal(self):
        elements = []

        if self.left:
            elements += self.left.postorder_traversal()

        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data)

        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        elements = self.inorder_traversal()
        return sum(elements)

    def search(self, val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = BinarySearchNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    root_node = build_tree(numbers)
    print(root_node.inorder_traversal())
    print(root_node.inorder_traversal())
    print(root_node.postorder_traversal())
    print("{} in Binary tree? {}".format(20, root_node.search(20)))
    print("{} in Binary tree? {}".format(51, root_node.search(51)))
    print("{} in Binary tree? {}".format(14, root_node.search(14)))
    print("Min element in tree:", root_node.find_min())
    print("Max element in tree:", root_node.find_max())
    print("Sum of element in tree:", root_node.calculate_sum())