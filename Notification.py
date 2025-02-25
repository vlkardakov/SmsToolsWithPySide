import sys
from PySide6.QtWidgets import QApplication, QDialog
from ui_notification import Ui_Notification

class Notification(QDialog):
    def __init__(self, text):
        super(Notification, self).__init__()
        self.ui = Ui_Notification()
        self.ui.setupUi(self)

        self.choice = None  # Переменная для хранения выбора пользователя

        self.ui.but2.setText("OK")
        self.ui.text.setText(text)

        self.ui.but2.clicked.connect(self.but2)

    def but2(self):
        self.close()
    def run(self):
        if self.exec() == QDialog.Accepted:
            return self.choice
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)

    Notification("Всё очень плохо!").run()  # Показываем окно и ждем выбор пользователя
    exit()