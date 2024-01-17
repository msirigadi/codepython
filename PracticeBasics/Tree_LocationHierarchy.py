"""
Build below location tree using TreeNode class

Global
    |__India
        |__Gujarat
            |__Ahmedabad
            |__Baroda
        |__Karnataka
            |__Bangluru
            |__Mysore
    |__USA
        |__New Jersey
            |__Princeton
            |__Trenton
        |__California
            |__San Francisco
            |__Mountain View
            |__Palo Alto
￼
Now modify print_tree method to take tree level as input.
And that should print tree only upto that level as shown below,
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, level):
        node_level = self.get_level()

        if node_level > level:
            return

        spaces = " " * node_level * 3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree(level)


def build_location_tree():
    root_node = TreeNode("Global")

    ind = TreeNode("India")

    guj = TreeNode("Gujarat")
    guj.add_child(TreeNode("Ahmedabad"))
    guj.add_child(TreeNode("Baroda"))

    kar = TreeNode("Karnataka")
    kar.add_child(TreeNode("Bangluru"))
    kar.add_child(TreeNode("Mysore"))

    ind.add_child(guj)
    ind.add_child(kar)

    usa = TreeNode("USA")
    njy = TreeNode("New Jersey")
    njy.add_child(TreeNode("Princeton"))
    njy.add_child(TreeNode("Trenton"))

    cal = TreeNode("California")
    cal.add_child(TreeNode("San Francisco"))
    cal.add_child(TreeNode("Mountain View"))
    cal.add_child(TreeNode("Palo Alto"))

    usa.add_child(njy)
    usa.add_child(cal)

    root_node.add_child(ind)
    root_node.add_child(usa)

    return root_node

if __name__ == "__main__":
    root_node = build_location_tree()
    #root_node.print_tree()
    root_node.print_tree(1)
    root_node.print_tree(2)
    root_node.print_tree(3)