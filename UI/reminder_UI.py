# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reminder_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(574, 189)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.ReminderModeCombo = QComboBox(self.frame)
        self.ReminderModeCombo.setObjectName(u"ReminderModeCombo")
        self.ReminderModeCombo.setMinimumSize(QSize(0, 30))
        self.ReminderModeCombo.setMaximumSize(QSize(120, 16777215))
        font = QFont()
        font.setFamily(u"Nirmala UI")
        self.ReminderModeCombo.setFont(font)
        self.ReminderModeCombo.setCursor(QCursor(Qt.PointingHandCursor))
        self.ReminderModeCombo.setStyleSheet(u"")

        self.gridLayout.addWidget(self.ReminderModeCombo, 0, 0, 1, 1)

        self.TimerLable = QLabel(self.frame)
        self.TimerLable.setObjectName(u"TimerLable")
        self.TimerLable.setMinimumSize(QSize(128, 0))
        font1 = QFont()
        font1.setFamily(u"LCDMono2")
        font1.setPointSize(41)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.TimerLable.setFont(font1)
        self.TimerLable.setCursor(QCursor(Qt.CrossCursor))
        self.TimerLable.setStyleSheet(u"color: rgb(176, 176, 176);")
        self.TimerLable.setLineWidth(0)
        self.TimerLable.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.TimerLable, 0, 2, 3, 1)

        self.StopReminderButton = QPushButton(self.frame)
        self.StopReminderButton.setObjectName(u"StopReminderButton")
        self.StopReminderButton.setMinimumSize(QSize(0, 25))
        self.StopReminderButton.setMaximumSize(QSize(120, 16777215))
        self.StopReminderButton.setFont(font)
        self.StopReminderButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.StopReminderButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.461285, y1:0, x2:0.479, y2:0.971682, stop:0 rgba(101, 101, 101, 255), stop:1 rgba(47, 47, 47, 255));\n"
"	border-radius:6px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.442, y1:1, x2:0.439, y2:0.0285002, stop:0 rgba(101, 101, 101, 255), stop:1 rgba(47, 47, 47, 255));\n"
"}")

        self.gridLayout.addWidget(self.StopReminderButton, 2, 1, 1, 1)

        self.TimeSetEdit = QTimeEdit(self.frame)
        self.TimeSetEdit.setObjectName(u"TimeSetEdit")
        self.TimeSetEdit.setMinimumSize(QSize(0, 30))
        self.TimeSetEdit.setMaximumSize(QSize(120, 16777215))
        self.TimeSetEdit.setFont(font)
        self.TimeSetEdit.setStyleSheet(u"")
        self.TimeSetEdit.setCurrentSection(QDateTimeEdit.HourSection)

        self.gridLayout.addWidget(self.TimeSetEdit, 1, 0, 1, 1)

        self.ReminderprogressBar = QProgressBar(self.frame)
        self.ReminderprogressBar.setObjectName(u"ReminderprogressBar")
        self.ReminderprogressBar.setMaximumSize(QSize(10000, 4))
        font2 = QFont()
        font2.setUnderline(False)
        self.ReminderprogressBar.setFont(font2)
        self.ReminderprogressBar.setStyleSheet(u"QProgressBar{\n"
"	border-radius:3px;\n"
"}\n"
"QProgressBar:chunk{\n"
"	border-radius:2px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(159, 80, 210, 255), stop:1 rgba(88, 197, 191, 255));\n"
"}")
        self.ReminderprogressBar.setValue(0)
        self.ReminderprogressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.ReminderprogressBar, 3, 0, 1, 3)

        self.StartReminderButton = QPushButton(self.frame)
        self.StartReminderButton.setObjectName(u"StartReminderButton")
        self.StartReminderButton.setMinimumSize(QSize(115, 25))
        self.StartReminderButton.setMaximumSize(QSize(120, 16777215))
        self.StartReminderButton.setFont(font)
        self.StartReminderButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.StartReminderButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.461285, y1:0, x2:0.479, y2:0.971682, stop:0 rgba(101, 101, 101, 255), stop:1 rgba(47, 47, 47, 255));\n"
