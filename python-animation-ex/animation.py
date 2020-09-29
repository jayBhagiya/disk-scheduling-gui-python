from turtle import *
from tkinter import *
import tkinter.font as font
from tkinter.ttk import *
from fcfs import fcfs_fun

hd_name = {1:"FCSF - First Come First Serve", 2:"SSTF - Shortest Seek Time First.", 3:"SCAN - Elevator", 4:"C-SCAN - Circular Scan", 5:"LOOK", 6:"C - LOOK"}
op, ls, hd = (1, [82,170,43,140,24,16,190], 50)
title = hd_name[op]

new_win = Tk()
new_win.title(title)

canvas = Canvas(master=new_win, width=712, height=600)
canvas.configure(bg='black')

new_heading = Label(canvas, font=('Courier', 24), text = title)
new_heading.configure(background='black', foreground='white')
canvas.pack()
new_heading.place(relx = 0.5, rely = 0.1, anchor = CENTER)

screen = TurtleScreen(canvas)
screen.bgcolor('black')
screen.setworldcoordinates(-30, -30, 210, 10)

tim = RawTurtle(screen)

tim.color('red')
tim.shape('turtle')
tim.shape("circle")
tim.turtlesize(.3, .3, 1)
tim.pensize(3)
tim.speed(1)
n = len(ls)
y = 0
for i in range(0, n):
    if i == 0:      # No drawing while the disktim goes to start position
        tim.penup()
        tim.goto(ls[i], y)
        tim.pendown()
        tim.stamp()
        tim.write(ls[i], False, align="right")
    else:           # Disktim draws its path to each request
        tim.goto(ls[i], y-2)
        tim.stamp()
        tim.write(ls[i], False, align="right")
        y -= 2
tim.hideturtle()
tim.speed(0)
tim.penup()
tim.goto(100, 5)
message1 = "Disk Scheduling Algorithm: " + str(op)
message2 = "Total Head Movement: "
tim.write(message1, False, align="center")     # Display algorithm used
tim.goto(100,4)
tim.write(message2, False, align="center")     # Display total movement
tim.pendown

new_win.mainloop()