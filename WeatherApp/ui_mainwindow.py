# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(651, 454)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.enter_label = QLabel(self.centralwidget)
        self.enter_label.setObjectName(u"enter_label")
        self.enter_label.setEnabled(True)
        self.enter_label.setGeometry(QRect(0, 10, 651, 61))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        self.enter_label.setFont(font)
        self.enter_label.setStyleSheet(u"")
        self.enter_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.enter_label.setWordWrap(False)
        self.city_lineEdit = QLineEdit(self.centralwidget)
        self.city_lineEdit.setObjectName(u"city_lineEdit")
        self.city_lineEdit.setGeometry(QRect(200, 70, 241, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        self.city_lineEdit.setFont(font1)
        self.getWeather_button = QPushButton(self.centralwidget)
        self.getWeather_button.setObjectName(u"getWeather_button")
        self.getWeather_button.setGeometry(QRect(210, 140, 221, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.getWeather_button.setFont(font2)
        self.weatherInfo_label = QLabel(self.centralwidget)
        self.weatherInfo_label.setObjectName(u"weatherInfo_label")
        self.weatherInfo_label.setGeometry(QRect(170, 370, 311, 41))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(22)
        self.weatherInfo_label.setFont(font3)
        self.weatherInfo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperature_label = QLabel(self.centralwidget)
        self.temperature_label.setObjectName(u"temperature_label")
        self.temperature_label.setGeometry(QRect(250, 190, 151, 41))
        self.temperature_label.setFont(font)
        self.temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(140, 190, 401, 61))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(18)
        font4.setBold(True)
        self.error_label.setFont(font4)
        self.error_label.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.error_label.setStyleSheet(u"color: rgb(255, 0, 4);")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.error_label.setMargin(0)
        self.weather_icon = QLabel(self.centralwidget)
        self.weather_icon.setObjectName(u"weather_icon")
        self.weather_icon.setGeometry(QRect(220, 240, 211, 121))
        self.weather_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.error_label.raise_()
        self.enter_label.raise_()
        self.city_lineEdit.raise_()
        self.getWeather_button.raise_()
        self.weatherInfo_label.raise_()
        self.temperature_label.raise_()
        self.weather_icon.raise_()
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.enter_label.setText(QCoreApplication.translate("MainWindow", u"Enter city name:", None))
        self.getWeather_button.setText(QCoreApplication.translate("MainWindow", u"Get Weather", None))
        self.weatherInfo_label.setText(QCoreApplication.translate("MainWindow", u"Weather infomation", None))
        self.temperature_label.setText(QCoreApplication.translate("MainWindow", u"22\u00b0C", None))
        self.error_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">City Not Found: <br/>Please input the correct location</p></body></html>", None))
        self.weather_icon.setText(QCoreApplication.translate("MainWindow", u"Weather icon", None))
    # retranslateUi

