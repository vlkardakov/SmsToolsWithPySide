# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notification.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Notification(object):
    def setupUi(self, Notification):
        if not Notification.objectName():
            Notification.setObjectName(u"Notification")
        Notification.resize(200, 120)
        Notification.setMinimumSize(QSize(200, 120))
        Notification.setMaximumSize(QSize(200, 120))
        Notification.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.934, y1:1, x2:0.127, y2:0.244, stop:0 rgba(10, 13, 18, 255), stop:1 rgba(54, 63, 80, 255));")
        self.gridFrame = QFrame(Notification)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(10, 10, 181, 101))
        self.gridFrame.setStyleSheet(u"background-color: rgba(255,255,255,20);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7;\n"
"color: white;")
        self.gridLayout = QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.text = QLabel(self.gridFrame)
        self.text.setObjectName(u"text")
        self.text.setMaximumSize(QSize(16777215, 40))

        self.gridLayout.addWidget(self.text, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.but2 = QPushButton(self.gridFrame)
        self.but2.setObjectName(u"but2")
        self.but2.setMinimumSize(QSize(80, 30))
        self.but2.setMaximumSize(QSize(180, 30))
        self.but2.setFocusPolicy(Qt.StrongFocus)
        self.but2.setStyleSheet(u"font: 11pt")

        self.horizontalLayout.addWidget(self.but2)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(Notification)

        QMetaObject.connectSlotsByName(Notification)
    # setupUi

    def retranslateUi(self, Notification):
        Notification.setWindowTitle(QCoreApplication.translate("Notification", u"\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u0435", None))
        self.text.setText(QCoreApplication.translate("Notification", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
        self.but2.setText(QCoreApplication.translate("Notification", u"\u041e\u041a", None))
    # retranslateUi

