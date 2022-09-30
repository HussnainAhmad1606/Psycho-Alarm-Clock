from plyer import notification
from datetime import datetime
from time import sleep
import pygame
timeArrFinal = []

with open("save.txt", "r") as file:
	data = file.read()
	

if data == "":
		print("No Alarms")
else:
	print("Alarm Found")
	timeArr = data.split("\n")
	for time in timeArr:
		al = time.split(" ")
		print(len(al))
		alarm = [
		al[1],
		al[0]
		]
		timeArrFinal.append(alarm)
		print(al)
		al = None
	print(timeArrFinal)

def showAlert(label, time):
	notification.notify(
    title = label,
    message = f'Time is {time}',
    app_icon = None,
    timeout = 5
    )

loopRunning = True


def playSound():
	pygame.init()
	soundObj = pygame.mixer.Sound('sound.mp3')
	soundObj.play()
	sleep(5)
	soundObj.stop()


def checkTime():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	for alarm in timeArrFinal:
		if alarm[1] == current_time:
			print("This is alarm")
			showAlert(alarm[0], str(current_time)[:5])
			playSound()
			sleep(1)

while loopRunning:
	checkTime()
