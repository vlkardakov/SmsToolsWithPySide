import sys
from PySide6.QtCore import Qt, QPropertyAnimation, QPointF
from PySide6.QtGui import QPainter, QLinearGradient, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QGraphicsOpacityEffect

class AnimatedGradientWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        self.animation = QPropertyAnimation(self, b"gradient_offset")
        self.animation.setDuration(2000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setLoopCount(-1)
        self.animation.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(34, 34, 221))
        gradient.setColorAt(1, QColor(200, 248, 255))
        painter.setBrush(gradient)
        painter.drawRect(self.rect())

    def setGradientOffset(self, offset):
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Анимированный градиентный фон")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background: transparent;")
        self.setCentralWidget(AnimatedGradientWidget())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
