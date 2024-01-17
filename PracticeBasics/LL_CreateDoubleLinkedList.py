"""
Implement Double linked list
"""

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
            return

        newnode = Node(data, self.head)
        self.head.prev = newnode
        self.head = newnode

    def insert_at_end(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
            return

        newnode = Node(data, None, self.tail)
        self.tail.next = newnode
        self.tail = newnode

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_beginning(data)

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                nextnode = itr.next
                newnode = Node(data, nextnode, itr)
                itr.next = newnode
                nextnode.prev = newnode
                break

            itr = itr.next
            count += 1


    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head

        while itr:
            if itr.data == data_after:
                nextnode = itr.next
                newnode = Node(data_to_insert, nextnode, itr)
                if nextnode:
                    nextnode.prev = newnode
                else:
                    self.tail = newnode

                itr.next = newnode
                break

            itr = itr.next

    def get_length(self):
        itr = self.head
        count = 0

        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            curnode = self.head
            nextnode = curnode.next
            curnode.next = nextnode.prev = None
            self.head = nextnode
            return

        if index == self.get_length() - 1:
            curnode = self.tail
            prevnode = self.tail.prev
            prevnode.next = curnode.next
            curnode.next = curnode.prev = None
            self.tail = prevnode
            return

        itr = self.head
        count = 0
        while itr:
            if count == index:
                nextnode = itr.next
                prevnode = itr.prev
                prevnode.next = nextnode
                nextnode.prev = prevnode
                itr.next = itr.prev = None
                break

            count += 1
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        while itr:
            if itr.data == data:
                if itr == self.head:
                    nextnode = itr.next
                    nextnode.prev = None
                    self.head = nextnode
                    itr.next = itr.prev = None
                    break
                elif itr == self.tail:
                    prevnode = itr.prev
                    prevnode.next = None
                    itr.next = itr.prev = None
                    self.tail = prevnode
                    break
                else:
                    prevnode = itr.prev
                    nextnode = itr.next
                    prevnode.next = nextnode
                    nextnode.prev = prevnode
                    itr.next = itr.prev = None
                    break

            itr = itr.next

    def print_forward(self):
        itr = self.head
        dll_str = ""

        while itr:
            dll_str += str(itr.data) + '--->'
            itr = itr.next

        return  dll_str

    def print_backward(self):
        itr = self.tail
        dll_str = ""

        while itr:
            dll_str += str(itr.data) + '--->'
            itr = itr.prev

        return dll_str


if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insert_at_end("SRINU")
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning('MAHI')
    dll.insert_at_end(30)
    dll.insert_at_end('ATHARV SOMISETTY')
    dll.insert_values(['Apples', 'Bananas', 'Melons'])
    dll.insert_at(0, 'Roses')
    dll.insert_at(9, 'Jasmine')
    dll.insert_after_value('ATHARV SOMISETTY', 'Hibiscus')
    dll.insert_after_value('Roses', 'Lillies')
    dll.insert_after_value('Apples', 'Peaches')
    dll.remove_at(0)
    dll.remove_at(12)
    dll.remove_at(7)
    dll.remove_by_value('Lillies')
    dll.remove_by_value('ATHARV SOMISETTY')
    dll.remove_by_value('Peaches')
    print(dll.print_forward())
    print(dll.print_backward())
    print("Length of list = ", dll.get_length())
