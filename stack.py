class Node:
    def __init__(self, data):
        self.__data = data
        self.__prev = None

class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, item: any) -> None:
        """
        Добавление элемента в коллекцию
        :param item: Элемент, который желаете добавить
        :type item: any
        :return: None
        """

        new_node = Node(item)
        new_node.__prev = self.__top
        self.__top = new_node

        self.__size += 1

    def pop(self) -> None or any:
        """
        Удаляет и возвращает последний элемент в коллекции
        :return: Элемент или None
        """

        if self.__size == 0:
            return None

        data = self.__top.__data
        self.__top = self.__top.__prev
        self.__size -= 1

        return data

    def peek(self) -> None or any:
        """
        Возвращает последний добавленный элемент в коллекцию
        :return: Элемент или None
        """
        return self.__top.__data if self.__size != 0 else None

    def is_empty(self) -> bool:
        """
        Проверка коллекции на пустоту
        :return: False - если коллекция пуста
                 True - если коллекция имеет элементы
        """
        
        return self.__top is not None


