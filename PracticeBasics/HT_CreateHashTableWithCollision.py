"""
Implement hash table which can handle collision
"""

class Hashtable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def print(self):
        for i in range(self.MAX):
            print(self.arr[i])

    def get_hash(self, key):
        h = 0
        for ch in key:
            h += ord(ch)

        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                return

        self.arr[h].append((key, value))


    def __getitem__(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]


if __name__ == '__main__':
    ht = Hashtable()
    print(ht.get_hash('Jan 14'))
    print(ht.get_hash('Jun 02'))
    print(ht.get_hash('Dec 30'))
    print(ht.get_hash('Jun 07'))
    print(ht.get_hash('Nov 01'))
    ht.print()
    ht['Jan 14'] = 1985
    ht['Jun 02'] = 2019
    ht['Jun 07'] = 2022
    ht['Nov 01'] = 2012
    ht['Jun 07'] = 2020
    ht.print()
    print(ht['Jan 14'])
    print(ht['Nov 01'])
    print(ht['Jun 07'])
    print(ht['May 31'])
    del ht['Jan 14']
    del ht['Jun 07']
    del ht['Nov 01']
    ht.print()
    ht['Nov 01'] = 2011
    ht['Nov 01'] = 2012
    ht.print()
else:
    print("Imported module ", __name__)

