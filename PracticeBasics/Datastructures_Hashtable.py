"""
Implement hash table
"""

class Hashtable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def gethash(self, key):
        h = 0
        for ch in key:
            h += ord(ch)

        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.gethash(key)
        self.arr[h] = value

    def __delitem__(self, key):
        h = self.gethash(key)
        self.arr[h] = None

    def __getitem__(self, item):
        h = self.gethash(item)
        return self.arr[h]

"""
    def add(self, key, val):
        h = self.gethash(key)
        self.arr[h] = val

    def remove(self, key):
        h = self.gethash(key)
        self.arr[h] = None
"""

ht = Hashtable()
ht['march 6'] = 120
ht['march 1'] = 90
print(ht.arr)
print(ht['march 1'])
del ht['march 6']
del ht['march 1']
print(ht.arr)
