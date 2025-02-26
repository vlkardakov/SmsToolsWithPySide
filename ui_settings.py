# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QWidget)

class Ui_settingswindow(object):
    def setupUi(self, settingswindow):
        if not settingswindow.objectName():
            settingswindow.setObjectName(u"settingswindow")
        settingswindow.resize(320, 360)
        settingswindow.setMinimumSize(QSize(320, 360))
        settingswindow.setMaximumSize(QSize(320, 360))
        settingswindow.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.934, y1:1, x2:0.127, y2:0.244, stop:0 rgba(10, 13, 18, 255), stop:1 rgba(54, 63, 80, 255));\n"
"QMainWindow {\n"
"  background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #22d, stop:0.5 #c8f8ff, stop:1 #6d2);\n"
"}\n"
"\n"
"QWidget#wrapper {\n"
"  background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #22d, stop:0.5 #c8f8ff, stop:1 #6d2);\n"
"  border-radius: 16px;\n"
"  padding: 16px;\n"
"  color: white;\n"
"}\n"
"\n"
"QLabel#title {\n"
"  margin-bottom: 24px;\n"
"  font-size: 24px;\n"
"  font-weight: bold;\n"
"  color: white;\n"
"}\n"
"\n"
"QLabel#subtitle {\n"
"  margin-bottom: 12px;\n"
"  text-align: center;\n"
"  font-size: 18px;\n"
"  font-weight: bold;\n"
"  color: white;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"  border: 1px solid #bbb;\n"
"  background: #ddd;\n"
"  height: 8px;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"  background: #22d;\n"
"  border: 1px solid"
                        " #22d;\n"
"  width: 18px;\n"
"  height: 18px;\n"
"  margin: -6px 0;\n"
"  border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"  background: #6d2;\n"
"  border: 1px solid #6d2;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"  background: #6d2;\n"
"  border-radius: 4px;\n"
"}\n"
"")
        self.gridFrame = QFrame(settingswindow)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(10, 40, 301, 311))
        self.gridFrame.setStyleSheet(u"background-color: rgba(255,255,255,20);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7;\n"
"color: white;\n"
"\n"
"Line {\n"
"border: None;\n"
"}\n"
"\n"
"")
        self.modemNameDisplay = QLabel(self.gridFrame)
        self.modemNameDisplay.setObjectName(u"modemNameDisplay")
        self.modemNameDisplay.setGeometry(QRect(10, 10, 281, 31))
        self.modemNameDisplay.setMaximumSize(QSize(10000, 1000))
        self.modemName = QLineEdit(self.gridFrame)
        self.modemName.setObjectName(u"modemName")
        self.modemName.setGeometry(QRect(150, 10, 141, 31))
        self.modemName.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: None;")
        self.modemSpeed = QLineEdit(self.gridFrame)
        self.modemSpeed.setObjectName(u"modemSpeed")
        self.modemSpeed.setGeometry(QRect(150, 60, 141, 31))
        self.modemSpeed.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: None;")
        self.ModemSpeedDisplay = QLabel(self.gridFrame)
        self.ModemSpeedDisplay.setObjectName(u"ModemSpeedDisplay")
        self.ModemSpeedDisplay.setGeometry(QRect(10, 60, 281, 31))
        self.ModemSpeedDisplay.setMaximumSize(QSize(10000, 1000))
        self.charge_warning = QSlider(self.gridFrame)
        self.charge_warning.setObjectName(u"charge_warning")
        self.charge_warning.setGeometry(QRect(10, 140, 281, 20))
        self.charge_warning.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height: 6px;\n"
