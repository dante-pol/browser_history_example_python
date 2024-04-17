
class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0

    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None

    def push(self, item: any) -> None:
        """
        Данная функция добавляет ,элемент любого типа данных в класс
        :param item: объект любого типа данных
        :return: None
        """
        node = Stack.Node(item)
        node.prev = self.__top
        self.__top = node
        self.__size += 1

    def pop(self) -> None or any:
        """
        Данная функция удаляет ,верхний элемент класса
        :return: Удаленный элемент, любого типа данных который находился на вверхушке
        """
        if self.__size == 0: return None

        data = self.__top.data
        self.__top = self.__top.prev
        self.__size -= 1

        return data

    def peek(self) -> None or any:
        """
        Данная функция показывает,элемент который находится на вверху
        :return: None либо элемент ,любого типа данных
        """
        if self.__size != 0:
            return self.__top.data
        else:
            return

    def is_empty(self) -> bool:
        """
        Данная функция проверяет класс на пустоту
        :return:True если элемента в классе нет,False если есть
        """
        return self.__top == None
