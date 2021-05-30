import os

new_reminder_icon = "{}/{}/{}/new-reminder.png".format(os.path.dirname(__file__), "UI", "Icons").replace(
    "\\", "/")
start_reminder_icon = "{}/{}/{}/start-reminder.png".format(os.path.dirname(__file__), "UI", "Icons").replace(
    "\\", "/")
stop_reminder_icon = "{}/{}/{}/stop-reminder.png".format(os.path.dirname(__file__), "UI", "Icons").replace(
    "\\", "/")
close_reminder_icon = "{}/{}/{}/close-reminder.png".format(os.path.dirname(__file__), "UI", "Icons").replace(
    "\\", "/")
database = "{}/{}/reminder_database.json".format(os.path.dirname(__file__), "database").replace("\\", "/")
