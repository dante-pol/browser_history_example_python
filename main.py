import stack

class HistoryItem:
    def __init__(self, url, datetime):
        self.__url = url
        self.__datetime = datetime


class BrowserHistory:
    def __init__(self, history_stack):
        self.__history_stack = stack.Stack()
        self.__current_index = 0
        self.__save_stack = stack.Stack()
        self.__save_stack_index = 0

    def visit(self, url):
        import datetime
        item = HistoryItem(url, datetime.datetime.now())
        self.__history_stack.push(item)
        self.__current_index += 1

    def back(self):
        item = self.__history_stack.pop()
        self.__current_index -= 1
        self.__save_stack.push(item)
        self.__save_stack_index += 1

        return self.__history_stack.peek()


    def forward(self):
        item = self.__save_stack.pop()
        self.__save_stack_index -= 1
        self.__history_stack.push(item)
        self.__current_index += 1

        return self.__history_stack.peek()

    def clear(self):
        while self.__current_index != 0:
            self.__history_stack.pop()
            self.__current_index -= 1

        while self.__save_stack_index != 0:
            self.__save_stack.pop()
            self.__save_stack_index -= 1

    def all(self):
        while self.__save_stack_index != 0:
            self.forward()

        text = ""

        while self.__history_stack != 0:
            buff = self.__history_stack.peek()
            self.back()
            text += f'{buff}\n'

        return text





