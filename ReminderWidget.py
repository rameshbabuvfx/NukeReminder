import sys
import time
import json

import nuke
from datetime import datetime, date
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from UI import reminder_UI
import PathVariables


class ReminderWidget(QWidget, reminder_UI.Ui_Form):
    def __init__(self, message=None, endtime=None):
        super(ReminderWidget, self).__init__()
        self.resume_end_time = endtime
        self.resume_message = message
        self.start_button = True
        self.read_json_data = None
        self.setupUi(self)
        self.modify_ui()
        self.connect_ui()
        if self.resume_message and self.resume_end_time:
            self.create_thread()

    def modify_ui(self):
        """
        Custom modifies in UI
        """
        self.StartReminderButton.setIcon(QIcon(PathVariables.start_reminder_icon))
        self.StopReminderButton.setIcon(QIcon(PathVariables.stop_reminder_icon))
        self.CloseReminderButton.setIcon(QIcon(PathVariables.close_reminder_icon))
        self.ReminderModeCombo.addItems(['Message PopUp', "Start Render", "Exit Nuke"])
        self.TimeSetEdit.setTime(self.resume_end_time)
        self.RemindertextEdit.setText(self.resume_message)

    def connect_ui(self):
        """
        Connects UI and custom functions
        """
        self.StartReminderButton.clicked.connect(self.create_thread)
        self.ReminderModeCombo.currentIndexChanged.connect(self.set_mode_widget)
        self.StopReminderButton.clicked.connect(self.stop_timer)

    def set_mode_widget(self):
        """
        Sets mode of reminder and changes functionalities
        """
        if self.ReminderModeCombo.currentText() == "Message PopUp":
            self.RemindertextEdit.setVisible(True)
            self.ReminderstackedWidget.setCurrentWidget(self.MessagePage)

        if self.ReminderModeCombo.currentText() == "Start Render":
            self.StartRenderNodeListWidget.setVisible(True)
            self.ReminderstackedWidget.setCurrentWidget(self.StartRenderPage)
            all_nodes = nuke.allNodes()
            write_nodes = []
            for node in all_nodes:
                if node.Class() == "Write":
                    node_name = node["name"].getValue()
                    write_nodes.append(node_name)
            self.StartRenderNodeListWidget.clear()
            node_items = list(dict.fromkeys(write_nodes))
            self.StartRenderNodeListWidget.addItems(node_items)

        if self.ReminderModeCombo.currentText() == "Exit Nuke":
            self.RemindertextEdit.setVisible(False)
            self.StartRenderNodeListWidget.setVisible(False)

    def create_thread(self):
        """
        Creates new thread and starts QThread
        """
        if self.ReminderModeCombo.currentText() == "Message PopUp":
            self.read_write_json()

        if self.start_button:
            self.endtime = self.TimeSetEdit.time()
            self.thread = ReminderThread(self.endtime)
            self.thread.running_timer.connect(self.set_timer_value)
            self.thread.running_progress.connect(self.set_progress_value)
            self.thread.start()
            self.start_button = False

    def set_timer_value(self, val):
        """
        Displays Timer in reminder label
        """
        self.TimerLable.setText(str(val))
        if self.ReminderModeCombo.currentText() == "Message PopUp":
            if str(val) == "0:0:1":
                self.thread.terminate()
                nuke.message(self.RemindertextEdit.toPlainText())

        if self.ReminderModeCombo.currentText() == "Start Render":
            if str(val) == "0:0:1":
                node_name = self.StartRenderNodeListWidget.currentItem().text()
                nuke.render(str(node_name))
                self.TimerLable.setText("DONE")
                self.thread.terminate()

        if self.ReminderModeCombo.currentText() == "Exit Nuke":
            if str(val) == "0:0:1":
                self.TimerLable.setText("0:0:0")
                self.thread.quit()
                nuke.scriptSave()
                nuke.scriptExit()

    def stop_timer(self):
        """
        Stops thread and reminder
        """
        self.thread.terminate()

    def set_progress_value(self, val):
        """
        sets progress values in progress bar widget
        """
        self.ReminderprogressBar.setValue(val)

    def read_write_json(self):
        """
        Read and Updates the json data for resumes incomplete reminders
        """
        start_time = datetime.now()
        endtime = f"{str(start_time.date())} {str(self.TimeSetEdit.time().toPython())}"
        reminder_data = {
            "end_time": endtime,
            "message": self.RemindertextEdit.toPlainText()
        }
        with open(PathVariables.database, 'r+') as jsonFile:
            self.read_json_data = json.load(jsonFile)
            jsonFile.close()
        self.read_json_data['Active_reminders'].append(reminder_data)
        reminders_list = self.read_json_data['Active_reminders']
        filter_reminders = []
        for i in range(len(reminders_list)):
            if reminders_list[i] not in reminders_list[i + 1:]:
                filter_reminders.append(reminders_list[i])
        self.read_json_data['Active_reminders'] = filter_reminders
        with open(PathVariables.database, 'w+') as jsonFile:
            json.dump(self.read_json_data, jsonFile, indent=4)
            jsonFile.close()


class ReminderThread(QThread):
    running_timer = Signal(datetime)
    running_progress = Signal(int)

    def __init__(self, end_time):
        super(ReminderThread, self).__init__()
        self.end_time = end_time

    def run(self):
        """
        Start(or)Runs the QThread
        """
        maximum_seconds = self.progress_value()
        while True:
            time.sleep(1)
            current_time = datetime.now()
            hours_diff = self.end_time.hour() - current_time.hour
            mins_diff = self.end_time.minute() - current_time.minute
            sec_diff = 60 - current_time.second
            time_counter = ("{}:{}:{}".format(hours_diff, mins_diff, sec_diff))
            self.running_timer.emit(time_counter)
            current_seconds = self.progress_value()
            progress_percentage = 100-(100*(current_seconds-0)/maximum_seconds)
            self.running_progress.emit(progress_percentage)

    def progress_value(self):
        """
        Calculates the progess bar value

        :return total_seconds:total seconds on end time
        :rtype: int
        """
        current_time = datetime.now()
        current_date = date.today()
        countdown_timer = "{} {}:{}:{}".format(
            current_date,
            self.end_time.hour(),
            self.end_time.minute(),
            59
        )
        total_seconds = (
                datetime.strptime(countdown_timer, '%Y-%m-%d %H:%M:%S') - current_time
        ).total_seconds()
        return int(total_seconds)


if __name__ == '__main__':
    app = QApplication()
    obj = ReminderWidget()
    obj.show()
    sys.exit(app.exec_())
