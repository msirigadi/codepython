"""
Implement binary search tree
"""

class BinarySearchTreeNode:
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
                self.left = BinarySearchTreeNode(data)


        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inorder_traversal(self):
        elements = []

        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def search(self, data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False

        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False


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
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right

            #min = self.right.find_min()
            #self.data = min
            #self.right.delete(min)

            max = self.left.find_max()
            self.data = max
            self.left.delete(max)

        return self
def build_tree(elements):
    root_node = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root_node.add_child(elements[i])

    return root_node

if __name__ == "__main__":
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("Inorder traversal for list: ", numbers_tree.inorder_traversal())
    print(numbers_tree.search(5))
    print(numbers_tree.search(20))
    print("Min: ", numbers_tree.find_min())
    print("Max: ", numbers_tree.find_max())
    print("Sum of all elements: ", numbers_tree.calculate_sum())
    print("Preorder traversal for list: ", numbers_tree.pre_order_traversal())
    print("Postorder traversal for list: ", numbers_tree.post_order_traversal())
    numbers_tree.delete(23)
    print("Inorder after deletion: ", numbers_tree.inorder_traversal())
    numbers_tree.delete(17)
    print("Inorder after deletion: ", numbers_tree.inorder_traversal())

