# **Разработка модуля браузера: История**

# **Цели**

1. Понять и реализовать структуру данных стек.
2. Применить объектно-ориентированный подход к решению задачи.
3. Разработать консольное приложение для управления историей веб-браузера.

# **Задача**

Студентам необходимо создать консольное приложение на языке Python, которое позволяет пользователю передвигаться по истории веб-страниц с использованием стека. История должна поддерживать операции перехода назад, вперед, очистки и просмотра всей истории.

# **Описание функционала**

### **Посещение страницы (visit)**

Пользователь может ввести URL для посещения новой страницы. Этот URL добавляется в стек истории, вместе с датой и временем запроса.

### **Переход назад (back)**

Позволяет вернуться к предыдущему URL в стеке, не удаляя его из стека.

### **Переход вперед (forward)**

Возвращает пользователя к URL, который он посетил до использования команды back.

### Очистка истории (clear)

Очищает все историю посещения страниц.

### Просмотр истории (all)

Возвращает информацию о посещенных страниц в формате {datetime: URL} в порядке LIFO.
