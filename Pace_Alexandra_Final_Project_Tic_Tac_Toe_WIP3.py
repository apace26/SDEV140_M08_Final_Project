"""
Program: Pace_Alexandra_Final_Project_Tic_Tac_Toe_WIP2.py
Author: Alexandra Pace
Date: 2/27/2024
Classic Tic-Tac-Toe game
Allows user input through cursor movement and clicking buttons
User selects x or o then chooses where to make their mark
Engages in taking turns with computer
Three marks in a row result in a winner or a draw
Records results that can be displayed to user as output
"""

import tkinter as tk
from tkinter import *

window = tk.Tk()    # create window for widgets
window.title('Tic Tac Toe') # create title
window.geometry('800x450')  # set window width and height
window.resizable(False, False)  # keep window at fixed width and height

bg = PhotoImage(file='images/tic_tac_toe_background_800x450.png')   # store background image in variable

my_canvas = Canvas(window, width=800, height=450, borderwidth=0, highlightthickness=0)  # set up canvas
my_canvas.pack()

my_canvas.create_image(0,0, image=bg, anchor="nw")  # display background image on canvas

# function that allows x/o buttons to be placed in grid
# sets x counter variables to 1
# allows show() functions to restrict user selection to x marks
def select_x1():
    global x_counter1   # sets x counter to a global variable to alter same variable name outside of function
    x_counter1 = 1  # changes x counter variable to hold a value of 1
    x_o_1_button.place(x=260, y=80) # place x/o button in grid - changes coordinates
    global x_counter2
    x_counter2 = 1
    x_o_2_button.place(x=367, y=80)
    global x_counter3
    x_counter3 = 1
    x_o_3_button.place(x=473, y=80)
    global x_counter4
    x_counter4 = 1
    x_o_4_button.place(x=260, y=187)
    global x_counter5
    x_counter5 = 1
    x_o_5_button.place(x=367, y=187)
    global x_counter6
    x_counter6 = 1
    x_o_6_button.place(x=473, y=187)
    global x_counter7
    x_counter7 = 1
    x_o_7_button.place(x=260, y=298)
    global x_counter8
    x_counter8 = 1
    x_o_8_button.place(x=367, y=298)
    global x_counter9
    x_counter9 = 1
    x_o_9_button.place(x=473, y=298)
    x_button['state'] = 'disabled'  # disable x selection button
    o_button['state'] = 'disabled'  # disable o selection button

x_button = Button(window, text='x', width=7, height=2, bg='#ffffff', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=select_x1)    # create x selection button
x_button.place(x=600, y=80)

# function that allows x/o buttons to be placed in grid
# allows show() functions to restrict user selection to o marks
def select_o1():
    x_o_1_button.place(x=260, y=80) # place x/o button in grid - changes coordinates
    x_o_2_button.place(x=367, y=80)
    x_o_3_button.place(x=473, y=80)
    x_o_4_button.place(x=260, y=187)
    x_o_5_button.place(x=367, y=187)
    x_o_6_button.place(x=473, y=187)
    x_o_7_button.place(x=260, y=298)
    x_o_8_button.place(x=367, y=298)
    x_o_9_button.place(x=473, y=298)
    x_button['state'] = 'disabled'  # disable x selection button
    o_button['state'] = 'disabled'  # disable o selection button

o_button = Button(window, text='o', width=7, height=2, bg='#ffffff', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=select_o1)    # create o selection button
o_button.place(x=600, y=200)

# initialize x counters to 0
x_counter1 = 0
x_counter2 = 0
x_counter3 = 0
x_counter4 = 0
x_counter5 = 0
x_counter6 = 0
x_counter7 = 0
x_counter8 = 0
x_counter9 = 0

# functions to determine whether to show x or o
def show_1():
    if x_counter1 == 1:
        x_img_Label1.place(x=260, y=80) # places x on grid
    else:
        o_img_Label1.place(x=260, y=80) # places o on grid
    x_o_1_button.place_forget() # disable this x_o button on grid

