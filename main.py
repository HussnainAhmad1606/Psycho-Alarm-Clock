from tkinter import *
from tkinter.messagebox import showinfo
import webbrowser


# Showing software info when user click on about in menu
def aboutSoftware():
	showinfo("About", "Software Version: 1.0\nProgrammer: Psycho Coder")

# Function will open github profile website in the browser
def visitWebsite():
	webbrowser.open("https://github.com/HussnainAhmad1606/")

# Function to save the alarm
def saveAlarm():
	with open("save.txt", "a") as file:
		time = alarmTimeVar.get()
		label = alarmLabelVar.get()	
		file.write(f"{label} - {time}{timeVar.get()}\n")
	showinfo("Saved!", "Your Alarm saved successfully!")

def clear():
	labelEntryBox.delete(0, END)
	timeEntryBox.delete(0, END)

root = Tk()

root.title("Psycho Alarm Clock - Set your Alarms")
root.geometry("400x400")

# Font to be used throughout the software
fontName = "Calibri"

# Alarm Label for Entry box
alarmLabelVar = StringVar("")
alarmTimeVar = StringVar("")
timeVar = StringVar("")

timeOptions = [
"AM",
"PM"
] 
timeVar.set(timeOptions[0])
# Main heading of the software
title = Label(root, text="Psycho Alarm Clock",font=(fontName, 20, "bold"))
title.pack()

labelEntry = Label(root, text="Alarm Label: ")
labelEntry.pack()

labelEntryBox = Entry(root, textvariable=alarmLabelVar)
labelEntryBox.pack()


timeEntry = Label(root, text="Alarm Time: ")
timeEntry.pack()

timeEntryBox = Entry(root, textvariable=alarmTimeVar)
timeEntryBox.pack()

ampm = OptionMenu(root, timeVar, *timeOptions)
ampm.pack()


# Save Alarm Button
saveAlarmBtn = Button(root, text="Save Alarm", command=saveAlarm)
saveAlarmBtn.pack()

# Clear Button
resetBtn = Button(root, text="Clear", command=clear)
resetBtn.pack()


# Main Menu
mainMenu = Menu(root)

# About Menu
aboutMenu = Menu(mainMenu, tearoff=0)
aboutMenu.add_command(label="About Software", command=aboutSoftware)
aboutMenu.add_command(label="Visit Website", command=visitWebsite)
mainMenu.add_cascade(label="About", menu=aboutMenu)



root.config(menu=mainMenu)



root.mainloop()