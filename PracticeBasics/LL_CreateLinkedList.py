"""
Create Linked list
"""

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, self.head)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_beginning(data)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head

        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next
    def print(self):
        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def remove_at(self, index):
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while count < index - 1:
            itr = itr.next
            count += 1

        itr.next = itr.next.next

    def remove_by_value(self, data):
        itr = self.head
        if itr.data == data:
            self.head = itr.next
            return

        while itr:
            if itr.next:
                if itr.next.data == data:
                    itr.next = itr.next.next
                    break

            itr = itr.next
    def get_length(self):
        len = 0
        itr = self.head

        while itr:
            itr = itr.next
            len += 1

        return len

"""
ll = LinkedList()
ll.insert_at_end(1)
ll.print()
ll.insert_at_beginning(10)
ll.print()
ll.insert_at_beginning(30)
ll.print()
ll.insert_at_beginning(50)
ll.print()
ll.insert_at_end(70)
ll.print()
ll.insert_at_end(90)
ll.print()
ll.insert_values(['Mahi', 'Cnu'])
ll.print()
ll.remove_at(1)
ll.print()
ll.remove_at(0)
ll.print()
ll.remove_at(5)
ll.print()
print("Length of linked list: ", ll.get_length())
ll.insert_at(0, 'Nuts')
ll.print()
ll.insert_at(3, 'Icecream')
ll.print()
ll.insert_at(6, 'Snacks')
ll.print()
"""

if __name__ == '__main__':
    """
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()
    """
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    print(ll.get_length())
    ll.print()