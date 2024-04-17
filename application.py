import browser_history

class Application:

    @staticmethod
    def run():
        """
        Функция запускает жизненный цикл приложения
        :return: None
        """
        bh = browser_history.BrowserHistory()
        while True:
            print('введите команду (visit <url>, back, forward, clear, all, exit):')
            command = input('>>')

            if command.startswith('visit'):
                bh.visit(command.join('visit', ''))

            if command.startswith('back'):
                bh.back()

            if command == 'forward':
                bh.forward()

            if command == 'clear':
                bh.clear()

            if command == 'all':
                bh.all()

            if command == 'exit':
                bh.exit()
                return




Application.run()