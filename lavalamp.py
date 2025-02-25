import sys
import vlc
from PySide6 import QtWidgets, QtGui, QtCore


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Welcome Galaxy")
        self.initUI()

    def initUI(self):
        self.vlc_instance = vlc.Instance()
        self.media_player = self.vlc_instance.media_player_new()

        self.videoFrame = QtWidgets.QFrame(self)
        self.setCentralWidget(self.videoFrame)
        print(f"{sys.platform=}")
        if sys.platform == "linux":
            self.media_player.set_xwindow(self.videoFrame.winId())
        elif sys.platform == "win32":
            self.media_player.set_hwnd(self.videoFrame.winId())
        elif sys.platform == "darwin":
            self.media_player.set_nsobject(int(self.videoFrame.winId()))
        else:
            pass

        # Добавляем обработчик события окончания медиа
        self.media_player.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached, self.on_media_end)

        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.play_video)
        self.timer.start(500)

    def play_video(self):
        media = self.vlc_instance.media_new('violet.mp4')
        # Устанавливаем флаг зацикливания
        media.add_option('input-repeat=65535')  # Или можно использовать '-1' для бесконечного повтора
        self.media_player.set_media(media)
        self.media_player.play()

    def on_media_end(self, event):
        # Перезапускаем видео с начала
        self.media_player.set_position(0)
        self.media_player.play()


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())