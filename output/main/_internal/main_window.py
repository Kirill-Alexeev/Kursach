# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(673, 564)
        MainWindow.setStyleSheet(u"background-color: #202A47; \n"
"font-family: Lucida Sans Unicode;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -1045, 636, 1589))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(155, 16777215))
        self.label.setPixmap(QPixmap(u":/icons/images/minsport.svg"))

        self.horizontalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(150, 16777215))
        self.label_2.setPixmap(QPixmap(u":/icons/images/minstroy.svg"))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(150, 16777215))
        self.label_7.setPixmap(QPixmap(u":/icons/images/saratov.svg"))

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(150, 16777215))
        self.label_8.setPixmap(QPixmap(u":/icons/images/smartcity.svg"))

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(156, 16777215))
        self.label_9.setPixmap(QPixmap(u":/icons/images/logo.svg"))

        self.horizontalLayout_2.addWidget(self.label_9)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font-size: 30px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.label_10)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(2, 50))
        self.label_13.setStyleSheet(u"background-color: white;")

        self.horizontalLayout.addWidget(self.label_13)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-size: 30px;\n"
"color: white;")

        self.horizontalLayout.addWidget(self.label_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font-size: 20px;\n"
"color: white;")

        self.verticalLayout_2.addWidget(self.label_12)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(600, 16777215))
        self.label_3.setStyleSheet(u"font-weight: 600;\n"
"font-size: 20px;\n"
"color: white;\n"
"margin: 30 0 0;")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QSize(600, 16777215))
        self.label_4.setStyleSheet(u"font-size: 17px;\n"
"color: white;")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(609, 16777215))
        self.label_5.setStyleSheet(u"font-size: 17px;\n"
"color: white;")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(600, 16777215))
        self.label_6.setStyleSheet(u"font-size: 17px;\n"
"color: white;")

        self.verticalLayout.addWidget(self.label_6)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_14 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font-weight: 600;\n"
"font-size: 20px;\n"
"color: white;\n"
"margin: 30 0 0;")

        self.verticalLayout_3.addWidget(self.label_14)

        self.listView = QListView(self.scrollAreaWidgetContents_2)
        self.listView.setObjectName(u"listView")
        self.listView.setMinimumSize(QSize(300, 270))
        self.listView.setMaximumSize(QSize(300, 300))
        self.listView.setStyleSheet(u"font-size: 17px;\n"
"color: white;\n"
"border: 1 solid white;\n"
"border-radius: 5;")

        self.verticalLayout_3.addWidget(self.listView)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font-size: 18px;\n"
"color: white;")
        self.label_27.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_27)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font-weight: 600;\n"
"font-size: 20px;\n"
"color: white;\n"
"margin: 30 0 0;")

        self.verticalLayout_5.addWidget(self.label_15)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_16 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(200, 16777215))
        self.label_16.setPixmap(QPixmap(u":/images/images/\u0413\u0430\u043b\u0435\u0440\u0435\u044f 1.jpg"))

        self.horizontalLayout_4.addWidget(self.label_16)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(200, 16777215))
        self.label_17.setPixmap(QPixmap(u":/images/images/\u0413\u0430\u043b\u0435\u0440\u0435\u044f 2.jpg"))

        self.horizontalLayout_4.addWidget(self.label_17)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(200, 16777215))
        self.label_18.setPixmap(QPixmap(u":/images/images/\u0413\u0430\u043b\u0435\u0440\u0435\u044f 3.jpg"))

        self.horizontalLayout_4.addWidget(self.label_18)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(700, 16777215))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: #636880;\n"
"	font-size: 18px;\n"
"	font-weight: 500;\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"	margin: 20 200 0;\n"
"}\n"
"QPushButton:hover {\n"
"	color: #636880;\n"
"	background-color: white;\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_19 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font-weight: 600;\n"
"font-size: 20px;\n"
"color: white;\n"
"margin: 30 0 0;")

        self.verticalLayout_6.addWidget(self.label_19)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_20 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(300, 16777215))
        self.label_20.setStyleSheet(u"font-size: 16px;\n"
"color: white;")

        self.horizontalLayout_5.addWidget(self.label_20)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(400, 16777215))
        self.lineEdit.setStyleSheet(u"margin: 5px 0 5px 5px;\n"
"color: white;\n"
"background-color: #4D5163;\n"
"font-size: 16px;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_21 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(300, 16777215))
        self.label_21.setStyleSheet(u"font-size: 16px;\n"
"color: white;")

        self.horizontalLayout_6.addWidget(self.label_21)

        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_2.setStyleSheet(u"margin: 5px 0 5px 5px;\n"
"color: white;\n"
"background-color: #4D5163;\n"
"font-size: 16px;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")

        self.horizontalLayout_6.addWidget(self.lineEdit_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_22 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(300, 16777215))
        self.label_22.setStyleSheet(u"font-size: 16px;\n"
"color: white;")

        self.horizontalLayout_7.addWidget(self.label_22)

        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_3.setStyleSheet(u"margin: 5px 0 5px 5px;\n"
"color: white;\n"
"background-color: #4D5163;\n"
"font-size: 16px;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")

        self.horizontalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_23 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(300, 16777215))
        self.label_23.setStyleSheet(u"font-size: 16px;\n"
"color: white;")

        self.horizontalLayout_8.addWidget(self.label_23)

        self.lineEdit_4 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_4.setStyleSheet(u"margin: 5px 0 5px 5px;\n"
"color: white;\n"
"background-color: #4D5163;\n"
"font-size: 16px;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")

        self.horizontalLayout_8.addWidget(self.lineEdit_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_24 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(300, 16777215))
        self.label_24.setStyleSheet(u"font-size: 16px;\n"
"color: white;")

        self.horizontalLayout_9.addWidget(self.label_24)

        self.lineEdit_5 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_5.setStyleSheet(u"margin: 5px 0 5px 5px;\n"
"color: white;\n"
"background-color: #4D5163;\n"
"font-size: 16px;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")

        self.horizontalLayout_9.addWidget(self.lineEdit_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_25 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(300, 16777215))
        self.label_25.setStyleSheet(u"font-size: 16px;\n"
"color: white;")

        self.horizontalLayout_10.addWidget(self.label_25)

        self.lineEdit_6 = QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(400, 16777215))
        self.lineEdit_6.setStyleSheet(u"margin: 5px 0 5px 5px;\n"
"color: white;\n"
"background-color: #4D5163;\n"
"font-size: 16px;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")

        self.horizontalLayout_10.addWidget(self.lineEdit_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_26 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(230, 16777215))
        self.label_26.setStyleSheet(u"font-size: 16px;\n"
"color: white;")

        self.horizontalLayout_11.addWidget(self.label_26)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"margin: 5px 0;\n"