def show_2():
    if x_counter2 == 1:
        x_img_Label2.place(x=367, y=80)
    else:
        o_img_Label2.place(x=367, y=80)
    x_o_2_button.place_forget()

def show_3():
    if x_counter3 == 1:
        x_img_Label3.place(x=473, y=80)
    else:
        o_img_Label3.place(x=473, y=80)
    x_o_3_button.place_forget()

def show_4():
    if x_counter4 == 1:
        x_img_Label4.place(x=260, y=190)
    else:
        o_img_Label4.place(x=260, y=190)
    x_o_4_button.place_forget()

def show_5():
    if x_counter5 == 1:
        x_img_Label5.place(x=367, y=187)
    else:
        o_img_Label5.place(x=367, y=187)
    x_o_5_button.place_forget()

def show_6():
    if x_counter6 == 1:
        x_img_Label6.place(x=473, y=187)
    else:
        o_img_Label6.place(x=473, y=187)
    x_o_6_button.place_forget()

def show_7():
    if x_counter7 == 1:
        x_img_Label7.place(x=260, y=298)
    else:
        o_img_Label7.place(x=260, y=298)
    x_o_7_button.place_forget()

def show_8():
    if x_counter8 == 1:
        x_img_Label8.place(x=367, y=298)
    else:
        o_img_Label8.place(x=367, y=298)
    x_o_8_button.place_forget()

def show_9():
    if x_counter9 == 1:
        x_img_Label9.place(x=473, y=298)
    else:
        o_img_Label9.place(x=473, y=298)
    x_o_9_button.place_forget()

# create x/o buttons for grid
x_o_1_button = Button(window, width=10, height=5, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_1)
x_o_1_button.place_forget()

x_o_2_button = Button(window, width=10, height=5, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_2)
x_o_2_button.place_forget()

x_o_3_button = Button(window, width=10, height=5, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_3)
x_o_3_button.place_forget()

x_o_4_button = Button(window, width=10, height=5, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_4)
x_o_4_button.place_forget()

x_o_5_button = Button(window, width=10, height=5, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_5)
x_o_5_button.place_forget()

x_o_6_button = Button(window, width=10, height=5, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_6)    
x_o_6_button.place_forget()

x_o_7_button = Button(window, width=10, height=5, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_7)
x_o_7_button.place_forget()

x_o_8_button = Button(window, width=10, height=5, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_8)
x_o_8_button.place_forget()

x_o_9_button = Button(window, width=10, height=5, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_9)
x_o_9_button.place_forget()

x_image1 = PhotoImage(file='images/x_1_67x72.png')  # store column 1/row 1 x_image1 in variable
x_img_Label1 = tk.Label(window, image=x_image1, borderwidth=0, highlightthickness=0)    # display x_image1 in column 1/row 1 of grid
x_img_Label1.place_forget()

o_image1 = PhotoImage(file='images/o_1_67x72.png')  # store column 1/row 1 o_image1 in variable
o_img_Label1 = tk.Label(window, image=o_image1, borderwidth=0, highlightthickness=0)    # display o_image1 in column 1/row 1 of grid
o_img_Label1.place_forget()

x_image2 = PhotoImage(file='images/x_2_67x72.png')  # store column 2/row 1 x_image2 in variable
x_img_Label2 = tk.Label(window, image=x_image2, borderwidth=0, highlightthickness=0)    # display x_image2 in column 2/row 1 of grid
x_img_Label2.place_forget()

o_image2 = PhotoImage(file='images/o_2_67x72.png')  # store column 2/row 1 o_image2 in variable
o_img_Label2 = tk.Label(window, image=o_image2, borderwidth=0, highlightthickness=0)    # display o_image2 in column 2/row 1 of grid
o_img_Label2.place_forget()

x_image3 = PhotoImage(file='images/x_3_67x72.png')  # store column 3/row 1 x_image3 in variable
x_img_Label3 = tk.Label(window, image=x_image3, borderwidth=0, highlightthickness=0)    # display x_image3 in column 3/row 1 of grid
x_img_Label3.place_forget()