"	border-radius:6px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.442, y1:1, x2:0.439, y2:0.0285002, stop:0 rgba(101, 101, 101, 255), stop:1 rgba(47, 47, 47, 255));\n"
"}")

        self.gridLayout.addWidget(self.StartReminderButton, 2, 0, 1, 1)

        self.CloseReminderButton = QPushButton(self.frame)
        self.CloseReminderButton.setObjectName(u"CloseReminderButton")
        self.CloseReminderButton.setMaximumSize(QSize(14, 14))
        self.CloseReminderButton.setStyleSheet(u"QPushButton{\n"
"	border-radius:7px;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(88, 88, 88);\n"
"}")

        self.gridLayout.addWidget(self.CloseReminderButton, 0, 3, 1, 1)

        self.ReminderstackedWidget = QStackedWidget(self.frame)
        self.ReminderstackedWidget.setObjectName(u"ReminderstackedWidget")
        self.ReminderstackedWidget.setMinimumSize(QSize(0, 100))
        self.ReminderstackedWidget.setMaximumSize(QSize(176, 16777215))
        self.ReminderstackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.MessagePage = QWidget()
        self.MessagePage.setObjectName(u"MessagePage")
        self.gridLayout_3 = QGridLayout(self.MessagePage)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.RemindertextEdit = QTextEdit(self.MessagePage)
        self.RemindertextEdit.setObjectName(u"RemindertextEdit")
        self.RemindertextEdit.setEnabled(True)
        self.RemindertextEdit.setMinimumSize(QSize(0, 80))
        self.RemindertextEdit.setMaximumSize(QSize(176, 16777215))
        self.RemindertextEdit.setStyleSheet(u"QTextEdit{\n"
"	\n"
"	font: 8pt \"Comic Sans MS\";\n"
"	border-style:solid;	\n"
"	border-width:2px;\n"
"	border-radius:10px;\n"
"	border-top-color: rgb(158, 82, 210);\n"
"	border-left-color: rgb(158, 82, 210);\n"
"	border-bottom-color: rgb(89, 196, 191);\n"
"	border-right-color: rgb(89, 195, 191);\n"
"}")

        self.gridLayout_3.addWidget(self.RemindertextEdit, 0, 0, 1, 1)

        self.ReminderstackedWidget.addWidget(self.MessagePage)
        self.StartRenderPage = QWidget()
        self.StartRenderPage.setObjectName(u"StartRenderPage")
        self.gridLayout_4 = QGridLayout(self.StartRenderPage)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.StartRenderNodeListWidget = QListWidget(self.StartRenderPage)
        self.StartRenderNodeListWidget.setObjectName(u"StartRenderNodeListWidget")
        self.StartRenderNodeListWidget.setStyleSheet(u"QListWidget{\n"
"	\n"
"	font: 8pt \"Comic Sans MS\";\n"
"	border-style:solid;	\n"
"	border-width:2px;\n"
"	border-radius:10px;\n"
"	border-top-color: rgb(158, 82, 210);\n"
"	border-left-color: rgb(158, 82, 210);\n"
"	border-bottom-color: rgb(89, 196, 191);\n"
"	border-right-color: rgb(89, 195, 191);\n"
"}")

        self.gridLayout_4.addWidget(self.StartRenderNodeListWidget, 0, 0, 1, 1)

        self.ReminderstackedWidget.addWidget(self.StartRenderPage)

        self.gridLayout.addWidget(self.ReminderstackedWidget, 0, 1, 2, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.ReminderstackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TimerLable.setText(QCoreApplication.translate("Form", u"00:00:00", None))
        self.StopReminderButton.setText(QCoreApplication.translate("Form", u"STOP", None))
        self.TimeSetEdit.setDisplayFormat(QCoreApplication.translate("Form", u"hh:mm:ss ", None))
        self.StartReminderButton.setText(QCoreApplication.translate("Form", u"START", None))
        self.CloseReminderButton.setText("")
        self.RemindertextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Add Message Here.....", None))
    # retranslateUi

