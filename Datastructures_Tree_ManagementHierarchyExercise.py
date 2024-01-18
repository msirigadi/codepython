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

Extent tree class built in our main tutorial so that it takes name
and designation in data part of TreeNode class. Now extend print_tree
function such that it can print either name tree, designation tree or
name and designation tree. As shown below,

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

    def print_tree(self, option):
        spaces = " " * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""

        if option == 'name':
            print(prefix + self.data[0])
        elif option == 'designation':
            print(prefix + self.data[1])
        elif option == 'both':
            print(prefix + self.data[0] + "  ({})".format(self.data[1]))

        if self.children:
            for child in self.children:
                child.print_tree(option)

def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vishwa","Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels","HR Head")

    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy