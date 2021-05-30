# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Nuke_reminder_UI.ui'
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
        Form.resize(488, 606)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.NukeReminderLabel = QLabel(Form)
        self.NukeReminderLabel.setObjectName(u"NukeReminderLabel")
        font = QFont()
        font.setFamily(u"hooge 05_53")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.NukeReminderLabel.setFont(font)
        self.NukeReminderLabel.setCursor(QCursor(Qt.CrossCursor))

        self.horizontalLayout.addWidget(self.NukeReminderLabel)

        self.NewReminderPushButton = QPushButton(Form)
        self.NewReminderPushButton.setObjectName(u"NewReminderPushButton")
        self.NewReminderPushButton.setMaximumSize(QSize(30, 16777215))
        self.NewReminderPushButton.setStyleSheet(u"background-color: rgb(46, 46, 46);")
        self.NewReminderPushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.NewReminderPushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.RemindersListWidget = QListWidget(Form)
        self.RemindersListWidget.setObjectName(u"RemindersListWidget")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Light")
        self.RemindersListWidget.setFont(font1)

        self.gridLayout.addWidget(self.RemindersListWidget, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.NukeReminderLabel.setText(QCoreApplication.translate("Form", u"NUKE REMINDER", None))
        self.NewReminderPushButton.setText("")
    # retranslateUi

