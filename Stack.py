class Stack():
    def __init__(self):
        self.s_list = []
    def add(self, value):
        self.s_list.append(value)
    def pop(self):
        if len(self.s_list) != 0:
            top_of_stack = self.s_list[-1]
            del self.s_list[-1]
            return top_of_stack
        else:
            return 0
    def peek(self):
        return self.s_list[-1]
    def clear(self):
        self.s_list = []

    def size(self):
        return len(self.s_list)

    def as_list(self):
        return self.s_list

    def reverse_stack(self):
        temp = []
        for i in range(len(self.s_list)-1, -1, -1):
            temp.append(self.s_list[i])

        self.s_list = temp
