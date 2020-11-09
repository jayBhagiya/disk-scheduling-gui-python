# 82,170,43,140,24,16,190

from turtle import *
from tkinter import *
from tkinter import messagebox
from time import sleep
from tkinter.ttk import *
import matplotlib.pyplot as plt

from fcfs import fcfs_fun
from sstf import sstf_fun
from scan import scan_fun
from c_scan import c_scan_fun
from look import look_fun
from c_look import c_look_fun

root = Tk(className='Disk Scheduling in - python')

root.geometry('600x512')
root.configure(bg='black')

hd_name = {1:"FCSF - First Come First Serve", 2:"SSTF - Shortest Seek Time First.", 3:"SCAN - Elevator", 4:"C-SCAN - Circular Scan", 5:"LOOK", 6:"C - LOOK"}

var = IntVar()
req_var = StringVar()
head_var = StringVar()

def get_data():
    ls = req_var.get()
    hd = head_var.get()
    op = var.get()

    try:
        num_list = [int(num) for num in ls.split(',')]
    except:
        messagebox.showerror('Error', 'Please enter number in above sequence and in integer..')
        print("All the sequence number should be integer..")

    try:
        n_hd = int(hd)
    except:
        messagebox.showerror('Error', 'Please enter the head position')

    return (int(op), num_list, n_hd)

# def show_all_graph():
#     op, num_list, hd = get_data()
    
#     y = [1, 2, 3, 4, 5, 6, 7, 8]

#     x1, _ = fcfs_fun(num_list, hd)
#     x2, _ = sstf_fun(num_list, hd)
#     x3, _ = scan_fun(num_list, hd)
#     x4, _ = c_scan_fun(num_list, hd)
#     x5, _ = look_fun(num_list, hd)
#     x6, _ = c_look_fun(num_list, hd)

#     plt.plot(x1, y, label = "fcfs")
#     plt.plot(x2, y, label = "sstf")
#     plt.plot(x3, y, label = "scan")
#     plt.plot(x4, y, label = "c-scan")
#     plt.plot(x5, y, label = "look")
#     plt.plot(x6, y, label = "c-look")

#     plt.legend()
#     plt.show()

def show_seek_time():
    left = [num for num in range(1,7)]

    op, num_list, hd = get_data()

    height = [0, 0, 0, 0, 0, 0]

    _, height[0] = fcfs_fun(num_list, hd)
    _, height[1] = sstf_fun(num_list, hd)
    _, height[2] = scan_fun(num_list, hd)
    _, height[3] = c_scan_fun(num_list, hd)
    _, height[4] = look_fun(num_list, hd)
    _, height[5] = c_look_fun(num_list, hd)

    al_label = ['fcfs', 'sstf', 'scan', 'c-scan', 'look', 'c-look']

    plt.bar(left, height, tick_label = al_label, width = 0.8, color = ['red', 'green', 'blue', 'pink', 'orange', 'gray'] )

    plt.show()

def out_str(ls):
    str_ls = ""
    
    for i in range(1, len(ls)):
        if ls[i-1] > ls[i]:
            _temp = "( {} - {} ) + ".format(ls[i-1], ls[i])
        else:
            _temp = "( {} - {} ) + ".format(ls[i], ls[i-1])
        str_ls += _temp

    return str_ls

def openNewWindow():

    op, num_list, hd = get_data()

    if op == 1:
        ls, total = fcfs_fun(num_list, hd)
    elif op == 2:
        ls, total = sstf_fun(num_list, hd)
    elif op == 3:
        ls, total = scan_fun(num_list, hd)
    elif op == 4:
        ls, total = c_scan_fun(num_list, hd)
    elif op == 5:
        ls, total = look_fun(num_list, hd)
    else:
        ls, total = c_look_fun(num_list, hd)

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

    tim.color('light blue')
    tim.shape("circle")
    tim.turtlesize(.3, .3, 3)
    tim.pensize(3)
    tim.speed(1)
    n = len(ls)
    y = 0
    for i in range(0, n):
        if i == 0:      # No drawing while the disktim goes to start position
            tim.penup()
            tim.goto(ls[i], y)
            sleep(0.5)
            tim.pendown()
            tim.stamp()
            tim.write("Head : {}".format(ls[i]), False, align="left", font=("Courier", 12, "bold"))
            sleep(0.5)
        else:           # Disktim draws its path to each request
            tim.goto(ls[i], y-2)
            sleep(0.5)
            tim.stamp()
            tim.write(ls[i], False, align="left", font=('Courier', 12, 'bold'))
            y -= 2
            sleep(0.5)
    tim.hideturtle()
    tim.speed(0)
    tim.penup()
    tim.goto(100, 5)
    tim.pendown

    msg = "Total seek time is : " + str(total)
    tot_msg = Label(canvas, font=('Courier', 18), text = msg)
    tot_msg.configure(background='black', foreground='white')
    tot_msg.place(relx=0.5, rely = 0.8, anchor=CENTER)

def main_ui():
    heading = Label(root, font=('Courier', 24), text = 'Disk Scheduling')
    heading.configure(background='black', foreground='white')
    desc = Label(root, font=('Courier', 11), text = 'Enter requests in range of 0 to 199, in separated comma.\ne.g 80, 163, 95, 120, 59')
    desc.configure(background='black', foreground='white')
    req_lbl = Label(root, font=('Courier', 11), text = 'Requests : ')
    req_lbl.configure(background='black', foreground='white')
    req_entry = Entry(root, textvariable = req_var, font=('Courier', 11))
    head_lbl = Label(root, font=('Courier', 11), text = 'Read/write Head : ')
    head_lbl.configure(background='black', foreground='white')
    head_entry = Entry(root, textvariable = head_var, font=('Courier', 11))

    style = Style(root)
    style.configure("TRadiobutton", background = "black", foreground = "white")

    for i in range(1, 7):
        rb = Radiobutton(root, text=hd_name[i], variable=var, value=i)
        rb.place(relx = 0.3, rely = (0.45 + i/20), anchor = W )

    btn = Button(root, text = 'Show Animation !', command = openNewWindow)
    btn2 = Button(root, text = 'Show Bar Graph !', command = show_seek_time)
    # btn3 = Button(root, text = 'Show all Graph !', command = show_all_graph)

    heading.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    desc.place(relx = 0.5, rely = 0.2, anchor = CENTER)
    req_lbl.place(relx = 0.2, rely = 0.3, anchor = CENTER)
    req_entry.place(relx = 0.65, rely = 0.3, width=320, anchor = CENTER)
    head_lbl.place(relx = 0.2, rely = 0.4, anchor = CENTER)
    head_entry.place(relx = 0.65, rely = 0.4, width=320, anchor = CENTER)
    btn.place(relx = 0.5, rely = 0.85, anchor = CENTER)
    btn2.place(relx = 0.5, rely = 0.93, anchor = CENTER)
    # btn3.place(relx = 0.6, rely = 0.93, anchor = CENTER)

    root.mainloop()

if __name__ == "__main__":
    main_ui()