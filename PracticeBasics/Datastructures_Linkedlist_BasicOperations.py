"""
Implement linked list
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

    def print_list(self):
        itr = self.head

        strg = ""
        while itr:
            strg += str(itr.data) + '--->'
            itr = itr.next

        print(strg)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

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
            self.head = self.head.next
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr .next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Exception")

        if index == 0:
            self.head = Node(data, self.head)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head

        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head

        if not itr:
            return

        if itr.data == data:
            self.head = itr.next
            return

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.print_list()
    ll.insert_at_beginning(20)
    ll.print_list()
    ll.insert_at_beginning('Mahi')
    ll.print_list()
    ll.insert_at_end(20)
    ll.print_list()
    ll.insert_at_end(30)
    ll.print_list()
    ll.insert_at_end("Mahi")
    ll.print_list()
    print("Length of list =", ll.get_length())
    ll.insert_values(['Bananas', 'Mangoes', 'Berries', 'Oranges', 'Melons'])
    ll.print_list()
    print("Length of list =", ll.get_length())
    ll.remove_at(2)
    ll.print_list()
    ll.remove_at(3)
    ll.print_list()
    ll.insert_at(2, 'Figs')
    ll.print_list()
    ll.insert_at(0, 'Dates')
    ll.print_list()
    ll.insert_after_value('Dates', 'Plums')
    ll.print_list()
    ll.insert_after_value('Oranges', 'Prunes')
    ll.print_list()
    ll.insert_after_value('Bananas', 10)
    ll.print_list()
    ll.remove_by_value('Dates')
    ll.print_list()
    ll.remove_by_value('Prunes')
    ll.print_list()
    ll.remove_by_value(10)
    ll.print_list()
