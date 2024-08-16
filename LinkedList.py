class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def has_next(self):
        if self.next is not None:
            return True
        return False

class LinkedList():
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

    def append(self, item):
        if self.head.value is not None:
            current_node = self.head
            while current_node.has_next():
                current_node = current_node.next
            current_node.next = Node(item)
            self.tail = current_node.next
        else:
            self.head = Node(item)
            self.tail = self.head

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
        elif self.tail.value == item:
            temp = self.head
            while temp.has_next():
                if temp.next != self.tail:
                    temp = temp.next
                else:
                    temp.next = None
                    self.tail = temp

        elif self.head.value != item and self.tail.value != item:
            temp = self.head
            next_node = self.head.next
            while temp.has_next():
                if next_node.value == item:
                    temp.next = next_node.next
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
        self.head = new_node

    def append_to_tail(self, item):
        new_node = Node(item)
        self.tail.next = new_node
        self.tail = new_node

    def remove_first_object(self):
        if self.head.next != None:
            self.head = self.head.next