o_image3 = PhotoImage(file='images/o_3_67x72.png')  # store column 3/row 1 o_image3 in variable
o_img_Label3 = tk.Label(window, image=o_image3, borderwidth=0, highlightthickness=0)    # display o_image3 in column 3/row 1 of grid
o_img_Label3.place_forget()

x_image4 = PhotoImage(file='images/x_4_67x72.png')  # store column 1/row 2 x_image4 in variable
x_img_Label4 = tk.Label(window, image=x_image4, borderwidth=0, highlightthickness=0)    # display x_image4 in column 1/row 2 of grid
x_img_Label4.place_forget()

o_image4 = PhotoImage(file='images/o_4_67x72.png')  # store column 1/row 2 o_image4 in variable
o_img_Label4 = tk.Label(window, image=o_image4, borderwidth=0, highlightthickness=0)    # display o_image4 in column 1/row 2 of grid
o_img_Label4.place_forget()

x_image5 = PhotoImage(file='images/x_5_67x72.png')  # store column 2/row 2 x_image5 in variable
x_img_Label5 = tk.Label(window, image=x_image5, borderwidth=0, highlightthickness=0)    # display x_image5 in column 2/row 2 of grid
x_img_Label5.place_forget()

o_image5 = PhotoImage(file='images/o_5_67x72.png')  # store column 2/row 2 o_image5 in variable
o_img_Label5 = tk.Label(window, image=o_image5, borderwidth=0, highlightthickness=0)    # display o_image5 in column 2/row 2 of grid
o_img_Label5.place_forget()

x_image6 = PhotoImage(file='images/x_6_67x72.png')  # store column 3/row 2 x_image6 in variable
x_img_Label6 = tk.Label(window, image=x_image6, borderwidth=0, highlightthickness=0)    # display x_image6 in column 3/row 2 of grid
x_img_Label6.place_forget()

o_image6 = PhotoImage(file='images/o_6_67x72.png')  # store column 3/row 2 o_image6 in variable
o_img_Label6 = tk.Label(window, image=o_image6, borderwidth=0, highlightthickness=0)    # display o_image6 in column 3/row 2 of grid
o_img_Label6.place_forget()

x_image7 = PhotoImage(file='images/x_7_67x72.png')  # store column 1/row 3 x_image7 in variable
x_img_Label7 = tk.Label(window, image=x_image7, borderwidth=0, highlightthickness=0)    # display x_image7 in column 1/row 3 of grid
x_img_Label7.place_forget()

o_image7 = PhotoImage(file='images/o_7_67x72.png')  # store column 1/row 3 o_image7 in variable
o_img_Label7 = tk.Label(window, image=o_image7, borderwidth=0, highlightthickness=0)  # display o_image7 in column 1/row 3 of grid  
o_img_Label7.place_forget()

x_image8 = PhotoImage(file='images/x_8_67x72.png')  # store column 2/row 3 x_image8 in variable
x_img_Label8 = tk.Label(window, image=x_image8, borderwidth=0, highlightthickness=0)    # display x_image8 in column 2/row 3 of grid
x_img_Label8.place()

o_image8 = PhotoImage(file='images/o_8_67x72.png')  # store column 2/row 3 o_image8 in variable
o_img_Label8 = tk.Label(window, image=o_image8, borderwidth=0, highlightthickness=0)    # display o_image8 in column 2/row 3 of grid
o_img_Label8.place_forget()

x_image9 = PhotoImage(file='images/x_9_67x72.png')  # store column 3/row 3 x_image9 in variable
x_img_Label9 = tk.Label(window, image=x_image9, borderwidth=0, highlightthickness=0)    # display x_image9 in column 3/row 3 of grid
x_img_Label9.place_forget()

o_image9 = PhotoImage(file='images/o_9_67x72.png')  # store column 3/row 3 o_image9 in variable
o_img_Label9 = tk.Label(window, image=o_image9, borderwidth=0, highlightthickness=0)    # display o_image9 in column 3/row 3 of grid
o_img_Label9.place_forget()

window.mainloop()   # execute mainloop()