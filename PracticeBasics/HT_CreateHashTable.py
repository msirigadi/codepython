"""
Implement python dictionary using hash tables
"""

class HashTable:
    def __init__(self, size = 10):
        self.MAX = size
        self.arr = [None for i in range(self.MAX)]

    def print(self):
        for i in range(self.MAX):
            print(self.arr[i])

    def __str__(self):
        return "Created List with size {}".format(self.MAX)

    def get_hash(self, key):
        hash_val = 0

        for ch in key:
            hash_val += ord(ch)

        return hash_val % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

    def add_item(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get_item(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def del_item(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == '__main__':
    ht = HashTable(100)
    #ht.print()
    print(ht)
    print(dir(ht))
    print("-----Adding item-------")
    ht['Jan 14'] = 1985
    ht['Jun 02'] = 2019
    ht['Dec 30'] = 1984
    ht.print()
    print("------Getting item-------")
    print(ht['Jan 14'])
    print(ht['Dec 30'])
    print("-------Deleting item------")
    del ht['Jan 14']
    del ht['Dec 30']
    ht.print()
    print("------Replacing item-------")
    ht['Jun 07'] = 2022
    ht['Nov 01'] = 2012
    ht.print()
    """
    print(ht.get_hash('Jan 14'))
    print(ht.get_hash('Jun 02'))
    print(ht.get_hash('Dec 30'))
    print(ht.get_hash('mar 9'))
    print(ht.get_hash('Nov 01'))
    print(ht.get_hash('Jun 07'))
    print("Adding item")
    ht.add_item('Jan 14', 1985)
    ht.add_item('Jun 02', 2019)
    ht.add_item('Dec 30', 1984)
    ht.add_item('Nov 01', 2012)
    ht.add_item('Jun 07', 2020)
    ht.print()
    print(ht.get_item('Jan 14'))
    print(ht.get_item('Jun 02'))
    ht.del_item('Jan 14')
    ht.del_item('Dec 30')
    ht.print()
    """
