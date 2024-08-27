class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def has_next(self):
        if self.next is not None:
            return True
        return False
    def has_prev(self):
        if self.prev is not None:
            return True
        return False
class DoublyLinkedList():
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.size = 0

    def append(self, item):
        if self.head.value is not None:
            current_node = self.head
            while current_node.has_next():
                current_node = current_node.next
            new_node = Node(item)
            current_node.next = new_node
            new_node.prev = current_node
            self.tail = new_node
        else:
            self.head = Node(item)
            self.tail = self.head
        self.size += 1

    def contains(self, item):
        if self.head.value == item:
            return True
        else:
            current_node = self.head
            while current_node.has_next():
                if current_node.value == item:
                    return True
                current_node = current_node.next
            return False

    def remove(self, item):
        if self.head.value == item:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        elif self.tail.value == item:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1

        elif self.head.value != item and self.tail.value != item:
            temp = self.head
            next_node = self.head.next
            while temp.has_next():
                if next_node.value == item:
                    self.size -= 1
                    temp.next = next_node.next
                    next_next_node = next_node.next
                    next_next_node.prev = temp
                    return;
                temp = next_node
                next_node = temp.next
        else:
            print(f"value: {item} doesn't exist")



    def return_as_list(self):
        l = []
        temp = self.head
        while temp.has_next():
            l.append(temp.value)
            temp = temp.next
        l.append(temp.value)
        return l

    def get_head_value(self):
        return self.head.value

    def get_tail_value(self):
        return self.tail.value

    def append_to_front(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size+=1

    def append_to_tail(self, item):
        new_node = Node(item)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def remove_first_object(self):
        if self.head.next != None:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1

    def remove_last_object(self):
        if self.tail != None and self.tail.prev != None:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1







