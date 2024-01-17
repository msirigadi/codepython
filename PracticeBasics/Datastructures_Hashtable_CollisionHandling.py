"""
Implement hashtable with collision domain
"""

class Hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def gethash(self, key):
        h = 0
        for ch in key:
            h += ord(ch)

        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.gethash(key)

        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))

    def __delitem__(self, key):
        h = self.gethash(key)

        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

    def __getitem__(self, key):
        h = self.gethash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

ht = Hashtable()
ht['march 6'] = 120
ht['march 6'] = 78
print(ht.arr)
ht['march 8'] = 67
ht['march 9'] = 4
ht['march 17'] = 459
print(ht.arr)
print(ht['march 17'])
print(ht['march 8'])
del ht['march 17']
print(ht.arr)
del ht['march 6']
print(ht.arr)
