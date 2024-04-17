class Node:
    def __init__(self, data):
        self.data = data
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
        if self.__size == 0: return None

        data = self.__top.data
        self.__top = self.__top.prev
        self.__size -= 1

        return data

    def peek(self):
        if self.__size != 0:
            return self.__top.data
        else:
            return

    def is_empty(self):
        return self.__top == None


