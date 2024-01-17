µ"""
Implement hash table collision with linear probing
"""
from HT_CreateHashTable import HashTable

class HashTableLP(HashTable):
    def __init__(self):
        super().__init__()

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        for i in range(h, self.MAX):
            if self.arr[i] is None:
                self.arr[i] = value
                return

        for j in range(0, h):
            if self.arr[j] is None:
                self.arr[j] = value
                return

    def get_hash(self, key):
        return key % self.MAX

if __name__ == '__main__':
    ht= HashTableLP()
    ht.print()
    ht[23] = 'Roses'
    ht[11] = 'Lillies'
    ht[99] = 'Jasmine'
    ht[43] = 'Marigold'
    ht[10] = 'Sunflower'
    ht[19] = 'Hibiscus'
    ht[29] = 'Lotus'

    print("-------- Hash table after insertion")
    ht.print()
