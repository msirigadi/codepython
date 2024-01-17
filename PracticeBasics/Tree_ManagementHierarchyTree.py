"""
Below is the management hierarchy of a company.

Nilupul (CEO)
    |__Chinmay (CTO)
        |__Vishwa (Infrastructure Head)
            |__Dhaval (Cloud Manager)
            |__Abhijit (App Manager)
        |__Aamir (Application Head)
    |__Gels (HR Head)
        |__Peter (Recruitment Manager)
        |__Waqas (Policy Manager)

Extent tree class built in our main tutorial so that it takes name and designation
in data part of TreeNode class. Now extend print_tree function such that it can print
either name tree, designation tree or name and designation tree. As shown below,


Here is how your main function should will look like,

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy

"""

class TreeNode:
    def __init__(self, name, designation):
        self.data = (name, designation)
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
    def print_tree(self, filter):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        if filter == "name":
            print(prefix + self.data[0])
        elif filter == "designation":
            print(prefix + self.data[1])
        else:
            print(prefix + self.data[0] + " (" + self.data[1] + ")")

        if self.children:
            for child in self.children:
                child.print_tree(filter)


def build_management_tree():
    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")

    ih = TreeNode("Vishwa", "Infrastructure Head")
    ih.add_child(TreeNode("Dhaval", "Cloud Manager"))
    ih.add_child(TreeNode("Abhijit", "App Manager"))

    ah = TreeNode("Aamir", "Application Head")

    cto.add_child(ih)
    cto.add_child(ah)

    hrh = TreeNode("Gels", "HR Head")
    hrh.add_child(TreeNode("Peter", "Recruitment Manager"))
    hrh.add_child(TreeNode("Waqas", "Policy Manager"))

    root.add_child(cto)
    root.add_child(hrh)

    return root

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
