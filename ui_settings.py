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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QWidget)

class Ui_settingswindow(object):
    def setupUi(self, settingswindow):
        if not settingswindow.objectName():
            settingswindow.setObjectName(u"settingswindow")
        settingswindow.resize(320, 270)
        settingswindow.setMinimumSize(QSize(320, 270))
        settingswindow.setMaximumSize(QSize(320, 270))
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
        self.gridFrame.setGeometry(QRect(10, 10, 301, 251))
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
        self.horizontalSlider = QSlider(self.gridFrame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(10, 140, 281, 20))
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
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
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(10)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.critical_charge = QLabel(self.gridFrame)
        self.critical_charge.setObjectName(u"critical_charge")
        self.critical_charge.setGeometry(QRect(10, 100, 221, 31))
        self.critical_charge.setStyleSheet(u"background-color: rgba(255,255,255,0);\n"
"border: None;")
        self.archivateData = QPushButton(self.gridFrame)
        self.archivateData.setObjectName(u"archivateData")
        self.archivateData.setGeometry(QRect(10, 170, 281, 31))
        self.archivateData.setStyleSheet(u"font: 11pt")
        icon = QIcon()
        icon.addFile(u"../../../../.designer/backup/icons/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.archivateData.setIcon(icon)
        self.saveSettings = QPushButton(self.gridFrame)
        self.saveSettings.setObjectName(u"saveSettings")
        self.saveSettings.setGeometry(QRect(10, 210, 131, 31))
        self.saveSettings.setStyleSheet(u"font: 11pt;\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../../../.designer/backup/icons/yes.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveSettings.setIcon(icon1)
        self.cancelSettings = QPushButton(self.gridFrame)
        self.cancelSettings.setObjectName(u"cancelSettings")
        self.cancelSettings.setGeometry(QRect(150, 210, 141, 31))
        self.cancelSettings.setStyleSheet(u"font: 11pt")
        icon2 = QIcon()
        icon2.addFile(u"../../../../.designer/backup/icons/no.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelSettings.setIcon(icon2)
        self.modemNameDisplay.raise_()
        self.modemName.raise_()
        self.ModemSpeedDisplay.raise_()
        self.modemSpeed.raise_()
        self.horizontalSlider.raise_()
        self.critical_charge.raise_()
        self.archivateData.raise_()
        self.saveSettings.raise_()
        self.cancelSettings.raise_()

        self.retranslateUi(settingswindow)

        QMetaObject.connectSlotsByName(settingswindow)
    # setupUi

    def retranslateUi(self, settingswindow):
        settingswindow.setWindowTitle(QCoreApplication.translate("settingswindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.modemNameDisplay.setText(QCoreApplication.translate("settingswindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u043e\u0434\u0435\u043c\u0430:</span></p></body></html>", None))
        self.ModemSpeedDisplay.setText(QCoreApplication.translate("settingswindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043c\u043e\u0434\u0435\u043c\u0430: </span></p></body></html>", None))
        self.critical_charge.setText(QCoreApplication.translate("settingswindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u041a\u0440\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c \u0437\u0430\u0440\u044f\u0434\u0430:</span></p></body></html>", None))
        self.archivateData.setText(QCoreApplication.translate("settingswindow", u"\u0410\u0440\u0445\u0438\u0444\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.saveSettings.setText(QCoreApplication.translate("settingswindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancelSettings.setText(QCoreApplication.translate("settingswindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