"color: white;\n"
"background-color: #4D5163;\n"
"font-size: 16px;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")

        self.horizontalLayout_11.addWidget(self.comboBox)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: white;\n"
"	background-color: #636880;\n"
"	font-size: 18px;\n"
"	font-weight: 500;\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"	margin: 20 200 0;\n"
"}\n"
"QPushButton:hover {\n"
"	color: #636880;\n"
"	background-color: white;\n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u043c\u043d\u044b\u0439 \u0433\u043e\u0440\u043e\u0434: \u0416\u0438\u0432\u0438 \u0441\u043f\u043e\u0440\u0442\u043e\u043c", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043c\u043d\u044b\u0439 \u0433\u043e\u0440\u043e\u0434", None))
        self.label_13.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0438\u0432\u0438 \u0441\u043f\u043e\u0440\u0442\u043e\u043c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"      I \u0412\u0441\u0435\u0440\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u0438\u0435 \u0438\u0433\u0440\u044b \u0423\u043c\u043d\u044b\u0445 \u0433\u043e\u0440\u043e\u0434\u043e\u0432", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"    \u041e\u0431 \u0438\u0433\u0440\u0430\u0445", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"     I \u0412\u0441\u0435\u0440\u043e\u0441\u0441\u0438\u0439\u0441\u043a\u0438\u0435 \u0438\u0433\u0440\u044b \u0423\u043c\u043d\u044b\u0445 \u0433\u043e\u0440\u043e\u0434\u043e\u0432 - \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435,\n"
"\u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u043d\u043e\u0435 \u043d\u0430 \u0412\u043e\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0433\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0430\n"
"\u0436\u0438\u0442\u0435\u043b\u0435\u0439 \u0420\u043e\u0441\u0441\u0438\u0438 \u0432 \u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0435 \u0437\u0430\u043d\u044f\u0442\u0438\u044f \u0441\u043f\u043e\u0440\u0442\u043e\u043c.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"     \u0412\u0442\u043e\u0440\u043e\u0439 \u0432\u0430\u0436\u043d\u043e\u0439 \u0437\u0430\u0434\u0430\u0447\u0435\u0439 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043f\u043e\u043f\u0443\u043b\u044f\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u0442\u0443\u0440\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e,\n"
"\u043f\u0440\u043e\u043c\u044b\u0448\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u0438 \u0438\u043d\u0432\u0435\u0441\u0442\u0438\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u0430 \u0421\u0430\u0440\u0430\u0442\u043e\u0432\u0441\u043a\u043e\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"     \u041d\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u043a, \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435 \u0441\u043b\u0443\u0436\u0438\u0442 \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u044f\u0440\u043a\u043e\u0433\u043e \u043f\u0440\u0430\u0437\u0434-\n"
"\u043d\u0438\u043a\u0430 \u0444\u0435\u0434\u0435\u0440\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043c\u0430\u0441\u0448\u0442\u0430\u0431\u0430 \u0441 \u0430\u043a\u0442\u0438\u0432\u043d\u044b\u043c \u0432\u043e\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u0435\u043c \u0436\u0438\u0442\u0435\u043b\u0435\u0439\n"
"\u0421\u0430\u0440\u0430\u0442\u043e\u0432\u0441\u043a\u043e\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438.", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"    \u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f", None))
        self.label_27.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"     \u0413\u0430\u043b\u0435\u0440\u0435\u044f", None))
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_18.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0432\u0441\u0435 \u0444\u043e\u0442\u043e", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"     \u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c\u0441\u044f", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"       \u0424\u0418\u041e:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"       \u0412\u043e\u0437\u0440\u0430\u0441\u0442:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"       \u041f\u043e\u043b:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"       \u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u0438\u044f:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"       \u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"       Email:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"       \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043b\u0435\u0439\u0431\u043e\u043b", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0441\u043a\u0435\u0442\u0431\u043e\u043b", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0424\u0443\u0442\u0431\u043e\u043b", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043d\u043d\u0438\u0441", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0445\u043c\u0430\u0442\u044b", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0431\u0435\u0433", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0441\u0435\u0441\u0441\u0438\u0438", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

