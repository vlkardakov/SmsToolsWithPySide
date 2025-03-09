import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QSize, QPoint


class ShrinkingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анимированное окно")
        self.resize(400, 300)

        # Центрируем окно на экране
        self.center()

        # Настройка внешнего вида
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
                border-radius: 10px;
            }
            QPushButton {
                background-color: #4a86e8;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #3a76d8;
            }
        """)

        # Создаем центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Создаем вертикальный layout
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(30, 30, 30, 30)

        # Добавляем кнопку закрытия
        self.close_button = QPushButton("Закрыть с анимацией сжатия")
        self.close_button.clicked.connect(self.shrink_animation)
        layout.addWidget(self.close_button)

        # Флаг для отслеживания, выполняется ли анимация
        self.animation_running = False

    def center(self):
        """Центрирует окно на экране"""
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        """Перехват стандартного события закрытия"""
        if not self.animation_running:
            # Если анимация не запущена, показываем анимацию сжатия
            self.shrink_animation()
            event.ignore()  # Игнорируем стандартное закрытие
        else:
            # Если анимация уже запущена, позволяем окну закрыться
            event.accept()

    def shrink_animation(self):
        """Анимация полного сжатия до нуля"""
        if self.animation_running:
            return

        self.animation_running = True

        # Сохраняем исходный размер
        original_size = self.size()

        # Получаем центр окна для правильного масштабирования
        center_x = self.x() + original_size.width() / 2
        center_y = self.y() + original_size.height() / 2

        # Создаем анимацию размера
        self.size_anim = QPropertyAnimation(self, b"size")
        self.size_anim.setDuration(1000)  # 1 секунда на анимацию
        self.size_anim.setStartValue(original_size)
        self.size_anim.setEndValue(QSize(0, 0))  # Полное сжатие до нуля
        self.size_anim.setEasingCurve(QEasingCurve.InOutQuad)  # Плавное ускорение/замедление

        # Создаем анимацию позиции, чтобы окно сжималось к центру
        self.pos_anim = QPropertyAnimation(self, b"pos")
        self.pos_anim.setDuration(1000)
        self.pos_anim.setStartValue(self.pos())
        # Устанавливаем конечную позицию в центр окна
        final_x = int(center_x)
        final_y = int(center_y)
        self.pos_anim.setEndValue(QPoint(final_x, final_y))
        self.pos_anim.setEasingCurve(QEasingCurve.InOutQuad)

        # При завершении анимации закрываем окно
        self.size_anim.finished.connect(self.close)

        # Запускаем анимации
        self.size_anim.start()
        self.pos_anim.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShrinkingWindow()
    window.show()
    sys.exit(app.exec())
