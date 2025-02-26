# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'continue.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(280, 150)
        Form.setMinimumSize(QSize(0, 150))
        Form.setMaximumSize(QSize(280, 150))
        Form.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.934, y1:1, x2:0.127, y2:0.244, stop:0 rgba(10, 13, 18, 255), stop:1 rgba(54, 63, 80, 255));")
        self.gridFrame = QFrame(Form)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(10, 40, 261, 101))
        self.gridFrame.setStyleSheet(u"background-color: rgba(255,255,255,20);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7;\n"
"color: white;")
        self.text = QLabel(self.gridFrame)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(10, 10, 241, 40))
        self.text.setMaximumSize(QSize(16777215, 40))
        self.but1 = QPushButton(self.gridFrame)
        self.but1.setObjectName(u"but1")
        self.but1.setGeometry(QRect(10, 59, 111, 31))
        self.but1.setMinimumSize(QSize(80, 30))
        self.but1.setMaximumSize(QSize(10000, 1000))
        self.but1.setFocusPolicy(Qt.TabFocus)
        self.but1.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255,255,255,20);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,80);\n"
"}")
        self.but2 = QPushButton(self.gridFrame)
        self.but2.setObjectName(u"but2")
        self.but2.setGeometry(QRect(130, 59, 121, 31))
        self.but2.setMinimumSize(QSize(80, 30))
        self.but2.setMaximumSize(QSize(2000, 1000))
        self.but2.setFocusPolicy(Qt.StrongFocus)
        self.but2.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255,255,255,20);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,80);\n"
"}")
        self.gridFrame_2 = QFrame(Form)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridFrame_2.setGeometry(QRect(10, 10, 261, 21))
        self.gridFrame_2.setStyleSheet(u"background-color: rgba(255,255,255,20);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7;\n"
"color: white;\n"
"QPushButton {\n"
"background-color: rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,80);\n"
"}")
        self.closeButton = QPushButton(self.gridFrame_2)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(230, 0, 30, 21))
        self.closeButton.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255,255,255,20);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,10,10,80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,80);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon)
        self.minimizeButton = QPushButton(self.gridFrame_2)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(190, 0, 30, 21))
        self.minimizeButton.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255,255,255,20);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(30,30,255,80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,80);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon1)
        self.labeltitle = QLabel(self.gridFrame_2)
        self.labeltitle.setObjectName(u"labeltitle")
        self.labeltitle.setGeometry(QRect(10, 0, 91, 21))
        self.labeltitle.setStyleSheet(u"border: None;\n"
"background-color: rgba(255,255,255,0);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.text.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
        self.but1.setText("")
        self.but2.setText("")
        self.closeButton.setText("")
        self.minimizeButton.setText("")
        self.labeltitle.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0424\u043e\u0440\u043c\u0430</span></p></body></html>", None))
    # retranslateUi

