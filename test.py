from LinkedList import LinkedList
from Stack import Stack

l = LinkedList()
l.append("2")
l.append("3")
l.append("4")
print(l.return_as_list())
print(l.get_tail_value())
l.append("5")
l.remove("3")
print(l.get_head_value())
print(l.get_tail_value())
print(l.get_head_value())
print(l.return_as_list())
l.append_to_front("1")
print(l.return_as_list())
print(l.get_head_value())
l.remove("4")
l.append_to_tail("7")
print(l.return_as_list())
print(l.get_tail_value())
print("------------------")
l2 = LinkedList()
l2.append(1)
l2.append(2)
l2.append(3)
print(l2.return_as_list())
print(l2.size)
l2.append_to_front(0)
l2.append_to_front(-1)
print(l2.return_as_list())
l2.remove(2)
l2.remove(-1)
print(l2.return_as_list())
print(l2.size)
# stack = Stack()
# stack.add(1)
# stack.add(2)
# print(stack.peek())
# print(stack.pop())
# print(stack.peek())