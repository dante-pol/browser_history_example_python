import datetime

import Stack as s
import datetime



class BrowserHistory:
    class HistoryItem:
        def __init__(self, url: str, datetime: datetime):
            self.url = url
            self.datetime = datetime

    def __init__(self):
        """
        Конструктор класса BrowserHistory
        """

        self.__history_stack = s.Stack()
        self.__history_stack_active = s.Stack()
        self.__current_index = 0

    class HistoryItem:

        def __init__(self, url, datetime):
            self.url = url
            self.datetime = datetime

    def visit(self, url: str):
        """
        Создаёт объект с текущим временем и добавляет его в стэк
        :return: None
        """
        import datetime
        item = BrowserHistory.HistoryItem(url, datetime.datetime.now())
        self.__history_stack.push(item)
        self.__current_index += 1


    def back(self) -> object:
        """
        Возвращает предыдущий объект из истории
        :return: Объект
        """
        if self.__current_index == 0:
            return -1


        buff1 = self.__history_stack.pop()
        self.__history_stack_active.push(buff1)

        return buff1





    def forward(self) -> object:
        """
        Возвращает следующий объект в истории
        :return: объект
        """
        buff = self.__history_stack_active.pop()
        self.__history_stack.push(buff)

        return buff



    def clear(self) -> None:
        pass




    def all(self) -> str:
        """
        Возвращает исттрию просмотра страниц
        :return: Возвращает форматированную строку
        """
        pass


    def exit(self):
        pass



































