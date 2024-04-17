import Stack as s
class BrowserHistory:

    def __init__(self):
        """
        Конструктор класса BrowserHistory
        """

        self.__history_stack = s.Stack()
        self.__current_index = 0

    def visit(self, url: str):
        """
        Создаёт объект с текущим временем и добавляет его в стэк
        :return: None
        """

    def back(self) -> object:
        """
        Возвращает предыдущий оюъект из истории
        :return: Объект
        """
        if self.__current_index == 0:
            return -1


    def forward(self) -> object:
        """
        Возвращает следующий объект в истории
        :return: объект
        """
        pass

    def clear(self) -> None:
        """
        Очищает историю просмотра страниц
        """
        pass

    def all(self) -> str:
        """
        Возвращает исттрию просмотра страниц
        :return: Возвращает форматированную строку
        """
        pass


    def exit(self):
        pass



































