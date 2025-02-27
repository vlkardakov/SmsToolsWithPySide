import sys
from PySide6.QtWidgets import QApplication, QDialog
from ui_continue import Ui_Form
from PySide6.QtCore import Qt, QTimer, QTime
from PySide6.QtGui import QImage, QPixmap, QPainter, QPainterPath
import cv2, os

class Continue(QDialog):
    def __init__(self, text, but1text, but2text):
        super(Continue, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #настройки
        self.settings = self.read_settings()
        self.settings['port'] = None  # Настроить
        self.canModem = False
        self.incomingCount = 0


        # инициализация видева
        self.capture = cv2.VideoCapture(f"Files/backgrounds/{self.settings['theme']}.mp4")
        self.snapshot = QPixmap()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.start_time = QTime.currentTime()

        # запуск
        self.timer.start(30)

        self.setWindowFlags(Qt.FramelessWindowHint)  # titlebar
        self.setAttribute(Qt.WA_TranslucentBackground)  # пусть фон будет прозрачным чтобы видет видева



        self.choice = None  #выбор пользователя

        self.ui.but1.setText(but1text)
        self.ui.but2.setText(but2text)
        self.ui.text.setText(text)

        self.ui.closeButton.clicked.connect(self.close)
        self.ui.minimizeButton.clicked.connect(self.showMinimized)


        self.ui.but1.clicked.connect(self.but1)
        self.ui.but2.clicked.connect(self.but2)

    def but1(self):
        self.choice = False  # Запоминаем выбор
        self.accept()#0

    def but2(self):
        self.choice = True  # Запоминаем выбор
        self.accept()#1

    def get_choice(self):
        if self.exec() == QDialog.Accepted:
            return self.choice
        return None
    def read_settings(self):
        settings_file = "Files/settings.txt"
        if not os.path.exists(settings_file):
            print(f"Файл {settings_file} не существует.")
            exit()
        settings = {}
        with open(settings_file, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                line = line.strip()
                if not line or '=' not in line:
                    continue
                try:
                    name, value = line.split('=', 1)
                    settings[name.strip()] = value.strip()
                except ValueError as e:
                    print(f"Ошибка в строке {line_num}: '{line}', ошибка: {e}")
                    continue
        return settings

    def mousePressEvent(self, event):
        try:
            if event.button() == Qt.LeftButton and self.childAt(event.pos()) == self.ui.Title:
                self.dragPos = event.globalPosition().toPoint()
        except:
            pass

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() == Qt.LeftButton and self.childAt(event.pos()) == self.ui.Title:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()
        except:
            pass
    def update_frame(self):
        if self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                # повтор
                if self.capture.get(cv2.CAP_PROP_POS_FRAMES) == self.capture.get(cv2.CAP_PROP_FRAME_COUNT):
                    self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame.shape
                bytes_per_line = ch * w

                image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.snapshot = QPixmap.fromImage(image)
                self.update()
    def paintEvent(self, event):
        if not self.snapshot.isNull():
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)

            path = QPainterPath()
            path.addRoundedRect(0, 0, self.width(), self.height(), 10, 10)

            painter.setClipPath(path)

            painter.drawPixmap(0, 0, self.snapshot.scaled(
                self.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            ))
        super().paintEvent(event)

    def closeEvent(self, event):
        self.capture.release()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    choice = Continue("Продолжить?", "Нет!", "Кнчн!").get_choice()  # Показываем окно и ждем выбор пользователя

    print(f"Выбор пользователя: {choice}")
    exit()
    # sys.exit(app.exec())