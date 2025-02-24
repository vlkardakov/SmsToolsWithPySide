import sys
from PySide6.QtWidgets import QApplication, QDialog
from ui_continue import Ui_Form

class Continue(QDialog):
    def __init__(self, text, but1text, but2text):
        super(Continue, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.choice = None  # Переменная для хранения выбора пользователя

        self.ui.but1.setText(but1text)
        self.ui.but2.setText(but2text)
        self.ui.text.setText(text)

        self.ui.but1.clicked.connect(self.but1)
        self.ui.but2.clicked.connect(self.but2)

    def but1(self):
        self.choice = False  # Запоминаем выбор
        self.reject()  # Закрываем диалог и возвращаем 0

    def but2(self):
        self.choice = True  # Запоминаем выбор
        self.accept()  # Закрываем диалог и возвращаем 1

    def get_choice(self):
        if self.exec() == QDialog.Accepted:
            return self.choice
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)

    choice = Continue("Продолжить?", "Нет!", "Кнчн!").get_choice()  # Показываем окно и ждем выбор пользователя

    print(f"Выбор пользователя: {choice}")  # Выводим результат в консоль
    exit()
    # sys.exit(app.exec())