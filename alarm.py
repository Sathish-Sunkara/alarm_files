# Import Required Library
from tkinter import *
import datetime
import time
import winsound
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("600x400")

# Use Threading
def Threading():
	t1=Thread(target=alarm)
	t1.start()

def alarm():
	# Infinite Loop
	while True:
		# Set Alarm
		set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

		# Wait for one seconds
		time.sleep(1)

		# Get current time
		current_time = datetime.datetime.now().strftime("%H:%M:%S")
		print(current_time,set_alarm_time)
		e1.delete(0,END)
		e1.insert(0,str(current_time))
		e2.delete(0,END)
		e2.insert(0,str(set_alarm_time))


		# Check whether set alarm is equal to current time or not
		if current_time == set_alarm_time:
			print("Time to Wake up")
			#display alaram
			e2.delete(0,END)
			e2.insert(0,"alarm ranged")
			# Playing sound
			winsound.PlaySound("sound.wav",winsound.SND_ASYNC)

# Add Labels, Frame, Button, Optionmenus
Label(root,text="Alarm Clock",font=("Helvetica 30 bold"),fg="red",bg = "cyan").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 20 bold"),fg = "green",bg = "cyan").pack(pady=15)

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT,padx=5)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT,padx=5)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT,padx=5)


Button(root,text="Set Alarm",font=("Helvetica 15 bold"),fg = "blue",bg = "cyan",command=Threading).pack(pady = 10)

#current time
l1 = Label(root,text = "TIME",font=("Helvetica 15"),fg="#702c1b",bg = "#90e0b0")
l1.pack(pady = 10)

e1 = Entry(root,text = "",font=("Helvetica 15"),fg="#160e52")
e1.pack()

# alarm time
l2 = Label(root,text = "ALARM TIME",font=("Helvetica 15"),fg="#702c1b",bg = "#90e0b0")
l2.pack(pady =10)

e2 = Entry(root,text = "",font=("Helvetica 15"),fg="#160e52")
e2.pack()



# Execute Tkinter
root.mainloop()

