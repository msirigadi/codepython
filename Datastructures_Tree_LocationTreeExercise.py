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

if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(1)
"""
class TreeNode:
    def __init__(self, location):
        self.data = location
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
        level = self.get_level()

        if level > option:
            return

        spaces = " " * level * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree(option)

def build_location_tree():
    guj = TreeNode('Gujarat')
    guj.add_child(TreeNode('Ahmedabad'))
    guj.add_child(TreeNode('Baroda'))

    kar = TreeNode('Karnataka')
    kar.add_child(TreeNode('Bangluru'))
    kar.add_child(TreeNode('Mysore'))

    ind = TreeNode('India')
    ind.add_child(guj)
    ind.add_child(kar)

    nj = TreeNode('New Jersey')
    nj.add_child(TreeNode('Princeton'))
    nj.add_child(TreeNode('Trenton'))

    ca = TreeNode('California')
    ca.add_child(TreeNode('San Francisco'))
    ca.add_child(TreeNode('Mountain View'))
    ca.add_child(TreeNode('Palo Alto'))

    usa = TreeNode('USA')
    usa.add_child(nj)
    usa.add_child(ca)

    gbl = TreeNode('Global')
    gbl.add_child(ind)
    gbl.add_child(usa)

    return gbl

if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(0)
    root_node.print_tree(1)
    root_node.print_tree(2)
    root_node.print_tree(3)



