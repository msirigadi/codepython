"""
General Tree implementation
"""

class Treenode:
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

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = Treenode("Electronics")

    laptop = Treenode("Laptops")
    mac = Treenode("Mac Book")
    hp = Treenode("HP Pavilion")
    dell = Treenode("Dell Inspiron")

    laptop.add_child(mac)
    laptop.add_child(hp)
    laptop.add_child(dell)

    cellphone = Treenode("Cell Phones")
    iphone = Treenode("IPhone")
    google = Treenode("Google Pixel")
    nokia = Treenode("Nokia")

    cellphone.add_child(iphone)
    cellphone.add_child(google)
    cellphone.add_child(nokia)

    tv = Treenode("Tvs")
    lg = Treenode("LG")
    samsung = Treenode("Samsung")

    tv.add_child(lg)
    tv.add_child(samsung)

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()