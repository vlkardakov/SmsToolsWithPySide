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
        MainWindow.setMinimumSize(QSize(600, 530))
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
        self.contacts.setStyleSheet(u"QTableWidget {\n"
"    gridline-color: transparent;\n"
"    selection-background-color: rgba(255, 255, 255, 40);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0431\u0435\u043b\u044b\u0439 \u043f\u0440\u0438 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0438 */\n"
"    selection-color: white;  /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u0440\u0438 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    border: none;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgba(255, 255, 255, 40);  /* \u041f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0431\u0435\u043b\u044b\u0439 \u043f\u0440\u0438 \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0438 */\n"
"    color: white;\n"
"	border: None;\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: rgba(255, 255, 255, 20);  /* \u0415\u0449\u0451 \u0431\u043e\u043b\u0435\u0435 \u0441"
                        "\u0432\u0435\u0442\u043b\u044b\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: none;\n"
"}\n"
"/* \u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 */\n"
"QScrollBar:vertical {\n"
"    background: rgba(255, 255, 255, 10);  /* \u0424\u043e\u043d \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"    width: 10px;                          /* \u0428\u0438\u0440\u0438\u043d\u0430 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"    margin: 0px;\n"
"    border-radius: 5px;                   /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u043a \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"QScrollBar::ha"
                        "ndle:vertical {\n"
"    background: rgba(255, 255, 255, 0);  /* \u0426\u0432\u0435\u0442 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    min-height: 20px;                     /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    border-radius: 5px;                   /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"}\n"
"\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0438 \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 (\u0441\u0442\u0440\u0435\u043b\u043a\u0438) */\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;                          /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"}\n"
"\n"
"/* \u0413\u043e\u0440\u0438\u0437\u043e\u043d"
                        "\u0442\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 */\n"
"QScrollBar:horizontal {\n"
"    background: rgba(255, 255, 255, 10);\n"
"    height: 10px;                         /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(255, 255, 255, 40);\n"
"    min-width: 20px;                      /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(255, 255, 255, 60);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background: rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 0px;                        "
                        "   /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"}\n"
"\n"
"/* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0444\u043e\u043d \u0443 \u043a\u0440\u0430\u0451\u0432 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:horizontal,\n"
"QScrollBar::add-page:horizontal {\n"
"    background: rgba(255, 255, 255, 50);  /* \u0424\u043e\u043d \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"}")
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
        icon.addFile(u"Files/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon)
        self.console = QTextBrowser(self.input_form)
        self.console.setObjectName(u"console")
        self.console.setGeometry(QRect(210, 160, 361, 241))
        self.console.setStyleSheet(u"QTextBrowser {\n"
"font: 11pt;\n"
"\n"
"}\n"
"\n"
"/* \u0412\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 */\n"
"QScrollBar:vertical {\n"
"    background: rgba(255, 255, 255, 10);  /* \u0424\u043e\u043d \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"    width: 10px;                          /* \u0428\u0438\u0440\u0438\u043d\u0430 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"    margin: 0px;\n"
"    border-radius: 5px;                   /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u043a \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(255, 255, 255, 0);  /* \u0426\u0432\u0435\u0442 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430"
                        " */\n"
"    min-height: 20px;                     /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    border-radius: 5px;                   /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"}\n"
"\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0438 \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 (\u0441\u0442\u0440\u0435\u043b\u043a\u0438) */\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;                          /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"}\n"
"\n"
"/* \u0413\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 */\n"
"QScrollBar:horizontal {\n"
"   "
                        " background: rgba(255, 255, 255, 10);\n"
"    height: 10px;                         /* \u0412\u044b\u0441\u043e\u0442\u0430 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgba(255, 255, 255, 40);\n"
"    min-width: 20px;                      /* \u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(255, 255, 255, 60);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background: rgba(255, 255, 255, 80);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 0px;                           /* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438"
                        " */\n"
