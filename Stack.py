class Node:
    def __init__(self, data):
        self.__data = data
        self.__prev = None


class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        return self.__top == None

