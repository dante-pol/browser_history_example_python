class BrowserHistory:

    def __init__(self, history_stack, current_index):
        """
        Конструктор класса BrowserHistory
        """

        self.__history_stack = history_stack
        self.__current_index = current_index


    def visit(self, url: object):
        """
        Создаёт объект с текущим временем и добавляет его в стэк.
        :return: None
        """
        pass

    def back(self) -> object:
        """
        Возвращает предыдущий оюъект из истории
        :return: Объект
        """
        pass

    def forward(self) -> object:
        """
        Возвращает предыдущий объект в истории
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



































