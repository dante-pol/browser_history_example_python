class Node:
    def __init__(self, data):
        self.__data = data
        self.prev = None


class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self,item):
        node = Node(item)
        node.prev = self.__top
        self.__top = node
        self.__size += 1

    def pop(self):
        pass

    def peek(self):
        return self.__top != None

    def is_empty(self):
        return self.__top == None


s1 = Stack()
s1.push(1)
print(s1.is_empty())
print(s1.peek())