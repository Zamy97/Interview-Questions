class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        print(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data == item:
                found = True
            else:
                previous = current
                current= current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        temp = Node(item)
        temp.set_next(current.get_next())
        current.set_next(temp)

    def insert(self, at_index, item):
        """insert an item after index item"""
        current = self.head
        for i in range(at_index):
            current = self.get_next()

        if current != None:
            temp = Node(item)
            temp.set_next(current.get_next())
            current.set_next(temp)
        else:
            raise("index out of range")

    def pop(self, index):
        self.remove(self.get_item(index))

    def get_item(self, index):
        """return an item given an index"""
        current = self.head
        for i in range(index):
            current = current.getNext()
        if current != None:
            return current.getData()
        else:
            raise ("index out of range")

    def get_index(self, item):
        """get the index of an item, assume the first one (head pointing to) is 0"""
        index = 0
        current = self.head
        found = False
        while current != None:
            if current.get_data() == item:
                found = True
                break
            else:
                current = current.get_next()
                index += 1
        if not found:
            index = None
        return index

    def printig_LL(self):
        result_list = []
        current = self.head
        while current:
            result_list.append(current.get_data())
            current = current.get_next()
        print(result_list)










linked_list_test = LinkedList()

linked_list_test.add(5)
linked_list_test.add(4)
linked_list_test.add(3)
linked_list_test.add(2)
linked_list_test.add(1)


linked_list_test.middle()


