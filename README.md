# NukeReminder

Nuke Reminder is a reminder app fit inside nuke. it helps artist to remind their future tasks and more.

1. Nuke reminder can give reminders at particluar time.
2. User can set Schedule rendersand start renders at a particular given time.
3. Exit nuke at the given time by the user.
4. Additional reminders resumes after restarting nuke.
   
   ![Nuke_Reminder](https://user-images.githubusercontent.com/73053972/120096509-87cc0400-c149-11eb-877b-f303ff61a26d.png)



# Installation

1. Copy the NukeReminder to `/.nuke` folder.
2. Add NukeReminder path in init.py
3. Like this -> `nuke.pluginAddPath("C:/Users/yourname/.nuke/NukeReminder")`
4. Open nuke and rignt click on tab header add nukeReminder panel.

![Nuke_Reminder_Panel](https://user-images.githubusercontent.com/73053972/120096513-92869900-c149-11eb-81fc-f48d91133814.png)
6. Save workspace as compositing, make sure that set by defalut launch compositing workspace.

![Nuke_Reminder_workspace_setup](https://user-images.githubusercontent.com/73053972/120096516-974b4d00-c149-11eb-9d8d-e2526ba5721f.png)

7. Saving workspace gives additional feature called Resume reminder after restart nuke.

# How to Use:

1. Add Reminders by clicking on plus icon.
2. Set Reminder mode messagepopup, startrender, exitnuke.
3. set reminder time in 24 hrs format.
4. Content widget, Add message text or select write node depends on reminder mode
5. Start reminder.
6. Stop reminder.
7. Disaplays remianing time.
8. Delete/Close/Exit reminder on clicking this power button.


