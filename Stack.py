class Node:
    def __init__(self, data):
        self.__data = data
        self.prev = None


class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self,item):
        pass

    def pop(self):
        pass

    def peek(self):
        return self.__top != None

    def is_empty(self):
        return self.__top == None