"    background: #d7d7d7;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #ffffff;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -5px 0;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #ffffff;\n"
"    border-radius: 3px;\n"
"}")
        self.charge_warning.setMaximum(100)
        self.charge_warning.setSingleStep(1)
        self.charge_warning.setValue(10)
        self.charge_warning.setOrientation(Qt.Horizontal)
        self.critical_charge = QLabel(self.gridFrame)
        self.critical_charge.setObjectName(u"critical_charge")
        self.critical_charge.setGeometry(QRect(10, 100, 221, 31))
        self.critical_charge.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: None;")
        self.archivateData = QPushButton(self.gridFrame)
        self.archivateData.setObjectName(u"archivateData")
        self.archivateData.setGeometry(QRect(10, 230, 281, 31))
        self.archivateData.setStyleSheet(u"QPushButton {\n"
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
        icon = QIcon()
        icon.addFile(u"../../../../.designer/backup/icons/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.archivateData.setIcon(icon)
        self.saveSettings = QPushButton(self.gridFrame)
        self.saveSettings.setObjectName(u"saveSettings")
        self.saveSettings.setGeometry(QRect(10, 270, 131, 31))
        self.saveSettings.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u"../../../../.designer/backup/icons/yes.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveSettings.setIcon(icon1)
        self.cancelSettings = QPushButton(self.gridFrame)
        self.cancelSettings.setObjectName(u"cancelSettings")
        self.cancelSettings.setGeometry(QRect(150, 270, 141, 31))
        self.cancelSettings.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u"../../../../.designer/backup/icons/no.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelSettings.setIcon(icon2)
        self.label = QLabel(self.gridFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 170, 131, 31))
        self.label.setStyleSheet(u"border: None;\n"
"background-color: rgba(255,255,255,0)")
        self.chooseTheme = QComboBox(self.gridFrame)
        self.chooseTheme.setObjectName(u"chooseTheme")
        self.chooseTheme.setGeometry(QRect(160, 170, 131, 31))
        self.chooseTheme.setStyleSheet(u"QComboBox {\n"
"    background-color: rgba(255,255,255,20);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius: 7px;\n"
"    color: white;\n"
"    padding: 5px;\n"
"    font: 11pt;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgba(255,255,255,50);\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"    background-color: rgba(255,255,255,80);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgba(255,255,255,20);\n"
"    border: 1px solid rgba(255,255,255,40);\n"
"    border-radius: 7px;\n"
"    color: white;\n"
"    selection-background-color: rgba(255,255,255,50);\n"
"    selection-color: white;\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    height: 24px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: rgba(255,255,255,50);\n"
"}")
        self.charge_warning_display = QLabel(self.gridFrame)
        self.charge_warning_display.setObjectName(u"charge_warning_display")
        self.charge_warning_display.setGeometry(QRect(220, 105, 71, 21))
        self.charge_warning_display.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: None;\n"
"font: 11pt;")
        self.label.raise_()
        self.modemNameDisplay.raise_()
        self.modemName.raise_()
        self.ModemSpeedDisplay.raise_()
        self.modemSpeed.raise_()
        self.charge_warning.raise_()
        self.critical_charge.raise_()
        self.archivateData.raise_()
        self.saveSettings.raise_()
        self.cancelSettings.raise_()
        self.chooseTheme.raise_()
        self.charge_warning_display.raise_()
        self.gridFrame_2 = QFrame(settingswindow)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridFrame_2.setGeometry(QRect(10, 10, 301, 21))
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
        self.closeButton.setGeometry(QRect(270, 0, 30, 21))
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
        icon3 = QIcon()
        icon3.addFile(u"icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.minimizeButton = QPushButton(self.gridFrame_2)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setGeometry(QRect(230, 0, 30, 21))
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
        icon4 = QIcon()
        icon4.addFile(u"icons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon4)
        self.labeltitle = QLabel(self.gridFrame_2)
        self.labeltitle.setObjectName(u"labeltitle")
        self.labeltitle.setGeometry(QRect(10, 0, 91, 21))
        self.labeltitle.setStyleSheet(u"border: None;\n"
"background-color: rgba(255,255,255,0);")

        self.retranslateUi(settingswindow)

        QMetaObject.connectSlotsByName(settingswindow)
    # setupUi

    def retranslateUi(self, settingswindow):
        settingswindow.setWindowTitle(QCoreApplication.translate("settingswindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.modemNameDisplay.setText(QCoreApplication.translate("settingswindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u043e\u0434\u0435\u043c\u0430:</span></p></body></html>", None))
        self.modemName.setText(QCoreApplication.translate("settingswindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.modemSpeed.setText(QCoreApplication.translate("settingswindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.ModemSpeedDisplay.setText(QCoreApplication.translate("settingswindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043c\u043e\u0434\u0435\u043c\u0430: </span></p></body></html>", None))
        self.critical_charge.setText(QCoreApplication.translate("settingswindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u041a\u0440\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u0437\u0430\u0440\u044f\u0434\u0430:</span></p></body></html>", None))
        self.archivateData.setText(QCoreApplication.translate("settingswindow", u"\u0410\u0440\u0445\u0438\u0444\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.saveSettings.setText(QCoreApplication.translate("settingswindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancelSettings.setText(QCoreApplication.translate("settingswindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("settingswindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0422\u0435\u043c\u0430 \u0433\u0440\u0430\u0434\u0438\u0435\u043d\u0442\u0430: </span></p></body></html>", None))
        self.charge_warning_display.setText(QCoreApplication.translate("settingswindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.closeButton.setText("")
        self.minimizeButton.setText("")
        self.labeltitle.setText(QCoreApplication.translate("settingswindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438</span></p></body></html>", None))
    # retranslateUi

