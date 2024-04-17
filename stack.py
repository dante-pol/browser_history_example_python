class Node:
    def __init__(self, data):
        self.__data = data
        self.__prev = None

class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, item: any):
        new_node = Node(item)
        new_node.__prev = self.__top
        self.__top = new_node

        self.__size += 1

    def pop(self):
        if self.__size == 0:
            return None

        data = self.__top.__data
        self.__top = self.__top.__prev
        self.__size -= 1

        return data

    def peek(self):
        return self.__top.__data if self.__size != 0 else None


