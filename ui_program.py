# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_program.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1521, 931)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_converted_text = QLabel(self.centralwidget)
        self.label_converted_text.setObjectName(u"label_converted_text")
        self.label_converted_text.setGeometry(QRect(40, 520, 471, 61))
        font1 = QFont()
        font1.setFamilies([u"NiseSega Cyrillic"])
        font1.setPointSize(18)
        self.label_converted_text.setFont(font1)
        self.label_converted_text.setAlignment(Qt.AlignCenter)
        self.original_text = QTextEdit(self.centralwidget)
        self.original_text.setObjectName(u"original_text")
        self.original_text.setGeometry(QRect(40, 160, 471, 251))
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(12)
        self.original_text.setFont(font2)
        self.original_text.setStyleSheet(u"border-color: white;\n"
"padding: 5px;")
        self.original_text.setFrameShape(QFrame.Box)
        self.original_text.setFrameShadow(QFrame.Plain)
        self.btn_performing = QPushButton(self.centralwidget)
        self.btn_performing.setObjectName(u"btn_performing")
        self.btn_performing.setGeometry(QRect(1110, 800, 211, 61))
        self.btn_performing.setFont(font1)
        self.btn_performing.setStyleSheet(u"QPushButton {\n"
"color: red;\n"
"border: 2px solid red;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1050, 620, 332, 131))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_performing = QLabel(self.layoutWidget)
        self.label_performing.setObjectName(u"label_performing")
        self.label_performing.setFont(font1)
        self.label_performing.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_performing)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_encode = QRadioButton(self.layoutWidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radio_encode)
        self.radio_encode.setObjectName(u"radio_encode")
        self.radio_encode.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.radio_encode.setFont(font3)

        self.horizontalLayout.addWidget(self.radio_encode)

        self.radio_decode = QRadioButton(self.layoutWidget)
        self.buttonGroup.addButton(self.radio_decode)
        self.radio_decode.setObjectName(u"radio_decode")
        self.radio_decode.setEnabled(True)
        self.radio_decode.setFont(font3)

        self.horizontalLayout.addWidget(self.radio_decode)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.converted_text = QTextEdit(self.centralwidget)
        self.converted_text.setObjectName(u"converted_text")
        self.converted_text.setGeometry(QRect(40, 630, 471, 251))
        self.converted_text.setFont(font2)
        self.converted_text.setStyleSheet(u"border-color: white;\n"
"padding: 5px;")
        self.converted_text.setFrameShape(QFrame.Box)
        self.converted_text.setFrameShadow(QFrame.Plain)
        self.converted_text.setReadOnly(True)
        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(40, 20, 491, 111))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_text = QLabel(self.layoutWidget_2)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setFont(font1)
        self.label_text.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_text)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radio_from_line = QRadioButton(self.layoutWidget_2)
        self.radio_from_line.setObjectName(u"radio_from_line")
        self.radio_from_line.setEnabled(True)
        self.radio_from_line.setFont(font3)

        self.horizontalLayout_4.addWidget(self.radio_from_line)

        self.radio_from_file = QRadioButton(self.layoutWidget_2)
        self.radio_from_file.setObjectName(u"radio_from_file")
        self.radio_from_file.setEnabled(True)
        self.radio_from_file.setFont(font3)

        self.horizontalLayout_4.addWidget(self.radio_from_file)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.btn_open_file = QPushButton(self.centralwidget)
        self.btn_open_file.setObjectName(u"btn_open_file")
        self.btn_open_file.setGeometry(QRect(640, 180, 141, 51))
        font4 = QFont()
        font4.setFamilies([u"NiseSega Cyrillic"])
        font4.setPointSize(16)
        self.btn_open_file.setFont(font4)
        self.btn_open_file.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"border: 2px solid white;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        self.label_open_key_n = QLabel(self.centralwidget)
        self.label_open_key_n.setObjectName(u"label_open_key_n")
        self.label_open_key_n.setGeometry(QRect(1190, 20, 51, 61))
        self.label_open_key_n.setFont(font1)
        self.label_open_key_n.setAlignment(Qt.AlignCenter)
        self.text_open_key_n = QTextEdit(self.centralwidget)
        self.text_open_key_n.setObjectName(u"text_open_key_n")
        self.text_open_key_n.setGeometry(QRect(940, 100, 551, 61))
        self.text_open_key_n.setFont(font2)
        self.text_open_key_n.setStyleSheet(u"border-color: white;\n"
"padding: 5px;")
        self.text_open_key_n.setFrameShape(QFrame.Box)
        self.text_open_key_n.setFrameShadow(QFrame.Plain)
        self.text_open_key_n.setReadOnly(False)
        self.text_open_key_s = QTextEdit(self.centralwidget)
        self.text_open_key_s.setObjectName(u"text_open_key_s")
        self.text_open_key_s.setGeometry(QRect(940, 260, 551, 61))
        self.text_open_key_s.setFont(font2)
        self.text_open_key_s.setStyleSheet(u"border-color: white;\n"
"padding: 5px;")
        self.text_open_key_s.setFrameShape(QFrame.Box)
        self.text_open_key_s.setFrameShadow(QFrame.Plain)
        self.text_open_key_s.setReadOnly(False)
        self.label_open_key_s = QLabel(self.centralwidget)
        self.label_open_key_s.setObjectName(u"label_open_key_s")
        self.label_open_key_s.setGeometry(QRect(1190, 180, 51, 61))
        self.label_open_key_s.setFont(font1)
        self.label_open_key_s.setAlignment(Qt.AlignCenter)
        self.btn_generate_open_keys = QPushButton(self.centralwidget)
        self.btn_generate_open_keys.setObjectName(u"btn_generate_open_keys")
        self.btn_generate_open_keys.setGeometry(QRect(1090, 550, 241, 51))
        self.btn_generate_open_keys.setFont(font4)
        self.btn_generate_open_keys.setStyleSheet(u"QPushButton {\n"
"color: Chartreuse;\n"
"border: 2px solid Chartreuse;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        self.label_closed_key_e = QLabel(self.centralwidget)
        self.label_closed_key_e.setObjectName(u"label_closed_key_e")
        self.label_closed_key_e.setGeometry(QRect(980, 360, 471, 51))
        self.label_closed_key_e.setFont(font1)
        self.label_closed_key_e.setAlignment(Qt.AlignCenter)
        self.text_closed_key_e = QTextEdit(self.centralwidget)
        self.text_closed_key_e.setObjectName(u"text_closed_key_e")
        self.text_closed_key_e.setGeometry(QRect(940, 440, 551, 61))
        self.text_closed_key_e.setFont(font2)
        self.text_closed_key_e.setStyleSheet(u"border-color: white;\n"
"padding: 5px;")
        self.text_closed_key_e.setFrameShape(QFrame.Box)
        self.text_closed_key_e.setFrameShadow(QFrame.Plain)
        self.file_path = QTextEdit(self.centralwidget)
        self.file_path.setObjectName(u"file_path")
        self.file_path.setGeometry(QRect(550, 250, 321, 121))
        self.file_path.setFont(font2)
        self.file_path.setStyleSheet(u"border-color: white;\n"
"padding: 5px;")
        self.file_path.setFrameShape(QFrame.Box)
        self.file_path.setFrameShadow(QFrame.Plain)
        self.file_path.setReadOnly(True)
        self.btn_switch_texts = QPushButton(self.centralwidget)
        self.btn_switch_texts.setObjectName(u"btn_switch_texts")
        self.btn_switch_texts.setGeometry(QRect(250, 450, 51, 51))
        font5 = QFont()
        font5.setFamilies([u"NiseSega Cyrillic"])
        font5.setPointSize(30)
        self.btn_switch_texts.setFont(font5)
        self.btn_switch_texts.setStyleSheet(u"QPushButton {\n"
"color: Cyan;\n"
"border: 2px solid Cyan;\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 90);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RSA", None))
        self.label_converted_text.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442:", None))
        self.original_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442", None))
        self.btn_performing.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0410\u0421\u0421\u0427\u0418\u0422\u0410\u0422\u042c", None))
        self.label_performing.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.radio_encode.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.radio_decode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.converted_text.setPlaceholderText("")
        self.label_text.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442:", None))
        self.radio_from_line.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0443\u0447\u043d\u0443\u044e", None))
        self.radio_from_file.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.btn_open_file.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0431\u0437\u043e\u0440", None))
        self.label_open_key_n.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.text_open_key_n.setPlaceholderText("")
        self.text_open_key_s.setPlaceholderText("")
        self.label_open_key_s.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.btn_generate_open_keys.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0413\u0415\u041d\u0415\u0420\u0418\u0420\u041e\u0412\u0410\u0422\u042c", None))
        self.label_closed_key_e.setText(QCoreApplication.translate("MainWindow", u"e (\u0437\u0430\u043a\u0440\u044b\u0442\u044b\u0439 \u043a\u043b\u044e\u0447)", None))
        self.text_closed_key_e.setPlaceholderText("")
        self.file_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b", None))
        self.btn_switch_texts.setText(QCoreApplication.translate("MainWindow", u"\u2191", None))
    # retranslateUi

