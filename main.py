from tkinter import *
from tkinter.messagebox import showinfo
import webbrowser
from tkinter import ttk

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
		isAm = None
		if timeVar.get() == "AM":
			isAm = 1
		else:
			isAm = 0
		file.write(f"\n{isAm} {time}:00 {label}")
	showinfo("Saved!", f"Your Alarm saved successfully!")

def clear():
	labelEntryBox.delete(0, END)
	timeEntryBox.delete(0, END)


root = Tk()

root.title("Psycho Alarm Clock - Set your Alarms")
root.geometry("400x400")

# Font to be used throughout the software
fontName = "Calibri"

alarmStatus = StringVar("")
alarmStatus.set("Alarms Are Not Running Go to OPTIONS>RUN ALARMS to enable all alarms")

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


timeEntry = Label(root, text="Alarm Time: (e.g 12:00)")
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

alarmsLabel = Label(root, text="Your Alarms: ", font=(fontName, 25))
alarmsLabel.pack()

with open("save.txt", "r") as file:
	data = file.read()


scrollbarY = Scrollbar(root, orient = 'vertical')
scrollbarY.pack(fill=Y, side=RIGHT)

alarmsFrame = Text(root, yscrollcommand = scrollbarY.set)
alarmsFrame.pack()

if data == "":
	noAlarm = Label(alarmsFrame, text="No Alarm to Show. Add new to show it here.")
	noAlarm.pack()
else:
	newData = data.split("\n")
	for data in newData:
		print(data)
		am = None
		if data[0:1] == "0":
			am = "PM"
		else:
			am = "AM"
		alarmsFrame.insert(END, f"Alarm Label:{data[8:]}\nAlarm Time: {data[2:7]}{am}\n\n")

alarmsFrame.config(state=DISABLED)
# Main Menu
mainMenu = Menu(root)

# About Menu
aboutMenu = Menu(mainMenu, tearoff=0)
aboutMenu.add_command(label="About Software", command=aboutSoftware)
aboutMenu.add_command(label="Visit Website", command=visitWebsite)
mainMenu.add_cascade(label="About", menu=aboutMenu)




root.config(menu=mainMenu)

scrollbarY.config(command=alarmsFrame.yview)


statusBar = Frame(root, relief='groove', borderwidth=5)
alarmStatusBar = Label(statusBar, textvariable=alarmStatus)
alarmStatusBar.pack()
statusBar.pack(side=BOTTOM, fill=BOTH)
root.mainloop()