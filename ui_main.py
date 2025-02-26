# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 530)
        MainWindow.setMinimumSize(QSize(600, 525))
        MainWindow.setMaximumSize(QSize(600, 530))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.934, y1:1, x2:0.127, y2:0.244, stop:0 rgba(10, 13, 18, 255), stop:1 rgba(54, 63, 80, 255));\n"
"font-family: Grammatica;\n"
"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_form = QFrame(self.centralwidget)
        self.input_form.setObjectName(u"input_form")
        self.input_form.setGeometry(QRect(10, 40, 581, 411))
        self.input_form.setStyleSheet(u"background-color: rgba(255,255,255,20);\n"
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
        self.name = QTextEdit(self.input_form)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(100, 10, 111, 31))
        self.name.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: 1px solid rgba(255,255,255,0);\n"
"border-radius: 7;\n"
"font: 11pt;")
        self.number = QTextEdit(self.input_form)
        self.number.setObjectName(u"number")
        self.number.setGeometry(QRect(260, 10, 71, 31))
        self.number.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: 1px solid rgba(255,255,255,0);\n"
"border-radius: 7;\n"
"font: 11pt;")
        self.add_contact = QPushButton(self.input_form)
        self.add_contact.setObjectName(u"add_contact")
        self.add_contact.setGeometry(QRect(10, 50, 321, 31))
        self.add_contact.setStyleSheet(u"QPushButton {\n"
"font: 11pt;\n"
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
        self.display_name = QLabel(self.input_form)
        self.display_name.setObjectName(u"display_name")
        self.display_name.setGeometry(QRect(220, 10, 111, 31))
        self.display_number = QLabel(self.input_form)
        self.display_number.setObjectName(u"display_number")
        self.display_number.setGeometry(QRect(10, 10, 201, 31))
        self.contacts = QTableWidget(self.input_form)
        self.contacts.setObjectName(u"contacts")
        self.contacts.setGeometry(QRect(10, 160, 191, 241))
        self.display_search = QLabel(self.input_form)
        self.display_search.setObjectName(u"display_search")
        self.display_search.setGeometry(QRect(10, 120, 191, 31))
        self.arguments = QLineEdit(self.input_form)
        self.arguments.setObjectName(u"arguments")
        self.arguments.setGeometry(QRect(70, 120, 131, 31))
        self.arguments.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: 1px solid rgba(255,255,255,0);\n"
"border-radius: 7;\n"
"font: 11pt;")
        self.search = QPushButton(self.input_form)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(170, 120, 31, 31))
        self.search.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: rgba(255,255,255,0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255,255,80);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon)
        self.console = QTextBrowser(self.input_form)
        self.console.setObjectName(u"console")
        self.console.setGeometry(QRect(210, 160, 361, 241))
        self.console.setStyleSheet(u"font: 11pt;")
        self.settings = QPushButton(self.input_form)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(460, 10, 111, 31))
        self.settings.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u"icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon1)
        self.open_folder = QPushButton(self.input_form)
        self.open_folder.setObjectName(u"open_folder")
        self.open_folder.setGeometry(QRect(350, 10, 101, 31))
        self.open_folder.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u"icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_folder.setIcon(icon2)
        self.analyze = QPushButton(self.input_form)
        self.analyze.setObjectName(u"analyze")
        self.analyze.setGeometry(QRect(350, 50, 171, 31))
        self.analyze.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u"icons/analyze.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.analyze.setIcon(icon3)
        self.get_messages = QPushButton(self.input_form)
        self.get_messages.setObjectName(u"get_messages")
        self.get_messages.setGeometry(QRect(210, 120, 161, 31))
        self.get_messages.setStyleSheet(u"QPushButton {\n"
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
        icon4 = QIcon()
        icon4.addFile(u"icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.get_messages.setIcon(icon4)
        self.restart = QPushButton(self.input_form)
        self.restart.setObjectName(u"restart")
        self.restart.setGeometry(QRect(380, 120, 191, 31))
        self.restart.setStyleSheet(u"QPushButton {\n"
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
        icon5 = QIcon()
        icon5.addFile(u"icons/refresh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restart.setIcon(icon5)
        self.save = QPushButton(self.input_form)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(530, 50, 41, 31))
        self.save.setStyleSheet(u"QPushButton {\n"
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
        icon6 = QIcon()
        icon6.addFile(u"icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save.setIcon(icon6)
        self.gridFrame_2 = QFrame(self.input_form)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridFrame_2.setGeometry(QRect(140, 90, 171, 21))
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
        self.closeButton_3 = QPushButton(self.gridFrame_2)
        self.closeButton_3.setObjectName(u"closeButton_3")
        self.closeButton_3.setGeometry(QRect(140, 0, 30, 21))
        self.closeButton_3.setStyleSheet(u"QPushButton {\n"
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
        icon7 = QIcon()
        icon7.addFile(u"icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton_3.setIcon(icon7)
        self.minimizeButton_3 = QPushButton(self.gridFrame_2)
        self.minimizeButton_3.setObjectName(u"minimizeButton_3")
        self.minimizeButton_3.setGeometry(QRect(100, 0, 30, 21))
        self.minimizeButton_3.setStyleSheet(u"QPushButton {\n"
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
        icon8 = QIcon()
        icon8.addFile(u"icons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton_3.setIcon(icon8)
        self.labeltitle_3 = QLabel(self.gridFrame_2)
        self.labeltitle_3.setObjectName(u"labeltitle_3")
        self.labeltitle_3.setGeometry(QRect(10, 0, 91, 21))
        self.labeltitle_3.setStyleSheet(u"border: None;\n"
"background-color: rgba(255,255,255,0);")
        self.add_contact.raise_()
        self.display_name.raise_()
        self.display_number.raise_()
        self.contacts.raise_()
        self.display_search.raise_()
        self.name.raise_()
        self.number.raise_()
        self.arguments.raise_()
        self.search.raise_()
        self.console.raise_()
        self.settings.raise_()
        self.open_folder.raise_()
        self.analyze.raise_()
        self.get_messages.raise_()
        self.restart.raise_()
        self.save.raise_()
        self.gridFrame_2.raise_()
        self.output_form = QFrame(self.centralwidget)
        self.output_form.setObjectName(u"output_form")
        self.output_form.setGeometry(QRect(10, 460, 581, 61))
        self.output_form.setStyleSheet(u"background-color: rgba(255,255,255,20);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7;\n"
"color: white;")
        self.gridLayout = QGridLayout(self.output_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sendButton = QPushButton(self.output_form)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setMinimumSize(QSize(140, 0))
        self.sendButton.setMaximumSize(QSize(100, 10000))
        self.sendButton.setStyleSheet(u"QPushButton {\n"
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
        icon9 = QIcon()
        icon9.addFile(u"icons/bolt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sendButton.setIcon(icon9)

        self.gridLayout.addWidget(self.sendButton, 4, 1, 2, 1)

        self.message = QTextEdit(self.output_form)
        self.message.setObjectName(u"message")

        self.gridLayout.addWidget(self.message, 4, 0, 2, 1)

        self.gridFrame = QFrame(self.centralwidget)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(10, 10, 581, 21))
        self.gridFrame.setStyleSheet(u"background-color: rgba(255,255,255,20);\n"
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
        self.closeButton = QPushButton(self.gridFrame)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(550, 0, 30, 21))
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
        self.closeButton.setIcon(icon7)
        self.minimizeButton = QPushButton(self.gridFrame)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(510, 0, 30, 21))
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
        self.minimizeButton.setIcon(icon8)
        self.labeltitle = QLabel(self.gridFrame)
        self.labeltitle.setObjectName(u"labeltitle")
        self.labeltitle.setGeometry(QRect(10, 0, 231, 21))
        self.labeltitle.setStyleSheet(u"border: None;\n"
"background-color: rgba(255,255,255,0);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f\u043c\u0438", None))
        self.name.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Grammatica'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gramatica';\"><br /></p></body></html>", None))
        self.number.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Grammatica'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Gramatica';\"><br /></p></body></html>", None))
        self.add_contact.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.display_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0418\u043c\u044f: </span></p></body></html>", None))
        self.display_number.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0422\u0435\u043b\u0435\u0444\u043e\u043d: +7</span></p></body></html>", None))
        self.display_search.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u041f\u043e\u0438\u0441\u043a :</span></p></body></html>", None))
        self.search.setText("")
        self.console.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Grammatica'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Gramatica';\">APP STARTING...</span></p></body></html>", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.open_folder.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b\u044b", None))
        self.analyze.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
#if QT_CONFIG(tooltip)
        self.get_messages.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.get_messages.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.get_messages.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.restart.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043c\u043e\u0434\u0435\u043c", None))
        self.save.setText("")
        self.closeButton_3.setText("")
        self.minimizeButton_3.setText("")
        self.labeltitle_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0424\u043e\u0440\u043c\u0430</span></p></body></html>", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c!", None))
        self.closeButton.setText("")
        self.minimizeButton.setText("")
        self.labeltitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0426\u0435\u043d\u0442\u0440 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f\u043c\u0438</span></p></body></html>", None))
    # retranslateUi

