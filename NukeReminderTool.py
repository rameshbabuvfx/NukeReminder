import datetime
import sys
import json

import nuke
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from UI import Nuke_reminder_UI
import ReminderWidget
import PathVariables


class NukeReminder(QWidget, Nuke_reminder_UI.Ui_Form):
    def __init__(self):
        super(NukeReminder, self).__init__()
        self.row_index = None
        self.setupUi(self)
        self.automate_resume_reminder()
        self.NewReminderPushButton.setIcon(QIcon(PathVariables.new_reminder_icon))
        self.RemindersListWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.NewReminderPushButton.clicked.connect(self.add_item_widget)

    def add_item_widget(self, message=None, end_time=None):
        """
        Adds widget in a list widget item
        """
        widget_item = QListWidgetItem(self.RemindersListWidget)
        self.RemindersListWidget.addItem(widget_item)
        self.reminder_widget = ReminderWidget.ReminderWidget(message=message, endtime=end_time)
        widget_item.setSizeHint(self.reminder_widget.sizeHint())
        self.RemindersListWidget.setItemWidget(widget_item, self.reminder_widget)
        self.reminder_widget.CloseReminderButton.clicked.connect(self.close_reminder_item)

    def close_reminder_item(self):
        """
        deletes the reminder row
        """
        self.RemindersListWidget.takeItem(self.RemindersListWidget.currentRow())

    def automate_resume_reminder(self):
        """
        Resumes the incomplete reminder tasks
        """
        with open(PathVariables.database, 'r+') as jsonFile:
            read_json = json.load(jsonFile)
            jsonFile.close()

        current_time = datetime.datetime.now()
        filter_list = []
        for count, reminders in enumerate(read_json['Active_reminders']):
            message = reminders['message']
            end_time = datetime.datetime.strptime(
                reminders['end_time'],
                "%Y-%m-%d %H:%M:%S"
            )
            resume_time = (end_time - current_time).total_seconds()
            if resume_time > 0:
                self.add_item_widget(message=message, end_time=end_time.time())
                filter_list.append(reminders)

        read_json['Active_reminders'] = filter_list
        with open(PathVariables.database, 'w+') as jsonFile:
            json.dump(read_json, jsonFile, indent=4)
            jsonFile.close()


if __name__ == '__main__':
    app = QApplication()
    obj = NukeReminder()
    obj.show()
    sys.exit(app.exec_())