"}\n"
"\n"
"/* \u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0444\u043e\u043d \u0443 \u043a\u0440\u0430\u0451\u0432 \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"QScrollBar::sub-page:vertical,\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:horizontal,\n"
"QScrollBar::add-page:horizontal {\n"
"    background: rgba(255, 255, 255, 50);  /* \u0424\u043e\u043d \u0441\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440\u0430 */\n"
"}")
        self.settings = QPushButton(self.input_form)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(440, 10, 131, 31))
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
        icon1.addFile(u"Files/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon1)
        self.open_folder = QPushButton(self.input_form)
        self.open_folder.setObjectName(u"open_folder")
        self.open_folder.setGeometry(QRect(350, 10, 81, 31))
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
        icon2.addFile(u"Files/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon3.addFile(u"Files/icons/analyze.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon4.addFile(u"Files/icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon5.addFile(u"Files/icons/autorenew.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon6.addFile(u"Files/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save.setIcon(icon6)
        self.number = QLineEdit(self.input_form)
        self.number.setObjectName(u"number")
        self.number.setGeometry(QRect(102, 10, 111, 31))
        self.number.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: 1px solid rgba(255,255,255,0);\n"
"border-radius: 7;\n"
"font: 11pt;")
        self.name = QLineEdit(self.input_form)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(260, 10, 71, 31))
        self.name.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: 1px solid rgba(255,255,255,0);\n"
"border-radius: 7;\n"
"font: 11pt;")
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
        icon7 = QIcon()
        icon7.addFile(u"Files/icons/bolt.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sendButton.setIcon(icon7)

        self.gridLayout.addWidget(self.sendButton, 4, 1, 2, 1)

        self.message = QTextEdit(self.output_form)
        self.message.setObjectName(u"message")

        self.gridLayout.addWidget(self.message, 4, 0, 2, 1)

        self.Title = QFrame(self.centralwidget)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(10, 10, 581, 21))
        self.Title.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: None;\n"
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
        self.closeButton = QPushButton(self.Title)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(550, 0, 30, 21))
        self.closeButton.setStyleSheet(u"QPushButton {\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7;\n"
"background-color: rgba(255,255,255,20);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255,30,30,80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,60,60,100);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"Files/icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon8)
        self.minimizeButton = QPushButton(self.Title)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(510, 0, 30, 21))
        self.minimizeButton.setStyleSheet(u"QPushButton {\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7;\n"
"background-color: rgba(255,255,255,20);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(30,30,255,80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(60,60,255,100);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"Files/icons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon9)
        self.labeltitle = QLabel(self.Title)
        self.labeltitle.setObjectName(u"labeltitle")
        self.labeltitle.setGeometry(QRect(0, 0, 231, 21))
        self.labeltitle.setStyleSheet(u"border: None;\n"
"background-color: rgba(255,255,255,0);")
        self.rerunButton = QPushButton(self.Title)
        self.rerunButton.setObjectName(u"rerunButton")
        self.rerunButton.setGeometry(QRect(470, 0, 30, 21))
        self.rerunButton.setStyleSheet(u"QPushButton {\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7;\n"
"background-color: rgba(255,255,255,20);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(5,255,30,80);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(10,255,60,100);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"Files/icons/restart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rerunButton.setIcon(icon10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f\u043c\u0438", None))
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u043e\u0438\u0441\u043a \u043c\u043e\u0434\u0435\u043c\u0430...</p></body></html>", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.open_folder.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b\u044b", None))
        self.analyze.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
#if QT_CONFIG(tooltip)
        self.get_messages.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.get_messages.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.get_messages.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f", None))
        self.restart.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043c\u043e\u0434\u0435\u043c", None))
        self.save.setText("")
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c!", None))
        self.closeButton.setText("")
        self.minimizeButton.setText("")
        self.labeltitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0426\u0435\u043d\u0442\u0440 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f\u043c\u0438</span></p></body></html>", None))
        self.rerunButton.setText("")
    # retranslateUi

