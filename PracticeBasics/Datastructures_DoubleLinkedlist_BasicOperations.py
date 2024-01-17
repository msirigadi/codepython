"""
Implement double linked list
"""

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = self.last = Node(data, self.head, None)
        else:
            newnode = Node(data, self.head, None)
            self.head.prev = newnode
            self.head = newnode

    def insert_at_end(self, data):
        if self.head is None:
            self.head = self.last = Node(data)
        else:
            newnode = Node(data, None, self.last)
            self.last.next = newnode
            self.last = newnode

    def get_length(self):
        itr = self.head
        cnt = 0

        while itr:
            itr = itr.next
            cnt += 1

        return cnt
    def print_forward(self):
        itr = self.head
        dllstr = ""
        while itr:
            dllstr += str(itr.data) + '--->'
            itr = itr.next

        print(dllstr)

    def print_backward(self):
        itr = self.last
        dllstr = ""
        while itr:
            dllstr += str(itr.data) + '--->'
            itr = itr.prev

        print(dllstr)

    def insert_values(self, data_list):
        self.head = self.last = None

        for data in data_list:
            self.insert_at_beginning(data)


    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if self.head is None:
            return

        itr = self.head
        if index == 0:
            itr.next.prev = None
            self.head = itr.next
            itr.next = None
            return

        cnt = 0
        while itr:
            if cnt == index:
                cur = itr
                prev = itr.prev
                prev.next = itr.next
                if cur.next:
                    cur.next.prev = prev
                else:
                    self.last = prev
                cur.next = cur.prev = None
                break

            itr = itr.next
            cnt += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            newnode = Node(data, self.head, None)
            self.head.prev = newnode
            self.head = newnode
            return

        itr = self.head
        cnt = 0
        while itr:
            if cnt == index - 1:
                newnode = Node(data, itr.next, itr)
                itr.next.prev = newnode
                itr.next = newnode
                break
            itr = itr.next
            cnt += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head

        while itr:
            if itr.data == data_after:
                newnode = Node(data_to_insert, itr.next, itr)
                if itr.next:
                    itr.next.prev = newnode
                else:
                    self.last = newnode
                itr.next = newnode
                break
            itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        if itr.data == data:
            if itr.next:
                itr.next.prev = None
                self.head = itr.next
                itr.next = None
                return
            else:
                self.head = None

        while itr:
            if itr.data == data:
                if itr.next:
                    itr.next.prev = itr.prev
                    itr.prev.next = itr.next
                    itr.prev = itr.next = None
                    break
                else:
                    itr.prev.next = itr.next
                    self.last = itr.prev
                    itr.prev = None
                    break

            itr = itr.next


if __name__ == '__main__':
    dll = DoubleLinkedList()
    """
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(30)
    dll.insert_at_beginning('Mahi')
    """
    dll.insert_at_end('Math')
    dll.insert_at_end('Social')
    dll.insert_at_end('Science')
    dll.insert_at_end('History')
    dll.print_forward()
    dll.print_backward()
    print("Length of double linked list is", dll.get_length())
    dll.insert_values(['Bananas', 'Apples', 'Berries', 'Mangoes', 'Watermelon'])
    dll.print_forward()
    dll.print_backward()
    dll.remove_at(0)
    dll.print_forward()
    dll.print_backward()
    dll.remove_at(2)
    dll.print_forward()
    dll.print_backward()
    dll.remove_at(2)
    dll.print_forward()
    dll.print_backward()
    dll.insert_at(0, 'Jackfruit')
    dll.print_forward()
    dll.print_backward()
    dll.insert_at(2, 'Kiwis')
    dll.print_forward()
    dll.print_backward()
    dll.insert_after_value('Jackfruit', 'CustardApples')
    dll.print_forward()
    dll.print_backward()
    dll.insert_after_value('Mangoes', 'Grapes')
    dll.print_forward()
    dll.print_backward()
    dll.insert_after_value('Berries', 'Pineapple')
    dll.print_forward()
    dll.print_backward()
    dll.remove_by_value('Pineapple')
    dll.print_forward()
    dll.print_backward()
    dll.remove_by_value('Jackfruit')
    dll.print_forward()
    dll.print_backward()
    dll.remove_by_value('Grapes')
    dll.print_forward()
    dll.print_backward()